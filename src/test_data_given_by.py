"""
    This file check if the command create by the user can be use to execute this program
"""

import os

def command(arguments):
    if not len(arguments) > 0:
        return 'Command Error: None argument given'

    if not arguments[0] in ['project', 'execute']:
        return 'Command Error: Argument given unknown'

    if not len(arguments) > 1:
        return 'Command Error: None name given'

    if arguments[0] == 'execute':
        #TODO
    else:
        if os.path.isdir(arguments[1]):
            return 'Command Error: The folder already exists'

def file(name_file):
    return #TODO
