from termcolor import colored

def robo_talk(str):
  print(colored('🤖: ' + str + '\n', 'green'))

def robo_question(str):
  return input(colored('🤖: ' + str + '\n', 'green'))

your_name = robo_question('I am roboko. Please tell me your name?')
favorite_restaurant = robo_question('What restaurant do you like?')
robo_talk('Thanks. Have a nice day.')