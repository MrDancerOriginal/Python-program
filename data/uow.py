from data.blog_repository import BlogRepository
from data.data_context import DataContext
from data.user_repository import UserRepository


class UnitOfWork():

    data_context = DataContext()
    user_repository = UserRepository(data_context)
    blog_repository = BlogRepository(data_context)

    config = data_context.config

    def __init__(self) -> None:
        pass
