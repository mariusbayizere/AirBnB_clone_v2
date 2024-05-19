#!/usr/bin/python3
"""
<<<<<<< HEAD
Fabric script to delete out-of-date archives
"""
from fabric.api import task, env, cd, run
from pathlib import Path
=======
Fabric script to delete out-of-date archives using the do_clean function.
"""

import os
from fabric.api import *
>>>>>>> 18110df42e5ddd7c53ebecb3bb4c7360b8b49400

env.hosts = ['3.84.239.91', '54.165.31.141']


<<<<<<< HEAD
@task
=======
>>>>>>> 18110df42e5ddd7c53ebecb3bb4c7360b8b49400
def do_clean(number=0):
    """
    Delete old archives, keeping the specified number of recent archives.

    Args:
        number (int, optional): The number of recent archives to keep,
            including the most recent.
            version. If 2 and so on.
    """
<<<<<<< HEAD
    versions_dir = str(Path('/versions'))
    releases_dir = str(Path('/data/web_static/releases'))

    for host in env.hosts:
        # Delete old archives in /versions
        with cd(versions_dir.replace(' ', r'\ ')):  # Escape spaces in the path
            archives = sorted(Path().glob('web_static_*.tgz'), reverse=True)
            for archive in archives[number:]:
                run(f'rm {archive}')

        # Delete old archives in /data/web_static/releases
        with cd(releases_dir.replace(' ', r'\ ')):  # Escape spaces in the path
            archives = sorted(Path().glob('web_static_*.tgz'), reverse=True)
            for archive in archives[number:]:
                run(f'rm {archive}')
=======
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
>>>>>>> 18110df42e5ddd7c53ebecb3bb4c7360b8b49400
