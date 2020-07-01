from termcolor import colored
import csv
import os


def robo_talk(str):
    print(colored('🤖: ' + str + '\n', 'green'))


def robo_question(str):
    return input(colored('🤖: ' + str + '\n', 'green'))


csv_file = 'list.csv'

your_name = robo_question('I am roboko. Please tell me your name?')

if os.path.exists(csv_file):
    dict = {}
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        next(file)
        for row in reader:
            dict[row[0]] = int(row[1])
        print(dict)
else:
    favorite_restaurant = robo_question(
        'Hi, ' + your_name + '. What restaurant do you like?')
    favorite_restaurant = favorite_restaurant.title()
    with open(csv_file, 'w') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Name': favorite_restaurant, 'Count': 1})
    robo_talk('Thanks. Have a nice day.')
