import sqlite3
from data.data_context import DataContext
from model.base_user import BaseUser
from model.user import User


class UserRepository:

    def __init__(self, data_context: DataContext):
        self._dbmanager = data_context.get_db()
        self.data_context = data_context

        for i in self.get_users():
            print(i)

    # TODO - add supportive id for user
    def add_user(self, username, nickname, password, salt):
        self._dbmanager.add_record(table="Users", record={
                                   "id": 0, "name": username, "nickname": nickname, "password": password, "salt": salt})

    def get_user(self, username):
        return self._dbmanager.filter_records(
            table="Users", values={"name": username})

    # -------------------

    def get_users(self) -> list:

        try:
            db: sqlite3.Connection = sqlite3.connect()
            cursor = db.cursor()

            query = """SELECT name, nickname FROM Users"""

            cursor.execute(query)

            users = cursor.fetchall()
            base_users = []

            for user in users:
                base_user = self.map_base_user(user)
                base_users.append(base_user)

            return base_users

        except sqlite3.Error:
            pass

        # raw_users = self._dbmanager.get_all_records(
        #     table="Users", database=self.data_context.config["database_path"])

        # users = []

        # for raw_user in raw_users:
        #     user = self.map_user(raw_user)

        #     if user is not None:
        #         users.append(self.map_user(raw_user))

        # return users

    # ------------------

    def map_base_user(self, raw_user) -> BaseUser:
        try:
            base_user = BaseUser(raw_user.name,
                                 raw_user.nickname)

            return base_user
        except Exception as e:
            return None

    def map_user(self, raw_user) -> User:
        try:
            user = User(raw_user["username"],
                        raw_user["nickname"],
                        raw_user["password"],
                        raw_user["salt"])

            return user
        except:
            return None
