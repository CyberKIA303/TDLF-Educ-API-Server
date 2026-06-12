from ..GeneralFunction import Length

def binary_to_number_string(binary: str):
    output = ""
    initial = binary[0]
    current = '!'
    count = 0
    for index in binary:
        if current != index:
            current = index
            if count != 0:
                output += str(count)
            count = 1
        else:
            count += 1
    output += str(count)
    if initial == '1':
        output += initial
    else:
        term = int(output[0]) + 1
        output += str(term)
    return output

def numder_string_to_binary(number_string: str):
    output =""
    size = Length(number_string) - 1
    initial = number_string[-1]
    if initial != '1':
        initial = '0'
    index = 0
    while index != size:
        value = int(number_string[index])
        while value != 0:
            output += initial
            value -= 1
        if initial == '1':
            initial = '0'
        else:
            initial = '1'
        index += 1
    return output