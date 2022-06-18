from PIL import Image

import os
import sys

img = Image.open('meteor_challenge_01.png').convert('RGB')
size = x, y = img.size

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

red = (255, 0, 0)
blue = (0, 0, 255)
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
    counter = 0
    groups = []
    coords = []
    for _x in range(x):
        counter += 1
        for _y in range(y):
            coord = _x, _y
            if img.getpixel(coord) == (255, 0, 0):
                groups.append('1')
            if img.getpixel(coord) == (255, 255, 255):
                groups.append('0')
        if counter == 4:
            groups = ['0'] if groups == [] else groups
            a = ''.join(groups)
            coords.append(int(a))
            groups = []
            counter = 0
    return coords


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
        chars = hiddenPhrase()
        print(''.join(str(chars)))
        print(len(chars))
        _red, _white = countPixel()
        red_water, x_list = countOnWater()
        # print(' '.join(list_red))
        # print(' '.join(list_white))

    elif op == '5':
        print("\n\nRestarting.\n\n")
        os.execv(sys.executable, ['python main.py'] + sys.argv)

    elif op == '0':
        break

    else:
        print("\n\nTry again.\n\n")
