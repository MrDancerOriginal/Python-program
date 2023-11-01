import sqlite3
from data.data_context import DataContext
from model.blog import Blog


class BlogRepository():
    def __init__(self, data_context: DataContext):
        self._dbmanager = data_context.get_db()
        self.data_context = data_context

    def add_blog(self, name, description, user_id):
        self._dbmanager.add_record(table="Users", record={
                                   "id": 0,
                                   "user_id": user_id,
                                   "name": name,
                                   "description": description})

    def get_all_blogs(self, user_id):
        try:
            db: sqlite3.Connection = sqlite3.connect()
            cursor = db.cursor()

            query = ""f"SELECT * FROM Blogs WHERE user_id = {user_id}"""

            cursor.execute(query)

            raw_blogs = cursor.fetchall()
            blogs = []

            for raw_blog in raw_blogs:
                blog = self.map_base_user(raw_blog)
                blogs.append(blog)

            return blogs

        except sqlite3.Error:
            pass

    def map_base_user(self, raw_blog) -> Blog:
        try:
            blog = Blog(raw_blog.name,
                        raw_blog.description,
                        raw_blog.user_id)

            return blog
        except Exception as e:
            return None
