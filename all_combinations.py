import sys
sys.setrecursionlimit(10000000)

"""
begin shitty "readme"...

find the shortest string which contains all substrings of length N:

stu@sente ~ python all_combinations.py
alpha_len:      2
code_len:       5
solution_len:   36
solution:       000001000110010100111010110111110000

there are 2^5 strings that must exist as substrings somewhere in our answer
00000
00001
00010
...
...
11101
11110
11111

They are all contained in this string!
000001000110010100111010110111110000


http://i.imgur.com/7vWyVE6.png
http://c.sente.cc/gLEr/all_combinations.html


"""

def getSubstrings(alphabet, sslen, cur=""):
    if len(cur) == len(alphabet) ** sslen + sslen-1:
        return cur
    for i in alphabet:
        if (cur+i)[-sslen:] in cur:
            continue
        s = getSubstrings(alphabet,sslen,cur+i)
        if s:
            return s


def main():
    """docstring for mai"""
    alphabet = int(sys.argv[1])
    codelength = int(sys.argv[2])


    s='0123456789'
    answer = getSubstrings(s[:alphabet],codelength)
    print "alpha_len:\t%d\ncode_len:\t%d\nsolution_len:\t%d\nsolution:\t%s" % (alphabet, codelength, len(answer), answer)


if __name__ == '__main__':
    main()
