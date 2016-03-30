'''
bubble_sort.py

Compares and swaps adjacent elements.
https://en.wikipedia.org/wiki/Bubble_sort
'''

def bubble_sort(seq):
    '''
    :param seq: A list of integers
    :rtype: A list of integers
    '''
    length = len(seq)
    for _ in range(length):
        for n in range(1, length):
            if seq[n - 1] > seq[n]:
                seq[n - 1], seq[n] = seq[n], seq[n - 1]
    return seq


if __name__ == '__main__':
    unordered_integers = [8, 15, 23, 42, 4, 16]
    ordered_integers = bubble_sort(unordered_integers)
    print('bubble_sort result: {}'.format(ordered_integers))
