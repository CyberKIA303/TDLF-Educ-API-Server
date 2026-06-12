from .bichar import (string_to_binary, binary_to_string)
from .numbi import (binary_to_number_string, numder_string_to_binary)
from .numchar import (number_string_to_characters, characters_to_number_string)
from .bibit64 import (binary_to_modified_bit64, modefied_bit64_to_binary)
from ..GeneralFunction import WSM

def Charbi(words: str):
    return string_to_binary(words)

def Bichar(binary: str):
    return binary_to_string(binary)

def Binum(binary: str):
    return binary_to_number_string(binary)

def Numbi(number_string: str):
    return numder_string_to_binary(number_string)

def Numchar(number_string: str):
    return number_string_to_characters(number_string)

def Charnum(characters: str):
    return characters_to_number_string(characters)

def Bimobit64(binary: str):
    return binary_to_modified_bit64(binary)

def Mobit64bi(characters: str):
    return modefied_bit64_to_binary(characters)

def incrypt(words: str, complex: bool = False):
    data: str = number_string_to_characters(binary_to_number_string(string_to_binary(words)))
    if not complex:
        return data
    else:
        modify: str = Bimobit64(string_to_binary(data))
        shuffle: str = WSM(modify)
        return WSM(number_string_to_characters(binary_to_number_string(string_to_binary(shuffle))), True)
        
def decrypt(words: str, complex: bool = False):
    if not complex:
        return binary_to_string(numder_string_to_binary(characters_to_number_string(words)))
    else:
        data: str = binary_to_string(numder_string_to_binary(characters_to_number_string(WSM(words))))
        shuffle: str = WSM(data, True)
        modify: str = binary_to_string(Mobit64bi(shuffle))
        return binary_to_string(numder_string_to_binary(characters_to_number_string(modify)))