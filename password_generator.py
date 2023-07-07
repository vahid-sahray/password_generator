
settings = {
    'lower': True,
    'upper': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 8
} # Initial settings


def get_yes_or_no_for_settings(option, default):

    while True:
        user_input = input(f'Include {option}? (Default is {default}) (y: yes, n: no):')
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print('Invalid input. Please try again')


def get_settings_from_user(settings):
    for option, default in settings.items():
        if option != 'length':
            get_yes_or_no_for_settings(option, default)





get_settings_from_user(settings)
print(settings)