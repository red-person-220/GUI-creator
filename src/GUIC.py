import sys, new, test_data_given_by, execute

if __name__ == '__main__':
    arguments = sys.argv[1:]

    test_data_given_by.command(arguments)

    if arguments[0] == 'new':
        if arguments[1] == 'project':
            new.project(name=arguments[2])
        elif arguments[1] == 'package':
            new.package(name=arguments[2], url=arguments[3])
    elif arguments[0] == 'execute':
        test_data_given_by.file(name_file=arguments[1])
        execute.file(arguments[1])