import random
import string
import os


settings = {
    'lower': True,
    'upper': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 8
} # Initial settings


def clear_screen():
    """
        To not print the basic information of the system
    """
    os.system('clear')


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
            user_password_length = get_user_password_length(option, default)
            settings[option] = user_password_length


def ask_if_change_settings(settings):

    while True:
        user_answer = input('Do you want to change default settings? (enter: yes, y: yes, n: no)')
        if user_answer in ['y', 'n', '']:
            if user_answer in ['y', '']:
                print('-' * 5, 'Change Settings', '-' *5, sep='')
                get_settings_from_user(settings)
            break
        else:
            print('Invalid input. (chose from: y: yes, n: no, enter: yes).')
            print('Please try again.')


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

def ask_to_generator_another_password():

    while True:
        user_answer = input('Regenerate? (y: yes, n: no), enter: yes: ')
        if user_answer in ['y', 'n', '']:
            if user_answer == 'n':
                return False
            return True
        else:
            print('Invalid input. (chose from: y: yes, n: no, enter: yes).')
            print('Please try again.')


def password_generator_loop(settings):
    """
        Show the password inside the loop
    """
    while True:
        print('-' * 40)
        print(f'Your Generator Password: {password_generator(settings)}')

        if ask_to_generator_another_password() == False:
            break


def run():
    """
        This function is responsible for executing the entire program   
    """
    clear_screen()
    ask_if_change_settings(settings)
    password_generator_loop(settings)
    print('Thank you for choosing us.')



run()