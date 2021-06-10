def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    else:
        return 'green'

print(update_light('yellow'))

def apple(x):
    if x ** 2 >= 1000:
        return "It's hotter than the sun!!"
    else:
        return "Help yourself to a honeycomb Yorkie for the glovebox."

print(apple(45))

def sp_eng(sentence):
    sentence = sentence.lower()
    x = "english"
    if x in sentence:
        return True
    elif x not in sentence:
        return False     

print(sp_eng("Are you english?"))


def sp_german(sentence):
    sentence = sentence.lower()
    x = 'german'
    if x in sentence:
        return True
    if x not in sentence:
        return False

print(sp_german("My, what a beautiful patio you have!"))

print(sp_german("Hello, are you German?"))

