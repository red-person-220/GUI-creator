import sys, test_data_given_by, commands

if __name__ == '__main__':
    arguments = sys.argv[1:]

    test_data_given_by.command(arguments)

    if arguments[0] == 'project':
        commands.project(name=arguments[1])
    elif arguments[0] == 'package':
        commands.package(name_user=arguments[1], name_project=arguments[2], name_branch=arguments[3])

    elif arguments[0] == 'execute':
        test_data_given_by.file(name_file=arguments[1])
        commands.execute(arguments[1])