from .size_of import strsize

charbinary = [
    {"charbi": {"let": " ", "dec": "0100000"}},
    {"charbi": {"let": "!", "dec": "0100001"}},
    {"charbi": {"let": '"', "dec": "0100010"}},
    {"charbi": {"let": "#", "dec": "0100011"}},
    {"charbi": {"let": "$", "dec": "0100100"}},
    {"charbi": {"let": "%", "dec": "0100101"}},
    {"charbi": {"let": "&", "dec": "0100110"}},
    {"charbi": {"let": "'", "dec": "0100111"}},
    {"charbi": {"let": "(", "dec": "0101000"}},
    {"charbi": {"let": ")", "dec": "0101001"}},
    {"charbi": {"let": "*", "dec": "0101010"}},
    {"charbi": {"let": "+", "dec": "0101011"}},
    {"charbi": {"let": ",", "dec": "0101100"}},
    {"charbi": {"let": "-", "dec": "0101101"}},
    {"charbi": {"let": ".", "dec": "0101110"}},
    {"charbi": {"let": "/", "dec": "0101111"}},
    {"charbi": {"let": "0", "dec": "0110000"}},
    {"charbi": {"let": "1", "dec": "0110001"}},
    {"charbi": {"let": "2", "dec": "0110010"}},
    {"charbi": {"let": "3", "dec": "0110011"}},
    {"charbi": {"let": "4", "dec": "0110100"}},
    {"charbi": {"let": "5", "dec": "0110101"}},
    {"charbi": {"let": "6", "dec": "0110110"}},
    {"charbi": {"let": "7", "dec": "0110111"}},
    {"charbi": {"let": "8", "dec": "0111000"}},
    {"charbi": {"let": "9", "dec": "0111001"}},
    {"charbi": {"let": ":", "dec": "0111010"}},
    {"charbi": {"let": ";", "dec": "0111011"}},
    {"charbi": {"let": "<", "dec": "0111100"}},
    {"charbi": {"let": "=", "dec": "0111101"}},
    {"charbi": {"let": ">", "dec": "0111110"}},
    {"charbi": {"let": "?", "dec": "0111111"}},
    {"charbi": {"let": "@", "dec": "1000000"}},
    {"charbi": {"let": "A", "dec": "1000001"}},
    {"charbi": {"let": "B", "dec": "1000010"}},
    {"charbi": {"let": "C", "dec": "1000011"}},
    {"charbi": {"let": "D", "dec": "1000100"}},
    {"charbi": {"let": "E", "dec": "1000101"}},
    {"charbi": {"let": "F", "dec": "1000110"}},
    {"charbi": {"let": "G", "dec": "1000111"}},
    {"charbi": {"let": "H", "dec": "1001000"}},
    {"charbi": {"let": "I", "dec": "1001001"}},
    {"charbi": {"let": "J", "dec": "1001010"}},
    {"charbi": {"let": "K", "dec": "1001011"}},
    {"charbi": {"let": "L", "dec": "1001100"}},
    {"charbi": {"let": "M", "dec": "1001101"}},
    {"charbi": {"let": "N", "dec": "1001110"}},
    {"charbi": {"let": "O", "dec": "1001111"}},
    {"charbi": {"let": "P", "dec": "1010000"}},
    {"charbi": {"let": "Q", "dec": "1010001"}},
    {"charbi": {"let": "R", "dec": "1010010"}},
    {"charbi": {"let": "S", "dec": "1010011"}},
    {"charbi": {"let": "T", "dec": "1010100"}},
    {"charbi": {"let": "U", "dec": "1010101"}},
    {"charbi": {"let": "V", "dec": "1010110"}},
    {"charbi": {"let": "W", "dec": "1010111"}},
    {"charbi": {"let": "X", "dec": "1011000"}},
    {"charbi": {"let": "Y", "dec": "1011001"}},
    {"charbi": {"let": "Z", "dec": "1011010"}},
    {"charbi": {"let": "[", "dec": "1011011"}},
    {"charbi": {"let": "\\","dec": "1011100"}},
    {"charbi": {"let": "]", "dec": "1011101"}},
    {"charbi": {"let": "^", "dec": "1011110"}},
    {"charbi": {"let": "_", "dec": "1011111"}},
    {"charbi": {"let": "`", "dec": "1100000"}},
    {"charbi": {"let": "a", "dec": "1100001"}},
    {"charbi": {"let": "b", "dec": "1100010"}},
    {"charbi": {"let": "c", "dec": "1100011"}},
    {"charbi": {"let": "d", "dec": "1100100"}},
    {"charbi": {"let": "e", "dec": "1100101"}},
    {"charbi": {"let": "f", "dec": "1100110"}},
    {"charbi": {"let": "g", "dec": "1100111"}},
    {"charbi": {"let": "h", "dec": "1101000"}},
    {"charbi": {"let": "i", "dec": "1101001"}},
    {"charbi": {"let": "j", "dec": "1101010"}},
    {"charbi": {"let": "k", "dec": "1101011"}},
    {"charbi": {"let": "l", "dec": "1101100"}},
    {"charbi": {"let": "m", "dec": "1101101"}},
    {"charbi": {"let": "n", "dec": "1101110"}},
    {"charbi": {"let": "o", "dec": "1101111"}},
    {"charbi": {"let": "p", "dec": "1110000"}},
    {"charbi": {"let": "q", "dec": "1110001"}},
    {"charbi": {"let": "r", "dec": "1110010"}},
    {"charbi": {"let": "s", "dec": "1110011"}},
    {"charbi": {"let": "t", "dec": "1110100"}},
    {"charbi": {"let": "u", "dec": "1110101"}},
    {"charbi": {"let": "v", "dec": "1110110"}},
    {"charbi": {"let": "w", "dec": "1110111"}},
    {"charbi": {"let": "x", "dec": "1111000"}},
    {"charbi": {"let": "y", "dec": "1111001"}},
    {"charbi": {"let": "z", "dec": "1111010"}},
    {"charbi": {"let": "{", "dec": "1111011"}},
    {"charbi": {"let": "|", "dec": "1111100"}},
    {"charbi": {"let": "}", "dec": "1111101"}},
    {"charbi": {"let": "~", "dec": "1111110"}},
]

