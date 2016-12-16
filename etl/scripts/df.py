#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

threshold = 10  # precentage

def diff(lines):
    keep = []
    for l in lines:
        l = l.strip()
        if '->' not in l:
            l = l+','
            if l.startswith('+++,') or l.startswith('---,') or '...' in l:
                keep.append(l)
            if l.startswith('@'):  # add header in header line
                l = l+'changes(%)'
                keep.append(l)
        else:
            numbers = l.split(',')[-1]
            if '->' not in numbers:
                keep.append(l+',')
            else:
                n0, n1 = numbers.split('->')
                n0 = float(n0)
                n1 = float(n1)
                if n0 == n1:
                    continue
                if n0 == 0:
                    if abs(n1) > threshold / 100:
                        keep.append(l+',')
                elif n0 * n1 < 0:
                    keep.append(l+',')
                elif (abs(n1-n0)) / abs(n0) * 100 > threshold:
                    dif = "{:.2f}".format(((abs(n1-n0)) / abs(n0) * 100 ))
                    keep.append(l+','+dif)
    return keep


if __name__ == "__main__":
    res = diff(sys.stdin)
    for l in res:
        print(l)
