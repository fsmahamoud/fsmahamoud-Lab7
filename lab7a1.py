#!/usr/bin/env python3
# Student ID: fsmahamoud

from lab7a import *

# Creating Time objects
t1 = Time(8, 0, 0)
t2 = Time(8, 55, 0)
t3 = Time(9, 50, 0)

# Time to add
td = Time(0, 50, 0)

# Sum of times
tsum1 = sum_times(t1, td)
tsum2 = sum_times(t2, td)
tsum3 = sum_times(t3, td)

# Formatting and printing the results
ft = format_time
print(ft(t1), '+', ft(td), '-->', ft(tsum1))  # Output the sum for t1
print(ft(t2), '+', ft(td), '-->', ft(tsum2))  # Output the sum for t2
print(ft(t3), '+', ft(td), '-->', ft(tsum3))  # Output the sum for t3
