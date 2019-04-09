#!/usr/bin/python3


def do_deploy(archive_path):
    """distributes an archive to the webservers"""
    #return false if archive path does not exist
    #upload archive to tmp directory
    #uncompress the archive to a folder on the web server
    #delete archive from web server
    #delete symbolic link
    #create a new symbolic link on the webserver linked to the new version of the code