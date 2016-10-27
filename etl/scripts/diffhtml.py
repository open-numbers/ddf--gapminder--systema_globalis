# -*- coding: utf-8 -*-

import os
import sys
import shutil

threshold = 10  # percentage
htmldirName = 'diffhtml'
diffjsName = 'diffhtml.js'

def diff(fin):

    htmldir = os.path.join(os.path.dirname(os.path.abspath(fin)), htmldirName)

    if not os.path.exists(htmldir):
        os.makedirs(htmldir)

    shutil.copy(diffjsName, os.path.join(htmldir, diffjsName))

    with open(fin) as f:
        lines = f.readlines()
        f.close()

    mainList = []
    changedRowsList = []
    changedRowsFile = ''
    mainList.append('<script type="text/javascript" src="' + diffjsName + '"></script>')
    mainList.append('<ul>')
    for l in lines:
        l = l.strip()
        if '->' not in l:
            if l.startswith('--- '):

                if len(changedRowsList) > 1:

                    # finish current file
                    changedRowsList.append('</table>')
                    mainList.append('<li><span>' + changedRowsFile + '</span></li>')
                    with open(os.path.join(htmldir, changedRowsFile + '.html'), 'w') as f:
                        f.write('\n'.join(changedRowsList))
                        f.close()

                #start new file
                changedRowsList = []
                changedRowsList.append('<table>')
                changedRowsFile = l[6:]

            elif l.startswith('+++,') or l.startswith('---,'):
                changedRowsList.append('<tr><td>' + l.replace(',','</td><td>') + '</td></tr>')
        else:
            numbers = l.split(',')[-1]
            if '->' not in numbers:
                changedRowsList.append('<tr><td>' + l.replace(',','</td><td>') + '</td></tr>')
            else:
                n0, n1 = numbers.split('->')
                n0 = float(n0)
                n1 = float(n1)
                if n0 == n1:
                    continue
                if n0 == 0:
                    if abs(n1) > threshold / 100:
                        changedRowsList.append('<tr><td>' + l.replace(',','</td><td>') + '</td></tr>')
                elif n0 * n1 < 0:
                    changedRowsList.append('<tr><td>' + l.replace(',','</td><td>') + '</td></tr>')
                elif (abs(n1-n0)) / abs(n0) * 100 > threshold:
                    changedRowsList.append('<tr><td>' + l.replace(',','</td><td>') + '</td></tr>')

    mainList.append('</ul>')

    # save to file
    with open(os.path.join(htmldir, 'index.html'), 'w') as f:
        f.write('\n'.join(mainList))
        f.close()


if __name__ == "__main__":
    fin = sys.argv[-1]
    assert os.path.exists(fin)
    diff(fin)
