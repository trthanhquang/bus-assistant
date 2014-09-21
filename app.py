import os
import logging
import time

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.gen

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

class busTime:
    def __init__(self,busCode,busTime):
        self.busCode = busCode #String
        self.busTime = busTime #List of String
    
    def __str__(self):
        return self.busCode

class TimeHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass
    
    def get(self):
        data = time.ctime(time.time())
        self.render("time.html", data=data)

class BusTimingHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass

    def get(self, bus_id = "16367"):
        busses = []
        if (bus_id == "16367"):
            busses = [
                busTime('8AX',['2','10']), 
                busTime('8X',['1','10','30']),
                busTime('9',['2','18','47']),
            ]
        self.render("index.html", busStop = bus_id, busses=busses)

class Application(tornado.web.Application):
    def __init__(self):

        handlers = [
            (r"/",BusTimingHandler),
            (r"/time", TimeHandler),
            (r"/bus/([0-9]+)",BusTimingHandler)
        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__),"static"),
        )
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
