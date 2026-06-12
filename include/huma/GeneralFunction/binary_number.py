def convert_bit64_to_binary(number: int):
    output: str = ""
    bival: int = 32
    while bival != 0:
        if number >= bival:
            output += "1"
        else:
            output += "0"
        if bival == 1:
            break
        if output[-1] == '1':
            number -= bival
        bival /= 2
    return output

def convert_binary_to_bit64(binary: str):
    output: int = 0
    aditive: int = 32
    for let in binary:
        if let == '1':
            output += aditive
        aditive /= 2
    return int(output)