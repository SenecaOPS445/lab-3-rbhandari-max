#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: rbhandari17@myseneca.ca
def describe_temperature(temp):
    if temp > 30:
        return 'hot'
    elif temp < 0:
        return 'cold'
    elif temp == 20:
        return 'perfect'
    return 'ok'
print(describe_temperature(50))   # Should return 'hot'
print(describe_temperature(20))   # Should return 'perfect'
print(describe_temperature(-50))  # Should return 'cold'
print(describe_temperature(25))   # Should return 'ok'
print(describe_temperature(10))   # Should return 'ok'
