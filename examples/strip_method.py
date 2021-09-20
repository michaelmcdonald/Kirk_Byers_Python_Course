#!/usr/bin/env python

from __future__ import print_function

my_str = "     whatever, somethings else \n\n\n"

print("String with leading whitespace and three new lines")
print(my_str)
print()
print("String with leading whitespace removed, maintains new lines")
print(my_str.lstrip())
print()
print("String maintaining leading whitespace, newlines removed")
print(my_str.rstrip())
