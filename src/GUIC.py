import sys, os, commands

if __name__ == '__main__':
    arguments = sys.argv[1:]

    try:
        if arguments[0] == 'project':
            os.mkdir(arguments[1])
            
            with open(f'{arguments[1]}/main.guic', 'w'):
                pass
            
            os.mkdir(f'{arguments[1]}/package')

        elif arguments[0] == 'execute':
            with open(arguments[1], 'r') as file:
                for line in file:
                    line = line.split()

                    str_command = f'commands.{line[0]}({line[1:]})'

                    exec(str_command)

        else:
            raise NameError('The command does not exists')

    except Exception as e:
        print(f'GUIC errror: {e}')