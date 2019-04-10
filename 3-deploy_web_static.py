#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['35.237.164.107', '35.243.176.56']


def do_deploy(archive_path):
    """distributes an archive to the webservers"""
    if os.path.exists(archive_path) is False:
        return False
    try:
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
    except:
        return False


def do_pack():
    """Fabric script that generates a .tgx archive"""
    n = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static".format(n))
    if result.failed:
        return None
    else:
        return "versions/web_static_{}.tgz".format(n)


def deploy():
    """creates and distributes an archive to your web servers, using deploy"""
    archive = do_pack()
    if archive is False:
        return False
    else:
        return do_deploy(archive)
