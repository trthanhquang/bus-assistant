import os
import logging
import datetime

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.gen

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

from getBusTiming import *

class TimeHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass
    
    def get(self):
        data = time.ctime(time.time())
        self.render("time.html", data=data)

class BusTimingHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass

    def get(self, stop_id = "16367"):
        stopStatus = getBusStopStatus(stop_id)
        self.render("index.html", 
            busStop = stop_id, 
            stopDescription= stopStatus.description,
            lastUpdateTime = datetime.datetime.now().strftime("%a %b %d %Y %H:%M:%S"),
            departureList=stopStatus.departureList)

class Application(tornado.web.Application):
    def __init__(self):

        handlers = [
            (r"/",BusTimingHandler),
            (r"/time", TimeHandler),
            (r"/stop/([0-9]+)",BusTimingHandler)
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
