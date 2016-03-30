'''
gnome_sort.py

A sorting algorithm similar to insertion sort except that the element is moved its proper place by a series of swap

https://en.wikipedia.org/wiki/Gnome_sort
'''

def gnome_sort():
    '''
    :param seq: A list of integers
    :rtype: A list of integers
    '''
    i = 1
    last = 0

    while i < len(seq):
        if seq[i] < seq[i - 1]:
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            if i > 1:
                if last == 0:
                    last = 1
                i -= 1
            else:
                i += 1
        else:
            if last != 0:
                i = last
                last = 0
            i += 1
    return seq
