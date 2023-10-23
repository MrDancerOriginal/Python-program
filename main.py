import bcrypt
import data.data_context
import data.user_repository

data_context = data.data_context.DataContext()
user_repository = data.user_repository.UserRepository(data_context)


def hash(password):
    password_bytes = bytes(password, "utf-8")

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed


def register(name, nickname, password):
    user_repository.add_user(name, nickname, hash(password))
