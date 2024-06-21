"""
    This file have all the commands that the user can use in the console
"""

import os, git

def project(name):
    os.mkdir(name)

    with open(f'{name}/package.json', 'w'):
        pass

    with open(f'{name}/main.guic', 'w'):
        pass

    os.mkdir(f'{name}/package')

def package(name_user, name_project):
    return #TODO pensar como hacer para que funcione

def execute(name_file):
    return #TODO