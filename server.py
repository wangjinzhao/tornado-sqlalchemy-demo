# -*- coding: utf-8 -*-
from tornado.web import Application
from handlers.UserHandler import UserHandler
from tornado.ioloop import IOLoop



class App(Application):
    def __init__(self):
        handlers = [
            (r"/api/user(/(.)*)?", UserHandler),
        ]

        Application.__init__(self, handlers)
        # self.session = manager.session


if __name__ == "__main__":
    application = App();
    application.listen(8888)
    IOLoop.instance().start()
