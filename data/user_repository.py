class UserRepository:

    def __init__(self, data_context):
        self._dbmanager = data_context.get_db()

    def add_user(self, username, nickname, password):
        self._dbmanager.add_record(table="Users", record={
                                   "id": 0, "name": username, "nickname": nickname, "password": password})
