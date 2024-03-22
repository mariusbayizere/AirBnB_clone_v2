#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives
"""
from fabric.api import task, env, cd, run
from pathlib import Path

env.hosts = ['3.84.239.91', '54.165.31.141']


@task
def do_clean(number=0):
    """
    Delete old archives, keeping the specified number of recent archives.

    Args:
        number (int, optional): The number of recent archives to keep,
            including the most recent.
            version. If 2 and so on.
    """
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
