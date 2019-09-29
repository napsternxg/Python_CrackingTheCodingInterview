"""
Original Code by Sangam Kumar Jain
You can connect with him at: http://www.facebook.com/jain.sangam

"""
val = 7

loop = 0;

current_index = 1;

list = [1,7,11,13,17,19,23,29]

def nextprime():
	global current_index;
	global loop;
	
	if(current_index == 7):
		loop = loop+1;
		current_index = 0;
	else:
		current_index = current_index +1
	return loop * 30 + list[current_index]
	
	
number = 18505779463480206643200;

while(number%2 ==0):
	number = number/2;
	print "2"
	if number == 2:
		print 2;
		exit(0);

while(number%3 ==0):
	number = number/3;
	print "3"
	if number == 3:
		print 3;
		exit(0);

while(number%5 ==0):
	number = number/5;
	print "5"
	if number == 5:
		print 5;
		exit(0);		

	
while(True):
	if number == val:
		print val;
		exit(0);
	while(number%val == 0):
		print val;
		number = number / val;
		if number == val:
			print val;
			exit(0);
	
	val = nextprime()