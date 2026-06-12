from .size_of import (strsize, numsize)
from .chraracter_binary import (initialize_characters, charbinary, letvalue)
from .letter_casing import (upper_case_words, alphabet)
from .general import (tick_loop, change_character)
from .binary_number import (convert_bit64_to_binary,  convert_binary_to_bit64)
from .sigment_method import (ESM_Sigment, OSM_Sigment)

def Length(words: str):
    return strsize(words)

def Numlength(number: float):
    return numsize(number)

def Fixiate_words(words: str):
    return initialize_characters(words)

def Get_charbinary():
    return charbinary

def Get_letvalue():
    return letvalue

def Upper_case(words: str):
    return upper_case_words(words)

def Get_alphabet():
    return alphabet

def Delay(second: int):
    tick_loop(seconds)

def Charto(word: str, target:str, value: str):
    return change_character(word, target, value)
    
def CNTB(number: int):
    return convert_bit64_to_binary(number)

def CBTN(binary: str):
    return convert_binary_to_bit64(binary)

def WSM(characters: str, invert: bool = False):
    size = strsize(characters)
    if size % 2 == 0:
        return ESM_Sigment(characters, invert)
    else:
        return OSM_Sigment(characters, invert)