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

#(15)


#(150)Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values.
