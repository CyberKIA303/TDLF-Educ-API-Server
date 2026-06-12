def strsize(words: str):
    output: int = 0
    for leters in words:
        output += 1
    return output

def numsize(number: float):
    convert: str = str(number)
    return strsize(convert)