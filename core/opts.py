# core/opts.py
"""
This file defines all the command line stdin used in this webserver
"""

from tornado.options import define, options, parse_command_line

def set_options():
    # Define the port number on the command line
    define("port", default=8000, help="Run this HTTP server on the given port", type=int)

    # Define the type of environment to use. Default is dev
    define("env", default="dev", help="Run an environment on this server given the environment code. Possible values are: dev, stage, prod", type=str)

    # Define the number of workers to be spawned during runtime. Default is 1 and max should be number of cores * 2.
    define("workers", default=1, help="Spawn number of workers. Min: 0, Max: <number of cores * 2>", type=int)

    parse_command_line()
    return options
