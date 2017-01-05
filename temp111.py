# coding:utf-8
# Copyright

import re


with open('temp.log', 'r') as f:
    x = f.read()
    s0 = re.compile(r'INFO (\d+)')
    print(x)
    yy = re.findall(s0, x)
    zz = len(yy)-1
    print(yy[zz])
