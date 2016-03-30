'''
bogo_sort.py

Picks two elements at random and swaps them
https://en.wikipedia.org/wiki/Bogosort
'''

import random

def bogo_sort(seq):
    '''
    :param seq: A list of integers
    :rtype: A list of sorted integers
    '''

    if len(seq) == 1:
        return seq
    random.seed()
    while not is_sorted(seq):
        if len(seq) == 2:
            i, j = 0, 1
        else:
            i = random.randint(0, len(seq) - 2)
            j = random.randint(i, len(seq) - 1)
        seq[i], seq[j] = seq[j], seq[i]
    return seq


def is_sorted(seq):
    '''
    :param seq: A list of integers
    :rtype: Boolean
    '''

    return all(seq[i - 1] <= seq[i] for i in range(1, len(seq)))


if __name__ == '__main__':
    unsorted_integers = [8, 16, 4, 23, 42, 15]
    sorted_integers = bogo_sort(unsorted_integers)
    print('bogo_sort function result: {}'.format(sorted_integers))
