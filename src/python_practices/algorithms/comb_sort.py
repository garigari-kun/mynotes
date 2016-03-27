'''
comb_sort.py

Improves on bubble sort by using a gap sequence to remove turtles.


https://en.wikipedia.org/wiki/Comb_sort
'''

def comb_sort(seq):
    '''
    :param seq: A list of integers
    :rtype: A list of integers
    '''

    gap = len(seq)
    swap = True

    while gap > 1 or swap:
        gap = max(1, int(gap / 1.25))
        swap = False
        for i in range(len(seq) - gap):
            #print(seq)
            if seq[i] > seq[i + gap]:
                seq[i], seq[i + gap] = seq[i + gap], seq[i]
                swap = True
    return seq


if __name__ == '__main__':
    unordered_integers = [8, 15, 23, 42, 4, 16]
    ordered_integers = comb_sort(unordered_integers)
    print('comb_sort reuslt: {}'.format(ordered_integers))
