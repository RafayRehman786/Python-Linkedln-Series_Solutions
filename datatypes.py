Today answer

Single-Line Comment:
Example 
# This program prints student name  

name = "Ali"
print(name)


Anything written after          #       becomes a single line  comment.

Multi-Line Comment (Using Triple Quotes):
Example 
"""
This program stores student data
and prints it on the screen
"""
name = "Ali"
print(name)

anything written after  '''     '''   becomes a multi line Comment


🏠 Real-Life Example:

Think of comments like sticky notes 📝 on your notebook.

The teacher reads them.
But the calculator ignores them.

Python also ignores comments when running the program

---------------------------------------------------------------------

Variable Naming Rules:

✔ A variable name must start with a letter or underscore _
✔ It cannot start with a number
✔ No spaces allowed
✔ Python is case-sensitive (age and Age are different)

Example:

name = "Ali"
_age = 20

Data Types in Python:

str → Text

int → Whole numbers

float → Decimal numbers

bool → True or False

Example:

name = "Ali"      # str
age = 20          # int
cgpa = 3.7        # float
is_student = True # bool



------------------------------------------------------------------------


#Sum of two numbers using vaiables , input function and data types 

a = int(input("enter number 1")) # tommarrow i discussed how to take input as interger number 
b = int(input("enter number 2"))
print("number a is: ",a)
print("number b is: ",b)
print("sum is" , a + b)

# datatypes ------------------------------



# data type typecasting 
a = "31.2"  # string type 
b = float(a) # a but the type should be float
t = type(b)  
c= complex(a) # complex type 
print(c)


exercises

Taking User Input and Printing it

# Take user name as input and print it
name = input("Enter your name: ")
print("Hello, " + name)



 Checking Data Type of a Variable

# Take a variable and check its data type
x = 5
print("Data type of x: ", type(x))

x = "hello"
print("Data type of x: ", type(x))

x = 3.14
print("Data type of x: ", type(x))

Converting Data Type

# Take a string input and convert it to integer
num = input("Enter a number: ")
num = int(num)
print("Number: ", num)
print("Data type: ", type(num))


