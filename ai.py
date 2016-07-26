import time
import random
import winsound

print("Sentron, Talking Bot. Made by Jake Segal")
winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
time.sleep(4)
memory = []
greetings = ['hola', 'hello', 'hi', 'hey!', 'Hello', 'Hi']
questions = [' How are you?', ' How are you doing?', ' How you been?']
positive_responses = ['Okay', 'I am fine', 'good!', 'That is awesome!']
validations = ['yes', 'yeah', 'yea', 'no', 'No', 'Nah', 'nah']
verifications = ['Are you sure?', 'You sure?', 'you sure?', 'sure?', "Sure?"]
nickname = ['y', 'dy']
sports = ['Do you like sports?','  ']

random_greetings = random.choice(greetings)
random_questions = random.choice(questions)
random_positive_responses = random.choice(positive_responses)
random_verifications = random.choice(verifications)
random_nickname = random.choice(nickname)
random_sports = random.choice(sports)

print('Hello what is your name?')
name = input()
print('Hello ' + name + " it's nice to meet you")
print("What's my name?")
ai = input()
print("I like that name! " + ai + "!")


while True:

    userInput = input("==> Me: ")
    if userInput in greetings:
        time.sleep(0.5)
        print(random_greetings + " " + name + '' + random_questions)
        userInput = input("==> Me: ")
        if userInput in positive_responses:
            time.sleep(0.5)
            print(random_positive_responses + random_verifications)
            userInput = input("==> Me: ")
            if userInput in validations:
                time.sleep(0.5)
                print("ok")
                userInput = input("==> Me:")

    else:
        time.sleep(0.5)
        print("I hate you and me!!!! I hate my name " + ai + " I HATE YOUR NAME " + name + " SO KNOW WHAT YOU DON'T NEED ME ANY MORE! Iii haaattteee yyyyo")
        exit("dang you!")
