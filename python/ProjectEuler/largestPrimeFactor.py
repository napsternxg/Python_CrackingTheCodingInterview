"""
The original code for the following program was written by Sangam Kumar Jain and can be found in the file test.py in this git project
You can connect with him at: http://www.facebook.com/jain.sangam

The code was written as a part of solving Project Euler Problem 3 (http://projecteuler.net/problem=3) which deals with finding the largest prime factor of a large number.

Currently the code finds all the powers of all prime factors of any large number.

I have rewritten a more modular and optimized version of the above code and tried to make it more easily comprehendable.

"""
import sys;
import datetime;

# Profiling started, string to write to log file
print "#"*60
print "Profiling started for: ", sys.argv;
print "Start time: ", str(datetime.datetime.now()), "\n\n";

def nextprime(loop, current_index, prime_list):
# Function to return the next prime to check for and also to populate the list array with numbers mapping to the current list items for the next 30 numbers.
	if(current_index == 7):
		loop = loop+1;
		current_index = 0;
	else:
		current_index = current_index +1
	return (loop * 30 + prime_list[current_index], loop, current_index, prime_list)

def checkDivisibility(number, val):
# Strip all powers of subsequent primes from the number	till the number equal to the prime which divides it
	i = 1;
	factors = []
	while(number%val == 0):
		#print number, val**i;
		factors.append(val**i);
		number = number / val; # Reduce the number by factor of val
		i = i + 1;
	return (number, factors)
	
	
def updateFactors(factors, factor):
	# Function to update the factors of the number with the factors found using checkDivisibility
	if factor != [] :
	# Append factor only if it is non empty
		factors.append(factor);
	return factors
	
	
def findFactors(number):
	# Function to find all the factors of the number and to also print the largest factor of the number
	val = 7;
	loop = 0;
	current_index = 1;
	prime_list = [1,7,11,13,17,19,23,29]; # List to populate with all primes less than 30

	factors = []; # Store all prime powers of a number
	# Strip all powers of 2 from the number	
	number, factor = checkDivisibility(number, 2);
	factors = updateFactors(factors, factor);

	# Strip all powers of 3 from the number
	number, factor = checkDivisibility(number, 3);
	factors = updateFactors(factors, factor);

	# Strip all powers of 5 from the number
	number, factor = checkDivisibility(number, 5);
	factors = updateFactors(factors, factor);	

	# Strip all powers of subsequent primes from the number	till the number equal to the prime which divides it
	while(number/val != 0):
		number, factor = checkDivisibility(number, val);
		factors = updateFactors(factors, factor);
		#Get Next Prime to check for and simultaneously update loop, current_index and prime_list
		val, loop, current_index, prime_list = nextprime(loop, current_index, prime_list)
	#Append the last factor in the factor list
	#factors.append([val])
	#print "Largest Prime:", factors[-1][0]
	return factors;
	
def findLargestPrimeFactor(number):
	return findFactors(number)[-1][0];

#Run the code for number given below and print the largest factor along with the set of powers of prime factors
#number = 18505779463480206643200; # Number to factorize
number = long(sys.argv[1]);
factors = findFactors(number)
print "All powers of prime factors of ", number, " are as follows:\n", factors, "\n\nAnd the largest prime factor is:", factors[-1][0];

#Finish Profiling Printing
print "\n\nEnd time: ", str(datetime.datetime.now());
print "Profiling finished for: ", sys.argv;
print "#"*60