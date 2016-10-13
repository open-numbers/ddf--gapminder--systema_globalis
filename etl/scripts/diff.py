# -*- coding: utf-8 -*-

import os
import sys

threshold = 10  # precentage

def diff(fin, fout):
    with open(fin) as f:
        lines = f.readlines()
        f.close()

    keep = []
    for l in lines:
        l = l.strip()
        if '->' not in l:
            if l.startswith('+++ ') or l.startswith('--- '):
                keep.append(l)
        else:
            numbers = l.split(',')[-1]
            if '->' not in numbers:
                keep.append(l)
            else:
                n0, n1 = numbers.split('->')
                n0 = float(n0)
                n1 = float(n1)
                if n0 == n1:
                    continue
                if n0 == 0:
                    if abs(n1) > threshold / 100:
                        keep.append(l)
                elif n0 * n1 < 0:
                    keep.append(l)
                elif (abs(n1-n0)) / abs(n0) * 100 > threshold:
                    keep.append(l)
    # save to file
    with open(fout, 'w') as f:
        f.write('\n'.join(keep))
        f.close()


if __name__ == "__main__":
    fin, fout = sys.argv[-2:]
    assert os.path.exists(fin)
    diff(fin, fout)
