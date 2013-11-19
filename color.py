#!/usr/bin/python
""" This script makes color of each project.
"""

import os
import random

def main():

    array = []

    for proj in os.listdir('./ranking/'):
        dir = {}
        dir['proj'] = proj
        color = '#'
        crange = '89ABCDE'
        for i in range(6):
            color += crange[random.randint(0, 6)]
        dir['color'] = color
        array.append(dir)

    print 'var projects = ' + str(array)

if __name__ == '__main__':
    main()
