from core.baseapp import BaseApp
from view.view_book import *


class MainApp(BaseApp):
    def __init__(self):
        self.books = []

    def list_book(self):
        self.list_book()


if __name__ == "__main__":
    app = MainApp()
    app.run()
