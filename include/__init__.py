from .huma import (KamCyperFunction_SM, KamCyperFunction_CM, read_file_content)

def HumaCyper(data: str, status: str, complex: bool = False):
    if not complex:
        return KamCyperFunction_SM(data, status)
    else:
        return KamCyperFunction_CM(data, status)