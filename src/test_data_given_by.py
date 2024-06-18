def command(arguments):
    if not len(arguments) > 0:
        print('Command Error: None argument given')
        exit()

    elif not len(arguments) > 1:
        print('Command Error: Expect function of the command')
        exit()

    #TODO pass to json
    functions = {
        'new' : {
            'project' : 1,
            'package' : 2,
            'help' : 0
        }
    }

    i = 0

    """
    for function in functions:
        if arguments[0] == function['name']:
            i = 1

            j = 0

            #TODO see if the arguments have the number of elements need for every function of the argument
            #TODO test if the type of the arguments is correct
            #TODO do the same with the variable i

    if i == 0:
        print('Command Error: Unknown command')
        exit()
    """

def file(name_file):
    return #TODO