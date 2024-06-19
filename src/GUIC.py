#TODO see why no working

import sys, new, test_data_given_by, execute

if __name__ == '__main__':
    arguments = sys.argv[1:]

    test_data_given_by.command(arguments)

    if arguments[0] == 'project':
        new.project(name=arguments[2])
    elif arguments[0] == 'package':
        new.package(name_user=arguments[2], name_project=arguments[3], name_branch=arguments[4])

    elif arguments[0] == 'execute':
        test_data_given_by.file(name_file=arguments[1])
        execute.file(arguments[1])