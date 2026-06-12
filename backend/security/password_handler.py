from .. import incrypt

def hash_password(password: str):
    return incrypt(password, True)

def verify_password(plain_password: str, hashed_password: str):
    varify = incrypt(plain_password, True)
    if varify == hashed_password:
        return True
    else:
        return False
