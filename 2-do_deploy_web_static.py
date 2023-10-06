#!/usr/bin/python3
"""Generates a .tgz archive from the
contents of the web_static folder
Distributes an archive to a web server"""

from fabric.operations import local, run, put
from datetime import datetime
import os
from fabric.api import env
import re


env.hosts = ['35.190.176.186', '35.196.156.157']


def do_pack():
    """Function to compress files in an archive"""
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
