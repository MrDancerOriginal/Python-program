from ReallySimpleDB import dbmanager
from data.data_context import DataContext


class UserRepository:

    def __init__(self, data_context: DataContext):
        self._dbmanager = data_context.get_db()
        self.data_context = data_context

    # TODO - add supportive id for user

    def add_user(self, username, nickname, password):
        self._dbmanager.add_record(table="Users", record={
                                   "id": 0, "name": username, "nickname": nickname, "password": password},
                                   database=self.data_context.config["database_path"])

    def get_user(self, username, password):
        self._dbmanager.filter_records(
            table="Users", record={"name": username, "password": password})

    def get_users(self):
        return self._dbmanager.get_all_records(table="Users", database=self.data_context.config["database_path"])
