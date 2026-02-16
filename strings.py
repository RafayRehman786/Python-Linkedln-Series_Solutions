
# Today Answer 






'''
Important Concepts:

=> Strings are Ordered

Each character has a position (index).

name = "Ali"
print(name[0])  # A
print(name[1])  # l


Index always starts from 0.

=> Strings are Immutable

You cannot change a character directly.

❌ This will give an error:

name = "Ali"
name[0] = "B"


Strings cannot be modified after creation.

=> String Concatenation (Joining Strings)
first = "Ali"
last = "Khan"

print(first + " " + last)


Output:

Ali Khan

=> String Length
name = "Python"
print(len(name))


Output:

6

Real-Life Example:

Think of a string like a train 🚆

Each character is a compartment.

Each compartment has a position (index).

You can look at a specific compartment.

But you cannot change a compartment directly.

'''
# Slicing in Python 

name= "Computer"
nameshort = name[0:3] #start from 0  all till 2
print(name[-4:-1]) # start backword 
print(name[1:4]) # start  to 3 not 4 

print(name[:4]) # its print before the 4 
a="123456789"

print (a[1:7:3])

# this f allow us variable directly written in string
name = input("the name is :")
print(f"Good Afternoon,{name}" )

# or second method is 
print("good afternoon" , name)
 

# Program to find the occurrence of '$' in a string

# Input string from user
text = input("Enter a string: ")

# Count occurrences of '$'
count = text.count('$')

# Output result
print("The occurrence of '$' in the string is:", count)

# practices 


#  Convert to title case

sentence = "hello world"
print(sentence.title())  # Output: "Hello World"

#  Count words in sentence

sentence = "Hello World, this is Python."
print(len(sentence.split()))  # Output: 5

#  9. Replace word
sentence = "Hello World, World is beautiful."
old_word = "World"
new_word = "Python"
print(sentence.replace(old_word, new_word))  # Output: "Hello Python, Python is beautiful."


#  Check digits only

s = "12345"
print(s.isdigit())  # Output: True