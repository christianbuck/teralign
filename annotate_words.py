#!/usr/bin/env python

import sys

words = None
linenr = 0
for line in sys.stdin:
    if line.startswith('Original Hyp: '):
        line = line.split()[2:]
        words = line
    elif line.startswith('Alignment: '):
        line = line.split('(')[1]
        line = line.split(')')[0]
        line = line.replace('D','')
        line = line.replace(' ','K')
        line = line.replace('I','D')

        assert len(words) == len(line)
        for i, (w, tag) in enumerate(zip(words,line)):
            print linenr, i, tag
            #print "(%d %s %s)" %(i, w, tag),
        linenr += 1
