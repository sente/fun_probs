import operator
import sys
from itertools import imap, repeat
from collections import deque

"""
    find a path between two words while only changing one letter at time.

    stu@sente.cc $ python word_up_yo.py monkey houses
    monkey honkey honker hooker looker looser looses louses houses
"""



def toTup(s):
    return tuple(imap(lambda x: ord(x) - 97, s))
def toStr(t):
    return  "".join(imap(lambda x: chr(97 + x), t))

def getNeighbors(start, wordset, pos = None):
    if pos == None:
        #None = give neighbors for all directions/characters
        for p in xrange(len(start)):
            for i in getNeighbors(start, wordset, p):
                yield i
        return
    #okay so pos has a real value now

    cur = list(start)
    for v in xrange(26):
        cur[pos] = v
        out = tuple(cur)
        if (out not in wordset) or (v==start[pos]):
            continue #if it's not a word, or it's our starting word, continue.
        yield out


def bfs(graph, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(getNeighbors(n, graph)) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])


def shortest_path(graph, start, end):
    paths = {None:[]}
    for parent, child in bfs(graph,start):
        paths[child] = paths[parent]+[child]
        if child == end:
            return paths[child]
    return None


if __name__ == '__main__':

    source_word = sys.argv[1]
    target_word = sys.argv[2]

    words = set()
    for word in file("WORD.lst"):
        word = word.strip()
        if len(word) == len(source_word):
            words.add(toTup(word))
    try:
        for i in shortest_path(words,toTup(source_word),toTup(target_word)):
            sys.stdout.write('%s ' % (toStr(i)))
    except:
        sys.stderr.write("There aren't any paths from %s to %s" % (source_word, target_word))

    sys.stdout.write('\n')

