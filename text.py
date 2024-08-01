#(1)Write a Python program to print the following string in a specific format (see the output).Sample String : 
# "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. 
# Twinkle, twinkle, little star, How I wonder what you are"
print("""
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
    """)

#(2) Write a  Python program to find out what version of Python you are using.	
import platform
print(platform.python_version())

#(3)Write a Python program to display the current date and time.
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

#(4)Write a Python program that calculates the area of a circle based on the radius entered by the user.
from math import pi
r=float(input("Input the radius of the circle :"))
area=pi*r**2
print("The area of the circle with radius "+ str(r) + " is: " + str(area))

#(5)Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
fname=(input("input your first name: "))
lname=(input("input your last name: "))
print("ahlan "+lname+" "+fname)

#(6)Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
values = input("Input some comma-separated numbers: ")
list=values.split(",")
tuple=tuple(list)
print("list: ", list)
print("tuple: ",tuple)
#(7)Write a  Python program that accepts a filename from the user and prints the extension of the file.
filename=(input("input sample filed: "))
f_extension=filename.split(".")
print("the output filename: " +repr(f_extension[-1]) )
#(8)Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
print("%s    %s" %(color_list[0],color_list[-1]))
#(9)Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
print(" the  examination will start from: %i / %i/ %i" % exam_st_date)

#(10) Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
a=int(input("input an integer: "))

n1=int("%s" % a)
n2=int("%s%s" % (a,a))
n3=int("%s%s%s" % (a,a,a))
print( n1+ n2+ n3)

#(11) Write a  Python program to print the documents (syntax, description etc.) of Python built-in function(s).
print(abs.__doc__)

#(12)Write a Python program that prints the calendar for a given month and year.
import calendar
y=int(input("input the year: "))
m=int(input("input the month: "))
print( calendar.month(y, m))

#(13)Write a Python program to print the following 'here document'.
print(''' 
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
''')

#(14)Write a Python program to calculate the number of days between two dates.
from datetime import date
f_date=date(2014, 7, 8)
l_date=date(2014,7,15)
delattr=l_date-f_date
print(delattr.days)

#(15)Write a  Python program to get the volume of a sphere with radius six.
from math import pi
pi=22/7
r=6.0
v=4.0/3.0*pi*r**3
print("the volume of sphere: ",v)

#(16)Write a Python program to calculate the difference between a given number and 17.
# If the number is greater than 17, return twice the absolute difference.
def difference(n):
	if n <= 17:
		return 17 - n
	else:
		return(n-17)*2

print (difference(22))
print (difference(14))

#(17)Write a Python program to test whether a number is within 100 of 1000 or 2000.
def near_thousand(n):
	return((abs(1000-n)<=100)or (abs(2000-n)<=100))

print(near_thousand(800))

print(near_thousand(1000))

print(near_thousand(900))

print(near_thousand(1200))

#(18)Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

def sum_thrice(a,b,c):
	sum=a+b+c

	if a==b==c:

		sum=sum*3
	return(sum)

print(sum_thrice(1,2,3))

print(sum_thrice(3,3,3))

#(19) Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

def new_string(text):
	if len(text)>=2 and text[:2]=="Is":
		return text
	else:
		return "Is"+text
print(new_string("Array"))
print(new_string("IsEmpty"))
			
#(20)Write a  Python program that returns a string that is n (non-negative integer) copies of a given string.

def larger_string(text, n):
	result=" "
	
	for i in range(n):
		result= result +" " + text

	return result
print(larger_string('A_S',2))	

#(21)Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
num = int(input("input the number: "))
mod=num%2
if mod>0:
	print("the number is the odd")
else:
	print("the number is the even")	

#(22) Write a Python program to count the number 4 in a given list.
def list_count_4(nums):
	count=0
	for i in nums:
		 if i==4:
		  count=count+1
	return count	  

print(list_count_4([1,8,4,7,4]))			

#(23)Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2
def substring_copy(text, n):
	flen=2
	if flen> len(text):
		flen=len(text)
	substr=text[:flen]
	result=" "	
	for i in range(n):
		result=result+substr
	return result
print(substring_copy("asd",5))		


#(24)Write a Python program to test whether a passed letter is a vowel or not 
def is_vowel(char):
	all_vowels ='aeiou'
	return char in all_vowels
print(is_vowel('i')),print(is_vowel('s'))		


#(25)Write a  Python program that checks whether a specified value is contained within a group of values.
def is_group_numbers(groupdata, n):
	for value in groupdata:
		if n== value:
			return True
	return False
print(is_group_numbers([1,5,8,1,4],4))		

#(26)Write a Python program to create a histogram from a given list of integers.
def histogram(items):
	for n in items:
		output=' '
		items=n

		while items>0:
			output +='A'
			items=items-1
		print(output)
histogram([4,5,3,3,5,4])		



