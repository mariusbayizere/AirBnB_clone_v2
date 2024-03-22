#!/usr/bin/python3
"""
Script that generates a tgz archive from the web_static folder contents.
"""
from datetime import datetime
from fabric.api import local
from os import path


def do_pack():
    """
    Generate a tgz archive from the web_static folder contents.

    Returns:
        The archive path if the archive has been correctly generated.
        None otherwise.
    """

    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        if not path.exists("versions"):
            local("mkdir versions")
        local("tar -cvzf {} web_static".format(file_name))
        archived_size = local("wc -c < {}".format(file_name), capture=True)
        print("web_static packed: {} -> {}Bytes".format(
            file_name, archived_size))
        return file_name
    except Exception:
        return None
