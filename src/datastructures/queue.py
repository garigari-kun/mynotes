'''
queue.py

https://en.wikipedia.org/wiki/Queue_%28abstract_data_type%29
'''

from collections import deque

class Queue(object):

    queue_list = deque([])

    def __init__(self):
        queue_list = deque([])

    def add(self, value):
        '''
        Add element as the last item in a queue
        '''
        self.queue_list.append(value)

    def remove(self):
        '''
        Remove element from the front of the queue and it's element
        '''
        return self.queue_list.popleft()

    def is_empty(self):
        '''
        Return whether the queue is empty or not
        '''
        return not len(self.queue_list)

    def size(self):
        '''
        Return size of the queue
        '''
        return len(self.queue_list)

if __name__ == '__main__':
    queue = Queue()
    for i in range(10):
        queue.add(i)
    print("The size: {}".format(queue.size()))
    first = queue.remove()
    print("The item that removed from queue: {}".format(first))
