import sys, new, test_data_given_by

if __name__ == '__main__':
    arguments = sys.argv[1:]

    test_data_given_by.command(arguments)

    if arguments[0] == 'new':
        # Quitar la funcion main y hacerlo directamente aqui chuparla
        new.main(arguments=arguments[1:])
    elif arguments[0] == 'execute':
        pass #TODO