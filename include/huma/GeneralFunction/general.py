from datetime import datetime

def tick_loop(seconds: int):
    hr: int = 0
    mt: int = 0
    sd: int = 0
    ml: int = 0
    while hr < seconds:
        while mt < 60:
            while sd < 60:
                while ml < 10000:
                    ml += 1
                ml = 0
                sd += 1
            sd = 0
            mt += 1
        mt = 0
        hr += 1
        
def change_character(word: str, target: str, value: str):
    output: str = ""
    for let in word:
        if let == target:
            output += value
        else:
            output += let
    return output