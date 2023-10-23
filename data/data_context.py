import json
from ReallySimpleDB import dbmanager


class DataContext():
    def __init__(self):
        self._dbmanager = dbmanager()

        with open("lesson4/data/config.json", "r") as config_file:
            self.config = json.load(config_file)

        self._dbmanager.create_db(
            dbpath=self.config["database_path"], replace=not self.config["production"])

        self._dbmanager.add_columns(column_name="id",
                                    datatype="INTEGER", primary_key=True)

        self._dbmanager.add_columns(column_name="name", not_null=True)
        self._dbmanager.add_columns(column_name="nickname", not_null=True)
        self._dbmanager.add_columns(column_name="password", not_null=True)

        self._dbmanager.create_table(
            database=self.config["database_path"], table_name="Users")

    def get_db(self):
        return self._dbmanager
