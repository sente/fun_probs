import re

"""
given a grid of words, use regular expressions to find the longest word
composed of adjacent letters!

stu@sente $ python hackity_hack_hack.py
mzhs
klpt
yeua
eore
towe
('spare', ((3, 0), (2, 1), (3, 2), (2, 3), (1, 2)))
"""


grid = "mzhs klpt yeua eore towe".split()
#grid = "fxie amlo ewbx astu".split()
nrows, ncols = len(grid), len(grid[0])

# A dictionary word that could be a solution must use only
# the grid's letters and have length >= 3. (With a case-
# insensitive match.)
alphabet = ''.join(set(''.join(grid)))
possible_solution = re.compile('[' + alphabet + ']{4,}$', re.I)

words = set(word.lower() for word in open('words5.lst').read().splitlines() if possible_solution.match(word))
prefixes = set(word[:i] for word in words for i in range(2, len(word)+1))

def neighbors((x, y)):
    for nx in range(max(0, x-1), min(ncols, x+2)):
        for ny in range(max(0, y-1), min(nrows, y+2)):
            yield (nx, ny)

def extending(prefix, path):
    if prefix in words:
        yield (prefix, path)
    for (nx, ny) in neighbors(path[-1]):
        if (nx, ny) not in path:
            prefix1 = prefix + grid[ny][nx]
            if prefix1 in prefixes:
                for result in extending(prefix1, path + ((nx, ny),)):
                    yield result

def solve():
    for y, row in enumerate(grid):
        for x, prefix in enumerate(row):
            for result in extending(prefix, ((x, y),)):
                yield result

print '\n'.join(grid)
# Print a maximal-length word and its path:
print max(solve(), key=lambda (word, path): len(word))



