#! /usr/bin/python

def right_justify(s):
    # figure out what column seventy is 
    adjusted_length = 70 - len(s)
    column_70_text = (" " * adjusted_length) + s 
    print(column_70_text)

right_justify('Nick')