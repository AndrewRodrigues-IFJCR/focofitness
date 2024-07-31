from pwdlib import PasswordHash

PasswordHandler = PasswordHash.recommended()


def generate_password_hash(password: str) -> str:
    return PasswordHandler.hash(password)


def verify_password(password_plain: str, password_hash: str) -> None:
    if not PasswordHandler.verify(password_plain, password_hash):
        raise Exception()
