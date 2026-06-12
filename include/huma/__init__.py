from .LicenceFolder import read_file_content
from .CyperFunction import (incrypt, decrypt)
from .GeneralFunction import Delay

def KamCyperFunction_SM(word: str, status: str):
    if status == "INCRYPT":
        return incrypt(word)
    elif status == "DECRYPT":
        return decrypt(word)
    else:
        return "Invalid Status!"
    
def KamCyperFunction_CM(word: str, status: str):
    if status == "INCRYPT":
        return incrypt(word, True)
    elif status == "DECRYPT":
        return decrypt(word, True)
    else:
        return "Invalid Status!"