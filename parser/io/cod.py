import pathlib

import numpy as np


def read_cod(path: pathlib.Path) -> str:
    """
    Read a COD binary file and return its contents as a string.
    """
    with path.open("rb") as f:
        cod_bytes = f.read()
    cod_uint16 = np.frombuffer(cod_bytes, count=len(cod_bytes) // 2, dtype=np.uint16)
    cod_uint16_decode = 256 - cod_uint16
    cod_str = cod_uint16_decode.tobytes().decode("cp1252", errors="ignore")
    return cod_str
