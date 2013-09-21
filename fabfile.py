#!/usr/bin/python
# -*- coding: utf-8 -*-


from fabric.api import local, put, sudo


def prepare():
    local('rm -rf _site')
    local('jekyll build')


def deploy():
    sudo('rm -rf /home/projects/_site')
    put('_site', '/home/projects/', use_sudo=True)
