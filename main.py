# main.py

"""
@author: Mimoy
@file: main.py
@title: Main
@description:
    This is the main logic if the HTTP Server. This basically contains and should
    only contain the following:

    a. Configuration instances
    b. HTTPServer instance
    c. Master route definition
    d. CLI command parser
    e. Database connection
"""
import tornado.web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from core.opts import set_options
from core.config import load

import ujson as json

from pprint import pprint

# Parse command line options
options = set_options()

# Load configurations from an environment yaml
config = load(options.env)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        response = {
            "error": 400,
            "message": "Bad Request",
            "data": None
        }
        self.write(json.dumps(response))
        self.finish()

def setup():
    """
    Main setup method for loading the master
    route configuration
    """
    return tornado.web.Application([
        (r"/", MainHandler)
    ],**config['system_settings'])


def main():
    """
    HTTP Server runtime logic
    """
    try:
        server = HTTPServer(setup(), xheaders=True)
        server.bind(options.port)
        server.start(options.workers)
        IOLoop.instance().start()
    except KeyboardInterrupt:
        # Exit the application cleanly on keyboard interrupt
        print("Exiting cleanly")
    except e:
        # Stdout any traceback thrown upon running this server
        print("Error occurred", e)

# Main start point
if __name__ == "__main__":
    main()
