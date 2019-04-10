#!/usr/bin/python3
import os
from fabric.api import *
import tarfile
from datetime import datetime
env.hosts = ['35.237.164.107', '35.243.176.56']


def do_deploy(archive_path):
    """distributes an archive to the webservers"""
    if os.path.exists(archive_path) is False:
        return False
    upload = put(archive_path, "/tmp/")
    n = archive_path[20:-4]
    run ("mkdir -p /data/web_static/releases/web_static_{}/".format(n))
    run("tar -xzf /tmp/web_static_{}.tgz -C /data/web_static/releases/\
        web_static_{}".format(n, n))
    run("mv /data/web_static/releases/web_static_{}/web_static/* /data/\
        web_static/releases/web_static_{}/".format(n, n))
    run("rm -rf /data/web_static/releases/web_static{}/web_static".format(n))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/current, /data/web_static/releases/web_static\
        _{}.format(n)")
    return True
