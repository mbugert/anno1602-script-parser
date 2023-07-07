import pathlib
import unittest


class BaseTestCase(unittest.TestCase):
    _1602_KE_ROOT = pathlib.Path(
        "/home/mbugert/Documents/Drive/Personal/Stuff/anno/wipwip/1602ke_files"
    )

    @classmethod
    def setUpClass(cls) -> None:
        if not cls._1602_KE_ROOT.exists():
            raise FileNotFoundError(
                f"1602 KE files not found at '{cls._1602_KE_ROOT}'"
            )
