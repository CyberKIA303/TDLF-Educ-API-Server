class letters:
    def uppercase(words: str):
        output: str = ""
        for let in words:
            num: int = ord(let)
            if num > 96 and num < 123:
                up: str = chr(num - 32)
                output += up
            else:
                output += let
        return output
    
    def lowercase(words: str):
        output: str = ""
        for let in words:
            num: int = ord(let)
            if num > 64 and num < 91:
                lo: str = chr(num + 32)
                output += lo
            else:
                output += let
        return output
    
    def camelcase(words: str):
        words = letters.lowercase(words)
        output: str = ""
        fl: bool = True
        for let in words:
            if fl:
                up: str = ""
                up += let
                up = letters.uppercase(up)
                output += up
                fl = False
            else:
                if let == ' ':
                    fl = True
                output += let
        return output