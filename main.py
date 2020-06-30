from termcolor import colored
import csv


def robo_talk(str):
    print(colored('🤖: ' + str + '\n', 'green'))


def robo_question(str):
    return input(colored('🤖: ' + str + '\n', 'green'))


your_name = robo_question('I am roboko. Please tell me your name?')
favorite_restaurant = robo_question(
    'Hi, ' + your_name + '. What restaurant do you like?')
with open('list.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': favorite_restaurant, 'Count': 1})
robo_talk('Thanks. Have a nice day.')
