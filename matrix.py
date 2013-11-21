#!/usr/bin/python
""" This script makes OSS relativity matrix.

"""

import os
from math import sqrt

def calc_rel(ranka, rankb):
    """ calculate OSS ranking relativity by summing up commits number
        committed by common author.
    """
    common = 0
    for name, count in ranka.items():
        if rankb.has_key(name):
            common += min(count, rankb[name])
    return sqrt(common)

def main():

    array = []

    for proj in os.listdir('./ranking/'):
        fd = open('./ranking/' + proj)
        lines = fd.readlines()
        fd.close()

        dir = {}

        for line in lines:
            splitted = line.split()
            count = int(splitted[0])
            name = ' '.join(splitted[1:])
            dir[name] = count

        array.append({
            'proj' : proj,
            'rank' : dir
        })

    length = len(array)
    matrix = [[0 for i in range(length)] for j in range(length)]

    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j] = calc_rel(array[i]['rank'], array[j]['rank'])
            matrix[j][i] = matrix[i][j]

    print 'var matrix = ' + str(matrix)

if __name__ == '__main__':
    main()
