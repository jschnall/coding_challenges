import numpy as np

'''
Coding exercise for Asana.
Rabbit starts in center of matrix, or largest center element if even dimension(s),
Continues moving to largest neighboring value, until it's 0, then returns total consumed
'''


def eat_carrots(matrix):
    array = np.asarray(matrix)
    dimens = array.shape
    height = dimens[0]
    width = dimens[1]
    halfh = height / 2
    halfw = width / 2

    # find the starting indices
    yindex = halfh - 1 if height % 2 == 0 else halfh
    xindex = halfw - 1 if width % 2 == 0 else halfw
    center = array[yindex:halfh + 1, xindex:halfw + 1]
    max_index = np.argmax(center)
    center_indices = np.unravel_index(max_index, center.shape)
    # location stored as y,x
    location = (yindex + center_indices[0], xindex + center_indices[1])

    total = array[location]
    while array[location] != 0:
        array[location] = 0
        location = move_rabbit(array, location)
        total += array[location]
    return total


def move_rabbit(array, location):
    y = location[0]
    x = location[1]
    dimens = array.shape
    height = dimens[0]
    width = dimens[1]

    starty = max(0, y - 1)
    endy = min(y + 2, height)
    startx = max(0, x - 1)
    endx = min(x + 2, width)

    neighborhood = array[starty:endy, startx:endx]
    max_index = np.argmax(neighborhood)
    neighborhood_indices = np.unravel_index(max_index, neighborhood.shape)

    return starty + neighborhood_indices[0], startx + neighborhood_indices[1]




