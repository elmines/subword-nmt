#! /usr/bin/env python
from __future__ import print_function
import sys
import io
from collections import Counter


def write_vocab(instream, outstream):
    c = Counter()
    if instream != sys.stdin:
        instr = open(instream, "r", encoding="utf-8")
        lines = instr.readlines()
    else:
        instr = instream
        lines = instr

    for line in lines:
        for word in line.split():
            c[word] += 1
    if instr != sys.stdin: instr.close()

    out = open(outstream, "w", encoding="utf-8") if outstream != sys.stdout else outstream
    for key,f in sorted(c.items(), key=lambda x: x[1], reverse=True):
        out.write( key + " " + str(f) + "\n" )
    if out != sys.stdout: out.close()

if __name__ == "__main__":
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", write_through=True, line_buffering=True)
    write_vocab(sys.stdin, sys.stdout)
