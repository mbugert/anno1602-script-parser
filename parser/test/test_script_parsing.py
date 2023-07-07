from pprint import pformat

from parser.game.constants import HAEUSER_COD, FIGUREN_COD
from parser.io.cod import read_cod
from parser.io.script.loader import (
    CodGadLoader,
    HaeuserCodLoader,
    FigurenCodLoader,
)
from parser.test.base import BaseTestCase


class TestScriptParsing(BaseTestCase):
    """
    Confirm successful parsing of 1602 script files with the grammar-based
    parser.
    """

    def test_interpret_haeuser_cod(self):
        cod_path = self._1602_KE_ROOT / HAEUSER_COD
        self.assertTrue(cod_path.exists())

        loader = HaeuserCodLoader()
        self.assertTrue(loader.accepts(cod_path))
        script = read_cod(cod_path)
        obj = loader.parse_interpret(script)

        # there should be at least some output
        self.assertTrue(bool(obj))

        print("\n" + HAEUSER_COD + ":\n\n" + pformat(obj)[:500] + "...")

    def test_interpret_figuren_cod(self):
        cod_path = self._1602_KE_ROOT / FIGUREN_COD
        self.assertTrue(cod_path.exists())

        loader = FigurenCodLoader()
        self.assertTrue(loader.accepts(cod_path))
        script = read_cod(cod_path)
        obj = loader.parse_interpret(script)

        # there should be at least some output
        self.assertTrue(bool(obj))

        print("\n" + FIGUREN_COD + ":\n\n" + pformat(obj)[:500] + "...")

    def test_parse_gad_scripts(self):
        for subdir in ("Gaddata", "Gadedit"):
            for path in (self._1602_KE_ROOT / subdir).iterdir():
                with self.subTest("GAD file", path=path):
                    with path.open(encoding="cp1252") as f:
                        script = f.read()
                    loader = CodGadLoader()
                    self.assertTrue(loader.accepts(path))
                    tree = loader.parse(script)
                    self.assertTrue(bool(tree))
