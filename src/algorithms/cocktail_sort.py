'''
cocktail_sort.py

A bidirectional bubble sort. Walks the elements bidirectionally, swapping
neighbors if one should come before/after the other.

https://en.wikipedia.org/wiki/Cocktail_shaker_sort
'''


def cocktail_sort(seq):
    '''
    :param seq: A list of integers
    :rtype: A list of integers
    '''

    lower_bound = -1
    upper_bound = len(seq) - 1
    swapped = True

    while swapped:
        swapped = False
        lower_bound += 1
        for i in range(lower_bound, upper_bound):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        upper_bound -= 1
        for i in range(upper_bound, lower_bound, -1):
            if seq[i] < seq[i - 1]:
                seq[i], seq[i - 1] = seq[i - 1], seq[i]
                swapped = True
    return seq


if __name__ == '__main__':
    unordered_integers = [8, 15, 23, 42, 4, 16]
    ordered_integers = cocktail_sort(unordered_integers)
    print('cocktail_sort result: {}'.format(ordered_integers))
