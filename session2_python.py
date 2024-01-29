# Developer Name: Izzati Baharom
# Program description: Write a program in Python to define an array, 
# print all the elements found in an array, 
# add a new element at the end of the array, 
# remove an element from an array,
# print the element found at a specific position in the array, 
# add an element at a specific position in the array and to 
# remove all the elements (clear) found in the array.

# define an array
cars = ['Proton','Volvo','BMW'] #cars is an array which holds a set of values

# print all elements found in an array - cars
for x in cars:
    print(x)

# print the number of elements found in the array
print('Number of cars: '+ str(len(cars)))

#len produce numerical output, print produce string output
# so add str if print os followed with string statement 
# e.g: Number of elements:...

print(len(cars))

# remove BMW from cars array
# remove should mentioned the name of the elements
cars.remove('BMW')
print(cars)

#Add a new car name at the end of the array
cars.append('Honda')
cars.append('BMW')
print(cars)

# print the element found at a specific position in the array
print(cars[2])
x = cars.index('Volvo')
print(x)

# Add a new element in a particular index position
# Volvo is at the index = 1
cars.insert(1, "Audi")
print(cars)

#remove an element found at a particular position or index
# pop should specify the index
cars.pop(1)
print(cars)

#sort the elements found in the array in ascending order
cars.sort()
print(cars)

#sort the elements found in the array in descending order
cars.sort(reverse=True)
print(cars)

# Clear all elements found in array
cars.clear()
print(cars)

#------------------------------NEW CODE--------------------------#
#character/string typed of array
full_name = 'NURSHAFIQAH IZZATI'
print('Number of letters found in my name: '+str(len(full_name)))
print(len(full_name))
#print of datatype of full_name
print(type(full_name))

salary = 2300
tv_price = 1999.90 

print(type(salary)) #int
print(type(tv_price)) #float
print(type(cars)) #list

numbers =[23,1,5,98,2]

#Descending order
numbers.sort(reverse=True)
print(numbers)

#Ascending order
numbers.sort()
print(numbers)

#---------------------------------QUESTION 2--------------------------------------#

# Write a program in Python to print the sum of all numbers found in an array.
numarray = [1,2,3,4,5]
totalvalue = 0
for x in numarray:
    totalvalue = (totalvalue + x)
print(totalvalue)


#---------------------------------QUESTION 3 --------------------------------------#
# Write a program in Python to do math functions.
import math #The math is the module consisting math functions

value = 2.15 #it is a float data type variable

print(math.floor(value)) #minimum integer value = floor
print(math.ceil(value)) #the next highest integer value

#---------------------------------QUESTION 4 --------------------------------------#
# Write a program in Python to search for a string in another string.

course_name = "PYTHON PROGRAMMING LANGUAGE"
string_to_be_searched = 'PY'
index_position = 0
is_found = False #initialised the statement to false, if found then turn true
index_position = course_name.find(string_to_be_searched)
if index_position > 0:
    is_found = True 
    print('The string is found in the '+str(index_position))
elif index_position < 0 :
    print("String is not found")

print(string_to_be_searched in course_name)

#or

print("MINg" in "PYTHON PROGRAMMING LANGUAGE")

#or

print(course_name.find(string_to_be_searched))

#---------------------------------QUESTION 5 --------------------------------------#
# Write a program in Python to convert a string into upper-case and into lower-case.

course_name ="PYTHON PROGRAMMINg LANGUAGE"
print("Print the course name in upper case: " +course_name.upper())
print("Print the course name in lower case: " +course_name.lower())
print(course_name.replace('g','G'))
print(course_name.replace('LANGUAGE','IS ONE OF THE BEST PROGRAMMING LANGUAGES'))

#---------------------------------QUESTION 5 --------------------------------------#
# Write a program in Python to practise if-else condition.

com = input("Please enter your salary: ")
salary = int(com)

if salary >= 0 and salary<=1000:
    print ("grade A")
elif salary >=1001 and salary <=2000:
    print ("grade B")
elif salary >=2001 and salary<=3000:
    print ("grade C")
elif salary >=3001 and salary<=5000:
    print("grade D")
elif salary >=5001 and salary<= 10000:
    print("grade E")
elif salary >=10001 and salary <=15000:
    print("grade G")
elif salary >=15001 and salary <=20000:
    print("H grade")
else:
    print("Grade J")
    print ("Your salary range: salary > 20000")

#--------------------------------QUESTION 7---------------------
a = 10
b = 10.5
num_list = [23,41,14,16,50]

print(type(a))
print(type(b))
print(type(num_list))

print(num_list[0])
print("Number of elements found in the list: "+str(len(num_list)))
print("Highest value found in the list: "+str(max(num_list)))
print("Lowest value found in the list: "+str(min(num_list)))
