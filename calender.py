"""
w3resource:
Write a Python program that prints the calendar for a given month and year.
Note: Use 'calendar' module.

Date: Sun 28 May
"""
import calendar
y = int(input("year : "))
m = int(input("month : "))
print(calendar.month(y, m))