#!/usr/bin/python
""" This script makes color of each project
"""

import os

def main():

    array = []

    for proj in os.listdir('./ranking/'):
        dir = {}
        dir['proj'] = proj
        dir['color'] = '#FF7F00'
        array.append(dir)

    print 'var projects = ' + str(array)

if __name__ == '__main__':
    main()
