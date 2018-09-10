import tornado.web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from core import set_options

import ujson as json

options = set_options()


class MainHandler(tornado.web.Application):
    def get(self):
        response = {
            "error": 400,
            "message": "Bad Request"
            "data": None
        }
        self.write(json.dumps(response))
        self.finish()

def setup():
    return tornado.web.Application([
        (r"/", MainHandler)
    ])

def main():
    try:
        server = HTTPServer(setup(), xheaders=True)
        server.bind(options.port)
        server.start(options.workers)
        IOLoop.instance().start()
    except KeyboardInterrupt:
        print("Exiting cleanly")

if __name__ == "__main__":
    main()
