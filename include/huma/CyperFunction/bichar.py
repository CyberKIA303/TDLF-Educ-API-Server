from ..GeneralFunction import Get_charbinary
from ..GeneralFunction import Fixiate_words
from ..GeneralFunction import Length

charbinary = Get_charbinary()

def string_to_binary(words: str):
    output = ""
    fixiated_words = Fixiate_words(words)
    for letters in fixiated_words:
        for character in charbinary:
            charbi = character['charbi']
            size = Length(charbi['let'])
            if size == 1:
                if letters == charbi['let']:
                    output += charbi['dec']
                    break
            else:
                if letters == charbi['let'][0]:
                    output += charbi['dec']
    return output

def binary_to_string(binary: str):
    output = ""
    data = ""
    for index in binary:
        data += index
        size = Length(data)
        if size == 7:
            for character in charbinary:
                charbi = character['charbi']
                if data == charbi['dec']:
                    let = charbi['let']
                    let_size = Length(let)
                    if let_size == 1:
                        output += let
                    else:
                        output += let[0]
                    data = ""
                    break
    return output