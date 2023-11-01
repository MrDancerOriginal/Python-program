import bcrypt
import data.uow

uow = data.uow.UnitOfWork()


def hash(password):
    password += uow.config["secret_key"]
    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    return (hashed.decode('utf-8'), salt.decode('utf-8'))


def check(login_password, hashed_password):
    if hashed_password is None:
        return False

    return bcrypt.checkpw(
        login_password.encode('utf-8'), hashed_password.encode('utf-8')
    )


def register(name, nickname, password):
    password = hash(password)
    uow.user_repository.add_user(name, nickname, password[0], password[1])


def login(name, password: str):
    users = uow.user_repository.get_user(name)
    password += uow.config["secret_key"]
    
    for user in users:
        if user is not None:
            stored_salt: str = user["salt"]
            stored_hashed_password: str = user["password"]
            hashed_password = bcrypt.hashpw(
                password.encode('utf-8'), stored_salt.encode('utf-8')).decode('utf-8')

            if hashed_password == stored_hashed_password:
                print("Успішно!")
            else:
                print("Неправильний пароль")
        else:
            print("Користувача не знайдено")
