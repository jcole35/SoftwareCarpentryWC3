#This is the second part of Weekly Challenge 3
#This script is meant to add up all the even numbers between a lower
#and upper bound (and this assumes that the lower and upper bounds
#are not included in the summation as it only adds numbers "between" them)

def Even_Number_Summation(lowerbound, upperbound):

	#first the bounds are set to integers, this is just to avoid errors
	#in the for loop, and has no consequences on the math as only numbers
	#between the bounds are included in the summation. Furthermore, the 
	#summation is set to start at zero

	lowerbound = int(lowerbound)
	upperbound = int(upperbound)
	summation = 0

	#Here a for loop goes through all the numbers between the bounds
	#first checking if the number is even. If it is even it adds it 
	#to the ongoing summation, and if it is not even then it just
	#continues on to the next number
	for number in range(lowerbound+1,upperbound):
		if (number % 2) == 0: 
			summation = summation + number
		else:
			continue

	#Once finished the function prints the total
	print(summation)

Even_Number_Summation(1,100)