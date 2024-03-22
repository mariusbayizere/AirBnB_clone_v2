#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives using the do_clean function.
"""

import os
from fabric.api import *

env.hosts = ['3.84.239.91', '54.165.31.141']


def do_clean(number=0):
    """
    Delete old archives, keeping the specified number of recent archives.

    Args:
        number (int, optional): The number of recent archives to keep,
            including the most recent.
            version. If 2 and so on.
    """
    number = 1 if int(number) == 0 else int(number)

    delete_arch = sorted(os.listdir("versions"))
    [delete_arch.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in delete_arch]

    with cd("/data/web_static/releases"):
        delete_arch = run("ls -tr").split()
        delete_arch = [a for a in delete_arch if "web_static_" in a]
        [delete_arch.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in delete_arch]
