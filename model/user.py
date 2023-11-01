from model.base_user import BaseUser


class User(BaseUser):
    def __init__(self, username, nickname, password, salt) -> None:
        BaseUser.__init__(self, username, nickname)
        self.password = password
        self.salt = salt
