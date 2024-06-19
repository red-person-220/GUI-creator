import os, requests

def command(arguments):
    if not len(arguments) > 0:
        print('Command Error: None argument given')
        exit()

    if not arguments[0] in ['project', 'packpage']:
        print('Command Error: Argument given unknown')
        exit()

    if not len(arguments) > 1:
        print(f'Command Error: None function given for the argument "{arguments[0]}"')
        exit()
    
    if not len(arguments) > 2:
        print(f'Command Error: None name given for the function "{arguments[1]}"')
        exit()

    if arguments[0] == 'package':
        if not len(arguments) == 4:
            print('Command Error: There are not enough arguments. Example: GUIC new packpage "name_user" "name_project" "name_branch"')
            exit()

        url = f"https://github.com/{arguments[2]}/{arguments[3]}/archive/{arguments[4]}.zip"

        try:
            response = requests.head(url)

            if response.status_code == 200:
                pass
            else:
                print('Command Error: Url make by the data you give dont find. Example: GUIC new packpage "name_user" "name_project" "name_branch"')
                exit()
        except requests.ConnectionError:
            print('Command Error: Url make by the data you give dont find. Example: GUIC packpage "name_user" "name_project" "name_branch"')
            exit()
    else:
        if os.path.isdir(arguments[2]):
            print('Command Error: The folder already exists')
            exit()

def file(name_file):
    return #TODO