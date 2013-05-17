import sys
sys.setrecursionlimit(10000000)

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
