"""
w3resource:
Write a Python program to calculate the number of days between two dates.

Date: Sun 28 May (D2, P2)
"""

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)