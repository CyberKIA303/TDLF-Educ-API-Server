alphabet = [
    {"alpha": {"upper_case": "A", "lower_case": "a"}},
    {"alpha": {"upper_case": "B", "lower_case": "b"}},
    {"alpha": {"upper_case": "C", "lower_case": "c"}},
    {"alpha": {"upper_case": "D", "lower_case": "d"}},
    {"alpha": {"upper_case": "E", "lower_case": "e"}},
    {"alpha": {"upper_case": "F", "lower_case": "f"}},
    {"alpha": {"upper_case": "G", "lower_case": "g"}},
    {"alpha": {"upper_case": "H", "lower_case": "h"}},
    {"alpha": {"upper_case": "I", "lower_case": "i"}},
    {"alpha": {"upper_case": "J", "lower_case": "j"}},
    {"alpha": {"upper_case": "K", "lower_case": "k"}},
    {"alpha": {"upper_case": "L", "lower_case": "l"}},
    {"alpha": {"upper_case": "M", "lower_case": "m"}},
    {"alpha": {"upper_case": "N", "lower_case": "n"}},
    {"alpha": {"upper_case": "O", "lower_case": "o"}},
    {"alpha": {"upper_case": "P", "lower_case": "p"}},
    {"alpha": {"upper_case": "Q", "lower_case": "q"}},
    {"alpha": {"upper_case": "R", "lower_case": "r"}},
    {"alpha": {"upper_case": "S", "lower_case": "s"}},
    {"alpha": {"upper_case": "T", "lower_case": "t"}},
    {"alpha": {"upper_case": "U", "lower_case": "u"}},
    {"alpha": {"upper_case": "V", "lower_case": "v"}},
    {"alpha": {"upper_case": "W", "lower_case": "w"}},
    {"alpha": {"upper_case": "X", "lower_case": "x"}},
    {"alpha": {"upper_case": "Y", "lower_case": "y"}},
    {"alpha": {"upper_case": "Z", "lower_case": "z"}},
]

def upper_case_words(words: str):
    output: str = ""
    for index in words:
        found: bool = False
        for letters in alphabet:
            alpha = letters['alpha']
            if index == alpha['lower_case']:
                output += alpha['upper_case']
                found = True
                break
        if not found:
            output += index
    return output

def lower_case_words(words: str):
    output: str = ""
    for index in words:
        found: bool = False
        for letters in alphabet:
            alpha = letters['alpha']
            if index == alpha['upper_case']:
                output += alpha['lower_case']
                found = True
                break
        if not found:
            output += index
    return output