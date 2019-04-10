#!/usr/bin/python3
import os
from fabric.api import *
from datetime import datetime
env.hosts = ['35.237.164.107', '35.243.176.56']


def do_deploy(archive_path):
    """distributes an archive to the webservers"""
    print('tio;')
    if os.path.exists(archive_path) is False:
        print(archive_path)
        return False
    try:
        print('try')
        upload = put(archive_path, "/tmp/")
        n = archive_path[20:-4]
        run("sudo mkdir -p /data/web_static/releases/web_static_{}/".format(n))
        run("sudo tar -xzf /tmp/web_static_{}.tgz -C "
            "/data/web_static/releases/web_static_{}".format(n, n))
        run("sudo rm /tmp/web_static_{}.tgz".format(n))
        run("sudo mv -f /data/web_static/releases/web_static_{}/web_static/* "
            "/data/web_static/releases/web_static_{}/".format(n, n))
        run("sudo rm -rf /data/web_static/releases/"
            "web_static{}/web_static".format(n))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/"
            "web_static_{}/ /data/web_static/current".format(n))
        return True
    except Exception as e:
        print("E is for everyone {}:", e)
        return False
