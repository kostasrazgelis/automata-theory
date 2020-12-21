import sys, getopt
from numpy import *

class Grammar:
    def __init__(self):
        self.non_ending_conditions = []
        self.ending_conditions = []
        self.syntax = []




def initialize_grammar(G):
    try:
        inputfile = open(sys.argv[1], 'r')
    except:
        print("file is not correct and did not open.... please put a correct root")
        sys.exit(1)
    else:
        print('The file has been opened, scanning the grammar now')

    tmp = inputfile.read().split()

    K = int(tmp[0])
    for x in range(1, 1+K):
        G.non_ending_conditions.append(tmp[x])

    L = int(tmp[K+1])
    for x in range(K+1+L, K+2+L):
        G.ending_conditions.append(tmp[x])

    N = int(tmp[K+L+2])

    matrix = []
    list = []


    for x in range(K+L+2, K+L+N+3,2):
        list.append(tmp[x])
        list.append(tmp[x+1])
        matrix.append(list)


    list.append(0)
    print(matrix)


    print(G.non_ending_conditions)
    print(G.ending_conditions)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:o", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile.txt> -o <outputfile.txt')
        sys.exit(2)

    if len(sys.argv) != 2:
        print("Not the correct format.... python test.py <file.txt>")
        sys.exit(1)

    G = Grammar()

    initialize_grammar(G)


if __name__ == "__main__":
    main(sys.argv[1:])

