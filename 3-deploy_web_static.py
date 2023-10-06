#!/usr/bin/python3
"""
do_pack(): Generates a .tgz archive from the
contents of the web_static folder
do_deploy(): Distributes an archive to a web server
deploy (): Creates and distributes an archive to a web server
"""

from fabric.operations import local, run, put
from datetime import datetime
import os
from fabric.api import env
import re


env.hosts = ['35.190.176.186', '35.196.156.157']


def do_pack():
    """Function to compress files in an archive"""
