from passlib.context import CryptContext

bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def createHash(password: str):
    return bcrypt.hash(password)

def compareHash(plainPassword: str, hashedPassword: str):
    return bcrypt.verify(plainPassword, hashedPassword)