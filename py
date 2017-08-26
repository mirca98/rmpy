#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import argparse
import os
import shutil

def remove(name):
    if os.path.isfile(name):
        name_path = os.path.abspath(name)
        shutil.move(name_path, '/home/miroslav/lab2/basket')

    if os.path.isdir(name):
        shutil.move(name, '/home/miroslav/lab2/basket')

def restore(name):
    pass

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', action='store_true', dest='delete', help='Delete files')
    parser.add_argument('-r', action='store_true', dest='restore', help='Restore files')
    parser.add_argument('-p', '--trash-path', action='store', dest='trash_path', help='Restore files')
    parser.add_argument('NAME', nargs='+', help='Name file')

    return parser.parse_args()

def main():
    args = vars(parse())

    if args['delete']:
        for arg in args['NAME']:
            remove(arg)

if __name__ == "__main__":
    main()
