import random
import string


settings = {
    'lower': True,
    'upper': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 8
} # Initial settings


def get_user_password_length(option, default, pw_min_length=4, pw_max_length=30):
    while True:
        user_input = input('Enter password length.'
                           f'(Default is {default}) (enter: default): ')
        if user_input == '':
            return default
        
        if user_input.isdigit():
            user_password_length = int(user_input)
            if pw_min_length <= user_password_length < pw_max_length:
                return int(user_input)
            print('Invalid input')
            print('Password length should be between'
                  f'{pw_min_length} and {pw_max_length}')
        else:
            print('Invalid input. You should enter a number.')
        
        print('Please try again. ')

def get_yes_or_no_for_settings(option, default):
    """
        In this function, we take the initial settings from the user
    """
    while True:
        user_input = input(f'Include {option}? (Default is {default})'
                           '(y: yes, n: no, enter: default):')
        if user_input == '':
            return default
            """
                By pressing the button enter the default value remains
            """
        
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print('Invalid input. Please try again')
        """
            By pressing the button 'y' True value and 
            by pressing the button 'n' False value
        """

def get_settings_from_user(settings):
    """
        This function executes the function of 
        receiving settings from the user and 
        changes the settings if necessary
    """
    for option, default in settings.items():
        if option != 'length':
            user_choice = get_yes_or_no_for_settings(option, default)
            settings[option] = user_choice
        else:
            user_password_linght = get_user_password_length(option, default)
            settings[option] = user_password_linght


def generate_random_char(choices):
    choice = random.choice(choices)

    if choice == 'upper':
        return random.choice(string.ascii_uppercase)
    if choice == 'lower':
        return random.choice(string.ascii_lowercase)
    if choice == 'symbol':
        return random.choice(""" !"#$%&'()*+,-./:;<=>?@[\]^_{|}~ """)
    if choice == 'number':
        return random.choice('0123456789')
    if choice == 'space':
        return ' '


def password_generator(settings):
    """
        This function creates a random password 
        based on the settings entered by the user
    """
    final_password = ''
    password_length = settings['length']

    choices = list(filter(lambda x: settings[x], ['lower', 'upper', 'symbol', 'number', 'space']))
    """ In this section, a list of True settings is returned """
    
    for i in range(password_length):
        final_password += generate_random_char(choices)
    return final_password

get_settings_from_user(settings)
# print(settings)
print(password_generator(settings))