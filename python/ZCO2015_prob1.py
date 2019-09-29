# -*- coding: utf-8 -*-
"""
ZCO 2015: Solutions to the problems in ZCO 2015, India. Full paper at: http://www.iarcs.org.in/inoi/2015/zco2015/zco2015-afternoon.pdf
Problem 1:
An interval is a pair of positive integers [a, b] with a ≤ b. It is meant to denote the set of integers
that lie between the values a and b. For example [3, 5] denotes the set {3, 4, 5} while the interval
[3, 3] denotes the set {3}.
We say that an interval [a, b] is covered by an integer i, if i belongs to the set defined by [a, b].
For example interval [3, 5] is covered by 3 and so is the interval [3, 3].
Given a set of intervals I, and a set of integers S we say that I is covered by S if for each
interval [a, b] in I there is an integer i in S such that [a, b] is covered by i. For example, the set
{[3, 5], [3, 3]} is covered by the set {3}. The set of intervals {[6, 9], [3, 5], [4, 8]} is covered by the set
{4, 5, 8}. It is also covered by the set {4, 7}.
We would like to compute, for any set of intervals I, the size of the smallest set S that covers
it. You can check that for the set of intervals {[6, 9], [3, 5], [4, 8]} the answer is 2 while for the set
of intervals {[3, 5], [3, 3]} the answer is 1.
"""
from random import randint

"""
Prepare input data
"""
N = 3
MAX = 20
input_arr = []
max_val = 0
"""
input_arr = [[16, 17, 18, 19, 20], [13, 14, 15, 16, 17, 18], [4, 5, 6, 7, 8, 9]]
max_val = 20
"""

for i in range(N):
    start = randint(1,MAX)
    end = start + randint(1,MAX/N)
    if end > max_val:
        max_val = end
    input_arr.append(range(start,end+1))

print input_arr

"""
Main code starts from here.
First create an array which will smartly track 
how many times an element occurs in the input data
We use the heuristic that if the element occurs n times
then all the n-1 bits should be set in the count of that item.
This can help us in identifying how many times
the item was added in different sets uniquely.

We also try simply counting the number of times it was added.
Both methods seem to work.
"""

val_arr = [0 for k in range(max_val+1)] # For storing binary presence

val_arr_c = [0 for k in range(max_val+1)] # For storing count presence

print max_val, len(val_arr), len(val_arr_c)


# Fill both the value arrays with the count heuristics mentioned above
for i in range(len(input_arr)):
    for j in input_arr[i]:
        val_arr[j] = val_arr[j]*2 + 1
        val_arr_c[j] += 1
    
for i in range(len(val_arr)):
    print "(%s=>%s,_c[%s])" % (i, val_arr[i], val_arr_c[i]),


"""
Recursively find if the maximum possible sum exists for the binary heurestic.
If yes return 1
If not then find the next maximum possble sum and 
    return 1 + plus the value of the recursive call
If n == 0 then exit as this is the default count.
"""

def find_set(arr,n):
    max_sum = (2**n) -1
    print "Entering for n=%s\tmax_sum=%s" % (n, max_sum)
    if n == 0:
        return 0
    try:
        i = arr.index(max_sum)
        print "arr[%s]=%s, max_sum = %s, n=%s" % (i, arr[i],max_sum, n)
        return 1
    except ValueError:
        return 1+find_set(arr,n-1)
    return 0

"""
Recursively find if the maximum possible sum exists for the count heurestic.
If yes return 1
If not then find the next maximum possble sum and 
    return 1 + plus the value of the recursive call
If n == 0 then exit as this is the default count.
"""
  
def find_set_c(arr,n):
    max_sum = n
    print "Entering for n=%s\tmax_sum=%s" % (n, max_sum)
    if n == 0:
        return 0
    try:
        i = arr.index(max_sum)
        print "arr[%s]=%s, max_sum = %s, n=%s" % (i, arr[i],max_sum, n)
        return 1
    except ValueError:
        return 1+find_set_c(arr,n-1)
    return 0  

# Call both the heuristics on their respective arrays.

print "\nFind spanning items in binary"    
n = find_set(val_arr, N)
print "\nFind spanning items in count"
n1 = find_set_c(val_arr_c, N)
print "Min number elements which span the input are: %s, %s" % (n,n1)
