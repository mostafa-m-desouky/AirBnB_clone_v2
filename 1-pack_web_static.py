#!/usr/bin/python3
<<<<<<< HEAD
"""Generates a .tgz archive from the
contents of the web_static folder"""

from fabric.operations import local
from datetime import datetime


def do_pack():
    """Function to compress files"""
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if result.failed:
        return None
    return result
=======
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
>>>>>>> 1b70cc0e0b6b7b31e61bd1ab79d9d99cfcfb1c46
