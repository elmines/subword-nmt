#! /usr/bin/env python
from __future__ import print_function
import sys
from collections import Counter

c = Counter()

def write_vocab(instream, outstream):

    if instream = sys.stdin:
        for line in sys.stdin:
            for word in line.split():
                c[word] += 1
    else:
        with open(instream, "r", encoding="utf-8") as instr:
            for line in instr.readlines():
                for word in line.split():
                    c[word] += 1

    if outstream = sys.stdout:
        for key,f in sorted(c.items(), key=lambda x: x[1], reverse=True):
            print(key+" "+ str(f))
    else:
        with open(outstream, "w", encoding="utf-8") as out:
            for key,f in sorted(c.items(), key=lambda x: x[1], reverse=True):
                out.write( key + " " + str(f) + "\n" )

if __name__ == "__main__":
    instream = sys.stdin if len(sys.argv) == 0 else sys.argv[0]
    oustream = sys.stdout if len(sys.argv) < 2 else sys.argv[1]
    write_vocab(instream, outstream)
