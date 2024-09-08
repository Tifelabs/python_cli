from commands import cmds 
import datetime
from logo import art


# Prompt to enter username:
user_name = input('Enter username: ')

# Ensure the username is in lowercase
if user_name != user_name.lower():
    print('small text only !!!')
else:
    # Print the Welcome Message
    print(">>👾WELCOME TO PYTHON CLI👾<<")
    print('=================================')
    print('= Enter --help to show commands =')
    print('=================================')

    # Terminal prompt function
    def terminal():
        return input(f'{user_name}: ').strip()  # Input prompt with the username, removing extra spaces

    # Help command to show available commands
    def show_help():
        for cmd, desc in cmds.items():
            print(f"{cmd}: {desc}")

    #The neofetch command will show the python Ascii
    def neofetch():
        print(art)

    #The time command will show the current time and date 
    def time():
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))

    # Run terminal commands
    while True:
        command = terminal()
        if command == '--help':
            show_help()

        if command == 'neofetch':
            neofetch()

        if command == 'time':
            time()
        elif command == 'exit':  # Allowing user to exit the loop
            print('Exiting the CLI. Goodbye!')
            break
        else:
            print(f"Command '{command}' not recognized. Enter --help to show available commands.")


