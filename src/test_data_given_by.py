"""
    This file check if the command create by the user can be use to execute this program
"""

import os, requests

def command(arguments):
    if not len(arguments) > 0:
        return 'Command Error: None argument given'

    if not arguments[0] in ['project', 'package']:
        return 'Command Error: Argument given unknown'

    if not len(arguments) > 1:
        return 'Command Error: None name given'

    if arguments[0] == 'package':
        if not len(arguments) == 3:
            return 'Command Error: There are not enough arguments. Example: GUIC packpage "name_user" "name_project" "name_branch"'

        #url = f"https://github.com/{arguments[1]}/{arguments[2]}/archive/{arguments[3]}.zip"
    
        if not os.path.isdir('package'):
            return 'Command Error: package folder do not find'
        
        if not os.path.isfile('package.json'):
            return 'Command Error: package.json do not find'
    else:
        if os.path.isdir(arguments[1]):
            return 'Command Error: The folder already exists'

def file(name_file):
    return #TODO