#!/usr/bin/python
import sys

from utilities import comment_tree

def print_result(tree, dir_name):
    res = comment_tree(tree, dir_name)
    if res == 1:
        print('Directory error')
        return 1
    print(res)

print('type your json:')
s = ''
for line in sys.stdin:
    s += line
print_result(s, sys.argv[1])
