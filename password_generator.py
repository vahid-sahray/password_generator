
settings = {
    'lower': True,
    'upper': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 8
} # Initial settings


def get_settings_from_user(settings):
    for option, default in settings.items():
        if option != 'length':
            while True:
                user_input = input(f'Include {option}? (Default is {default}) (y: yes, n: no):')
                if user_input == 'y' or user_input == 'n':
                    if user_input == 'y':
                        settings[option] = True
                    else:
                        settings[option] = False
                    break
                else:
                    print('Invalid input. Please try again')





get_settings_from_user(settings)
print(settings)