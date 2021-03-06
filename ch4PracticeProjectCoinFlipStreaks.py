#Write a program to find out how often a streak of six heads
#or a streak of six tails comes up in a randomly generated list
#of heads and tails.
#Your program breaks up the experiment  into two parts:
#the first part generates a list of randomly selected 'heads' and
#'tails' values, and the second part checks if there is a
#streak in it.
#Put all of this code in a loop that repeats the experiment
#10,000 times so we can find out what percentage of the coin flips
#contains a streak of six heads or tails in a row.
#As a hint, the function call random.randint(0,1) will return
#a 0 value 50% of the time and a 1 value the other 50% of the time.

import random
numberOfStreaks = 0
for experimentNumber in range(10000):

    #Code that creates a list of 100 'heads' or 'tails' values
    results = [] #Initialize or clear list for coin flip results
    for i in range(100):
        results.append(random.randint(0,1)) #Fill results list with 0 for tails and 1 for heads
        
    #Code that checks if there is a streak of 6 heads or tails in a row.
    counter = 0
    for i in range(100):
        if results[i] == results[i-1]:
            counter += 1
        else:
            counter = 0
        if counter == 5:
            numberOfStreaks += 1 #End loop once a streak of six has been found in the list
            break

print('Chance of streak: %s%%'%(numberOfStreaks/100))
