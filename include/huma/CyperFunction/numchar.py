from ..GeneralFunction import Get_letvalue
from ..GeneralFunction import Length
from ..GeneralFunction import Upper_case
from ..GeneralFunction import Get_alphabet

letvalue = Get_letvalue()
alphabet = Get_alphabet()

def number_string_to_characters(number_string: str):
    output = ""
    value = ""
    for index in number_string:
        value += index
        size = Length(value)
        if size == 2:
            found = False
            for character in letvalue:
                letval = character['letval']
                if value == letval['val']:
                    output += letval['let']
                    found = True
                    break
            if not found:
                for let in value:
                    for character in letvalue:
                        letval = character['letval']
                        if let == letval['val']:
                            output += letval['let']
                            break
            value = ""
    if value != "":
        for let in value:
            for character in letvalue:
                letval = character['letval']
                if let == letval['val']:
                    output += letval['let']
                    break
    simplified_output = ""
    initial = '!'
    for index in output:
        if initial == index:
            simplified_output += Upper_case(initial)
            initial = '!'
        elif initial == '!':
            initial = index
        else:
            simplified_output += initial
            initial = index
    if initial != '!':
        simplified_output += initial
    return simplified_output

def characters_to_number_string(characters: str):
    unsimplified = ""
    for index in characters:
        found = False
        for letters in alphabet:
            alpha = letters['alpha']
            if index == alpha['upper_case']:
                unsimplified += alpha['lower_case']
                unsimplified += alpha['lower_case']
                found = True
                break
        if not found:
            unsimplified += index
    output = ""
    for index in unsimplified:
        for character in letvalue:
            letval = character['letval']
            if index == letval['let']:
                output += letval['val']
                break
    return output