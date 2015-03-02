#!/usr/bin/env python

import sys

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-prefix', help="id-prefix", default='S')
    args = parser.parse_args(sys.argv[1:])

    for linenr, line in enumerate(sys.stdin):
        print "%s (%s_%s)" %(line.strip(), args.prefix, linenr)
