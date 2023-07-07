import enum
import pathlib
from importlib.resources import files, as_file
from typing import Optional, Any, Type

from lark import Lark, ParseTree

from parser.game.constants import (
    HAEUSER_COD,
    MAXPRODCNT,
    RADIUS_HQ,
    RADIUS_MARKT,
    Resource,
    InfrastructureLevel,
    BuildingKind,
    AudioSample,
    Ruins,
    Character,
    OreSize,
    AnimationType,
    FIGUREN_COD,
    NOOBJEKT,
    CharacterType,
    Formation,
    PROPERTY_NUM_ROTATIONS,
)
from parser.io.script.interpreter import ScriptInterpreter


class CodGadLoader:
    """
    Generic COD/GAD content loader.
    """

    def __init__(self):
        traversable = files("parser.io.script").joinpath("grammar.lark")
        with as_file(traversable) as lark_path, open(lark_path) as f:
            self.lark = Lark(f, propagate_positions=True, parser="lalr")

        external_vars = self._get_external_vars()
        enums = self._get_enums()
        self.interpreter = ScriptInterpreter(external_vars=external_vars, enums=enums)

    def accepts(self, path: pathlib.Path) -> bool:
        return path.suffix.lower() in (".cod", ".gad", ".inc")

    def _get_external_vars(self) -> Optional[dict[str, Any]]:
        return None

    def _get_enums(self) -> Optional[list[Type[enum.IntEnum]]]:
        return None

    def parse_interpret(self, file_content: str) -> Any:
        tree = self.parse(file_content)
        obj = self.interpreter.visit(tree)
        return self._post_process(obj)

    def parse(self, file_content: str) -> ParseTree:
        return self.lark.parse(file_content)

    def _post_process(self, obj: Any) -> Any:
        return obj


class HaeuserCodLoader(CodGadLoader):
    def accepts(self, path: pathlib.Path) -> bool:
        return path.name.lower() == HAEUSER_COD

    def _get_external_vars(self) -> Optional[dict[str, Any]]:
        return {
            MAXPRODCNT: -1,
            # TODO determine these radii
            RADIUS_HQ: -1,
            RADIUS_MARKT: -1,
        }

    def _get_enums(self) -> Optional[list[Type[enum.IntEnum]]]:
        return [
            Resource,
            InfrastructureLevel,
            BuildingKind,
            AudioSample,
            Ruins,
            Character,
            OreSize,
            AnimationType,
        ]


class FigurenCodLoader(CodGadLoader):
    def accepts(self, path: pathlib.Path) -> bool:
        return path.name.lower() == FIGUREN_COD

    def _get_external_vars(self) -> Optional[dict[str, Any]]:
        return {NOOBJEKT: -1}

    def _get_enums(self) -> Optional[list[Type[enum.IntEnum]]]:
        return [
            CharacterType,
            Character,
            Formation,
            AnimationType,
            AudioSample,
            Resource,
        ]

    def _post_process(self, obj: Any) -> Any:
        # Several "Rotate" properties in FIGUREN.COD are incorrect, we fix
        # those here:
        # - all ships have "Rotate: 1" which should be 8
        # - bow wave animations have "Rotate: 12" which should be 8
        # - flags have "Rotate: 8" which should be 1
        # - cannon effects have "Rotate: 16" which should be 8
        # - ship sinking effect has "Rotate: 36" which should be 8
        # - juggler has "Rotate: 8" which should be 4
        fixed_rotations_by_character = {
            8: [
                Character.HANDEL1,
                Character.HANDELD1,
                Character.HANDEL2,
                Character.HANDELD2,
                Character.KRIEG1,
                Character.KRIEGD1,
                Character.KRIEG2,
                Character.KRIEGD2,
                Character.HANDLER,
                Character.HANDLERD,
                Character.PIRAT,
                Character.PIRATD,
                Character.BUGH,
                Character.KANONSHOT1,
                Character.KANONSHOT2,
                Character.KANONSHOTTURM,
                Character.KANONSHOTTURM2,
                Character.UNTERGANG,
            ],
            4: [Character.GAUKLER1],
            1: [
                Character.FAHNE1,
                Character.FAHNE2,
                Character.FAHNE3,
                Character.FAHNE4,
                Character.FAHNEPIRAT,
                Character.FAHNEWEISS,
            ],
        }

        for fixed_rotation, characters in fixed_rotations_by_character.items():
            for character in characters:
                obj["FIGUR"][character][PROPERTY_NUM_ROTATIONS] = fixed_rotation
        return obj
