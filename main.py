import bcrypt
import data.data_context
import data.user_repository

data_context = data.data_context.DataContext()
user_repository = data.user_repository.UserRepository(data_context)


def hash(password) -> str:
    password = password+data_context.config["secret_key"]
    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed.decode('utf-8')


def check(login_password, hashed_password):
    if hashed_password is None:
        return False

    return bcrypt.checkpw(
        login_password.encode('utf-8'), hashed_password.encode('utf-8')
    )


def register(name, nickname, password):
    user_repository.add_user(name, nickname, hash(password))


def login(name, password):
    for user in user_repository.get_users():
        if check(password+data_context.config["secret_key"],
                 hash(user["password"])) and user["name"] == name:
            print("Знайдено")