letvalue = [
    {"letval": {"let":  "a", "val": "1"}},
    {"letval": {"let":  "b", "val": "2"}},
    {"letval": {"let":  "c", "val": "3"}},
    {"letval": {"let":  "d", "val": "4"}},
    {"letval": {"let":  "e", "val": "5"}},
    {"letval": {"let":  "f", "val": "6"}},
    {"letval": {"let":  "g", "val": "7"}},
    {"letval": {"let":  "h", "val": "8"}},
    {"letval": {"let":  "i", "val": "9"}},
    {"letval": {"let":  "j", "val":"10"}},
    {"letval": {"let":  "k", "val":"11"}},
    {"letval": {"let":  "l", "val":"12"}},
    {"letval": {"let":  "m", "val":"13"}},
    {"letval": {"let":  "n", "val":"14"}},
    {"letval": {"let":  "o", "val":"15"}},
    {"letval": {"let":  "p", "val":"16"}},
    {"letval": {"let":  "q", "val":"17"}},
    {"letval": {"let":  "r", "val":"18"}},
    {"letval": {"let":  "s", "val":"19"}},
    {"letval": {"let":  "t", "val":"20"}},
    {"letval": {"let":  "u", "val":"21"}},
    {"letval": {"let":  "v", "val":"22"}},
    {"letval": {"let":  "w", "val":"23"}},
    {"letval": {"let":  "x", "val":"24"}},
    {"letval": {"let":  "y", "val":"25"}},
    {"letval": {"let":  "z", "val":"26"}},
]

# def characer_to_binary(words: str):
#     output = ""
#     size = strsize(words)
#     term = 0
#     while(term < size):
#         let = words[term]
        
#         num: int = let
#         print(num)
#         bit: int = 64
#         while(bit > 1):
#             if num > bit:
#                 output += "1"
#                 num -= bit
#             else:
#                 output += "0"
#             bit /= 2
#     return output

def initialize_characters(words: str):
    output: str = ""
    for letter in words:
        found: bool = False
        for character in charbinary:
            charbi = character['charbi']
            size = strsize(charbi['let'])
            if size == 1:
                if letter == charbi['let']:
                    output += letter
                    found = True
                    break
            else:
                if letter == charbi['let'][0]:
                    output += letter
                    found = True
                    break
        if not found:
            output += "?"
    return output
