import bcrypt


def hash_password(password: str):
    """метод шифрования пароля"""
    return bcrypt.checkpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf8")


def validate_password(password: str, hashed_password: str) -> bool:
    """
    Сверить хеш пароля с хешем из БД.
    """
    return bcrypt.checkpw(password.encode("utf8"), hashed_password.encode("utf8"))
