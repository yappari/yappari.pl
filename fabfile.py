#!/usr/bin/python
# -*- coding: utf-8 -*-


from fabric.api import local, put, sudo


def prepare():
    """..."""
    #
    local('rm -rf _site')
    local('jekyll build')

    #
    local('rm _site/README.md')
    local('rm _site/fabfile.py')
    local('rm _site/fabfile.pyc')


def deploy():
    """..."""
    #
    prepare()

    #
    sudo('rm -rf /home/projects/_site')
    put('_site', '/home/projects/', use_sudo=True)
