from .. import HumaCyper

def hash_password(password: str):
    return HumaCyper(password, "INCRYPT", complex=True)

def verify_password(plain_password: str, hashed_password: str):
    varify = HumaCyper(plain_password, "INCRYPT", complex=True)
    if varify == hashed_password:
        return True
    else:
        return False
