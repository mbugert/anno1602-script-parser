import enum
from typing import Any, Type, Optional

from lark import ParseTree, ParseError
from lark.visitors import Interpreter

from parser.game.constants import NUMMER


class ScriptInterpreter(Interpreter):
    """
    Parsing a 1602 script with grammar.lark produces a ParseTree. This
    interpreter walks over the parse tree and converts its contents into plain
    Python objects.
    """

    FILL_FORWARD = "__fill_forward__"
    FILL_BACKWARD = "__fill__backward__"

    def __init__(
        self,
        external_vars: Optional[dict[str, Any]] = None,
        enums: Optional[list[Type[enum.IntEnum]]] = None,
    ):
        """
        :param external_vars: any external variables that are referenced but
                              not defined in the script, without which parsing
                              would fail
        :param enums: in case a variable identifier cannot be resolved against
                      a variable defined in the script, or a variable from
                      external_vars, it can be looked up in this list of enums
        """
        self.enums = enums or []
        self.vars = external_vars or {}
        # Each object introduces a new scope for properties. There can be
        # properties on the top-level scope without any object definition,
        # so initialize the stack with an empty dict for the top-level scope.
        # Variables appear to be globally scoped and do not need a stack.
        self.properties = [{}]

    def start(self, tree: ParseTree) -> dict:
        child_objs = self.visit_children(tree)

        # child_objs will contain None's from variable definitions, remove
        # those (only keep properties)
        properties_objects = [e for e in child_objs if e is not None]

        object_ = self._aggregate_duplicate_dict_items(properties_objects)
        return object_

    def def_object(self, tree: ParseTree) -> tuple[str, dict]:
        """
        Aggregate all properties & sub-objects (in the case of a simple
        object), or all numbered sub-objects (in the case of numbered
        sub-objects) of an object into one object (a dict), and return it
        alongside its identifier.
        """
        # open new scope
        self.properties.append({})

        # collect object contents from subtrees
        child_objs = self.visit_children(tree)
        object_identifier = child_objs[0].value
        has_numbered_objects = type(child_objs[1]) is tuple
        if not has_numbered_objects:
            # a regular non-numbered object
            assert len(child_objs) == 2 and type(child_objs[1]) is dict
            overall_object = child_objs[1]
        else:
            # if there are numbered objects, we need to aggregate the list of
            # them into a single object, and apply ObjFill logic
            overall_object = {}

            # List of prototype objects to use for pre-populating other
            # objects. The int represents the Nummer of the first object to be
            # pre-populated (all subsequent numbered objects in that object
            # will be populated too).
            fill_proto_objects: list[tuple[int, dict]] = []

            for number, obj in child_objs[1:]:
                obj_filled = {}

                # detect prototype object used for forward filling
                if fill_forward := obj.get(self.FILL_FORWARD):
                    fill_from_number, fill_ident = fill_forward
                    assert fill_ident == object_identifier
                    fill_proto_objects.append((fill_from_number, obj))

                # apply forward filling (if applicable)
                if fill_proto_objects:
                    for fill_from_number, proto_obj in fill_proto_objects:
                        if number >= fill_from_number:
                            obj_filled |= proto_obj

                # apply backward filling (if applicable)
                if fill_backward := obj.get(self.FILL_BACKWARD):
                    recalled_obj = overall_object[fill_backward]
                    obj_filled |= recalled_obj

                # finally, apply properties of the object itself
                obj_filled |= obj
                # remove special fill properties
                obj_filled.pop(self.FILL_FORWARD, None)
                obj_filled.pop(self.FILL_BACKWARD, None)
                overall_object[number] = obj_filled

        # close scope
        self.properties.pop()
        return object_identifier, overall_object

    def object_content(self, tree: ParseTree) -> dict:
        child_objs = self.visit_children(tree)
        object_ = self._aggregate_duplicate_dict_items(child_objs)
        return object_

    def numbered_object(self, tree: ParseTree) -> tuple[int, dict[str, Any]]:
        """
        Aggregate all properties and sub-objects of a numbered object into one
        object (a dict), and return it alongside its number.
        """
        child_objs = self.visit_children(tree)

        object_contents = []
        number = None
        for obj in child_objs:
            # child_objs will contain None's from variable definitions, remove
            # those (only keep properties)
            if obj is None:
                continue
            elif type(obj) is tuple:
                if obj[0] == NUMMER:
                    assert number is None
                    number = obj[1]
                else:
                    # special ObjFill properties
                    object_contents.append(obj)
            elif type(obj) is dict:
                # dict with properties and sub-objects (there can be multiple
                # of these dicts for a single numbered object, in case the
                # property/object definitions are interrupted by variable
                # definitions)
                object_contents += obj.items()
        object_ = self._aggregate_duplicate_dict_items(object_contents)
        return number, object_

    def def_number_absolute(self, tree: ParseTree) -> tuple[str, Any]:
        """
        Define or overwrite the "Nummer" property in the current scope. Return
        the name the property and its new value.
        """
        _, value = self.visit_children(tree)
        self.properties[-1][NUMMER] = value
        return NUMMER, value

    def def_number_relative(self, tree: ParseTree) -> tuple[str, Any]:
        """
        Modify the "Nummer" property in the current scope by adding some delta
        to it. Return the name the property and its new value.
        """
        _, delta = self.visit_children(tree)

        if NUMMER not in self.properties[-1]:
            # exception to cover the ugly first occurrence of "Nummer" in
            # HAEUSER.COD (which is "@Nummer: 0")
            new_value = delta
        else:
            new_value = self.properties[-1][NUMMER] + delta
        self.properties[-1][NUMMER] = new_value

        return NUMMER, new_value

    def property_value(self, tree: ParseTree) -> Any | tuple:
        value = self.visit_children(tree)
        # unpack singleton list, tuple-ify list-typed values
        value = value[0] if len(value) == 1 else tuple(value)
        return value

    def def_property_absolute(self, tree: ParseTree) -> tuple[str, Any]:
        """
        Define or overwrite a property in the current scope. Return the name
        the property and its new value.
        """
        prop, value_tree = tree.children
        value = self.visit(value_tree)
        self.properties[-1][prop.value] = value

        return prop.value, value

    def def_property_relative(self, tree: ParseTree) -> tuple[str, Any]:
        """
        Modify a property in the current scope by adding some delta to it.
        Return the name the property and its new value.
        """
        prop, delta_tree = tree.children
        if prop.value not in self.properties[-1]:
            raise ParseError(
                f"Undefined property '{prop}' (line {tree.meta.line}, col {tree.meta.column})."
            )

        delta = self.visit(delta_tree)
        new_value = self.properties[-1][prop.value] + delta
        self.properties[-1][prop.value] = new_value

        return prop.value, new_value

    def def_var_absolute(self, tree: ParseTree) -> None:
        """
        Define or overwrite a variable.
        """
        var, arith_expr = tree.children
        value = self.visit(arith_expr)
        self.vars[var.value] = value

    def def_var_relative(self, tree: ParseTree) -> None:
        """
        Modify a variable by adding some delta to it.
        """
        var, arith_expr = tree.children
        value = self.visit(arith_expr)
        self.vars[var.value] += value

    def fill_expr(self, tree: ParseTree) -> tuple[str, tuple | int]:
        child_objs = self.visit_children(tree)
        if len(child_objs) == 1:
            return self.FILL_BACKWARD, child_objs[0]
        elif len(child_objs) == 2:
            fill_from_number, ident_to = child_objs
            return self.FILL_FORWARD, (fill_from_number, ident_to.value)
        else:
            raise NotImplementedError

    def binary_arith_expr(self, tree: ParseTree) -> int | float:
        operand_a, operator, operand_b = self.visit_children(tree)
        if operator == "+":
            return operand_a + operand_b
        elif operator == "-":
            return operand_a - operand_b
        else:
            raise NotImplementedError

    def unary_arith_expr(self, tree: ParseTree) -> int | float:
        sign, literal_tree = tree.children
        literal = self.visit(literal_tree)
        return literal * -1 if sign == "-" else literal

    def literal(self, tree: ParseTree) -> int | float:
        s = tree.children[0]
        try:
            return int(s)
        except ValueError:
            return float(s)

    def int_literal(self, tree: ParseTree) -> int:
        return int(tree.children[0])

    def var_ref(self, tree: ParseTree) -> int | float:
        """
        Look up the value of a variable, or, if unsuccessful, try to find an
        enum of the same name.
        """
        var = tree.children[0].value
        if var in self.vars:
            return self.vars[var]

        # look up variable name in enums if it cannot be found
        for enum_cls in self.enums:
            try:
                return enum_cls[var]
            except KeyError:
                continue
        raise ParseError(
            f"Unknown variable '{var}' (line {tree.meta.line}, col {tree.meta.column}). It is not defined in this file, and was not found in predefined enums."
        )

    def property_ref(self, tree: ParseTree) -> int | float:
        """
        Look up the value of a property from the current scope.
        """
        prop = tree.children[0].value
        try:
            return self.properties[-1][prop]
        except KeyError:
            raise ParseError(
                f"Undefined property '{prop}' (line {tree.meta.line}, col {tree.meta.column})"
            )

    def property_index_ref(self, tree: ParseTree) -> int | float:
        # TODO implement me
        raise NotImplementedError

    def include_expr(self, tree: ParseTree):
        # TODO implement me
        raise NotImplementedError

    @staticmethod
    def _aggregate_duplicate_dict_items(dict_items: list[tuple]) -> dict:
        """
        Collect 2-tuples of key, value in a dict. In case of duplicate keys,
        do not overwrite, but collect all values of that key in a list, in
        their order of appearance in `dict_items`.
        """
        # Collect properties in a dict.
        aggregated = {}
        for k, v in dict_items:
            if k not in aggregated:
                aggregated[k] = v
            elif type(aggregated[k]) is list:
                aggregated[k].append(v)
            else:
                aggregated[k] = [aggregated[k], v]
        return aggregated
