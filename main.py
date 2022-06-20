from PIL import Image

import os
import sys

img = Image.open('meteor_challenge_01.png').convert('RGB')
size = x, y = img.size

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)


def countPixel():
    list_red = []
    list_white = []
    for _x in range(x):
        for _y in range(y):
            coord = _x, _y
            # Detecting RED pixels.
            if img.getpixel(coord) == red:
                list_red.append(coord)
            # Detecting WHITE pixels.
            if img.getpixel(coord) == white:
                list_white.append(coord)
    return list_red, list_white


def countOnWater():
    red_water = []
    x_list = []

    # Adding blue pixel X coordinates to a list
    for _x in range(x):
        for _y in range(y):
            coord = _x, _y
            if img.getpixel(coord) == blue:
                if _x not in x_list:
                    x_list.append(_x)

    # Searching red pixels in X coordinates from the list
    for _x in x_list:
        for _y in range(y):
            coord = _x, _y
            if img.getpixel(coord) == red:
                red_water.append(coord)
    return red_water, x_list


def hiddenPhrase():
    # Using the generated image to try finding the characters.
    tmp = createNewImg()
    x, _ = tmp.size
    string = ''
    strings = []
    alternator = 0
    alt = False
    _x = 0
    while _x < x:
        if not alt:
            coord = _x, 0
            if tmp.getpixel(coord) == black:
                string = string+'0'
            if tmp.getpixel(coord) == white:
                string = string+'1'
            if tmp.getpixel(coord) == red:
                string = string+'2'
            alternator += 1
            if alternator == 2:
                alt = True
                alternator = 0
                _x = _x-1

        if alt:
            _coord = _x, 1
            if tmp.getpixel(_coord) == black:
                string = string+'0'
            if tmp.getpixel(_coord) == white:
                string = string+'1'
            if tmp.getpixel(_coord) == red:
                string = string+'2'
            alternator += 1
            if alternator == 2:
                strings.append(string)
                string = ''
                alt = False
                alternator = 0
        _x += 1

    string = ' '.join(strings)
    return string  # This is the closest attempt.


def createNewImg():
    # Generates an image that maps the occasions of RED and WHITE pixels in the X axis
    found = False
    new_img = Image.new('RGB', (x, 2))
    for _x in range(x):
        for _y in range(y):
            coord = _x, _y
            if img.getpixel(coord) == red:
                if not found:
                    new_img.putpixel((_x, 0), red)
                if found:
                    new_img.putpixel((_x, 1), red)
                found = True
            if img.getpixel(coord) == white:
                if not found:
                    new_img.putpixel((_x, 0), white)
                if found:
                    new_img.putpixel((_x, 1), white)
                found = True
        found = False
    new_img.save('new.png')
    return new_img


menu = {}
menu['1'] = "How many STARS?"
menu['2'] = "How many METEORS?"
menu['3'] = "How many METEORS ON WATER?"
menu['4'] = "What is the HIDDEN PHRASE?"
menu['5'] = "Restart"
menu['0'] = "Exit"

while True:
    options = menu.keys()

    for entry in options:
        print(entry, menu[entry])

    op = input("Select your option: ")

    if op == '1':
        _, _white = countPixel()
        print('\nThere are ' + str(len(_white)) + ' stars.\n')

    elif op == '2':
        _red, _ = countPixel()
        print('\nThere are ' + str(len(_red)) + ' meteors.\n')

    elif op == '3':
        red_water, _ = countOnWater()
        print('\nThere are ' + str(len(red_water)) + ' meteors on water.\n')

    elif op == '4':
        string = hiddenPhrase()
        print(string)

    elif op == '5':
        print("\n\nRestarting.\n\n")
        os.execv(sys.executable, ['python main.py'] + sys.argv)

    elif op == '0':
        break

    else:
        print("\n\nTry again.\n\n")
