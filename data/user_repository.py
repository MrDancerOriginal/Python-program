from data.data_context import DataContext
from model.user import User


class UserRepository:

    def __init__(self, data_context: DataContext):
        self._dbmanager = data_context.get_db()
        self.data_context = data_context

        for i in self.get_users():
            print(i)
    # TODO - add supportive id for user

    def add_user(self, username, nickname, password):
        self._dbmanager.add_record(table="Users", record={
                                   "id": 0, "name": username, "nickname": nickname, "password": password})

    def get_user(self, username, password):
        self._dbmanager.filter_records(
            table="Users", record={"name": username, "password": password})

    # -------------------

    def get_users(self) -> list:
        raw_users = self._dbmanager.get_all_records(
            table="Users", database=self.data_context.config["database_path"])

        users = []

        for raw_user in raw_users:
            users.append(self.map_user(raw_user))

        return users

    # ------------------

    def map_user(self, raw_user) -> User:
        try:
            user = User(raw_user["username"],
                        raw_user["nickname"], raw_user["password"])

            return user
        except:
            pass
