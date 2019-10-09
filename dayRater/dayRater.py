#!/usr/bin/env python

''' This is a dayRater project
		Simple program where I write a code for how my day went, after a while of consecutive responses
		I should be able to take some long-term measures
'''

import datetime
import os
import sys

all_options = ['a','g','b','n','t','u','f','s','h']

# Check/compare the date
f = open("date.txt","r")
lastDate = f.read(20).split("\n")[0]
curDate = str(datetime.datetime.now()).split(" ")[0]

# Already logged today
if (lastDate == curDate):
	print "Error: Already rated today, date is: ",curDate
	f.close()
	exit(1)

f.close()

# Prompt user for input
print "Please enter one of the follow characters to describe your day:\n\
a - Amazing, one of the best\n\
g - Really good\n\
b - Better than 'average'\n\
n - Neutral, alright\n\
t - Tiring, exhausting\n\
u - Sad, upsetting\n\
f - Frustrating\n\
s - Stressful\n\
h - Horrible, just generally really bad"

# Record input
inp = sys.stdin.readline().split("\n")[0]

# Make sure input is properly formatted/accurate
if (len(inp) > 1 or inp not in all_options):
	print "Error: Improperly formatted or unsupported response: ",inp
	exit(1)

# Submit input
file = open("days.txt","a")
file.write(inp)
file.close()

# Wipe the date file
os.remove("date.txt")

# Advance/update the date
f = open("date.txt","w")
f.write(curDate)
f.close()

# Done!
exit(0)