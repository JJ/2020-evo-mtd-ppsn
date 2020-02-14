#!/usr/bin/env python

from os.path import dirname, abspath, join
import sys

# Find code directory relative to our directory
THIS_DIR = dirname(__file__)
CODE_DIR = abspath(join(THIS_DIR, '..'))

sys.path.append(CODE_DIR)

from evomtd.config.nginx import generate

print( generate() )

