from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# def verify_password(plain_paassword, hashed_password):
#     return pwd_context.verify(plain_paassword, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


# def authenticate_user(username: str, password: str):
#     user = [u for u in USERS if u["username"] == str(username)]
#     print(user)
#     if not user:
#         return False
#     if not verify_password(password, user[0]['password']):
#         return False
#     return user[0]
