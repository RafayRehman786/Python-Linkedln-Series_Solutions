'''
Important Concepts:


1  Dictionaries Store Data in KeyValue Format
student = {"name": "Ali", "age": 20}
print(student["name"])


Output:

Ali


We access values using their keys.

2  Dictionaries Are Mutable

We can change, add, or remove values.

student["age"] = 21
student["city"] = "Lahore"
print(student)

3  Keys Must Be Unique

 This is wrong:

data = {"name": "Ali", "name": "Ahmed"}


The second value will overwrite the first one.

4 Useful Dictionary Methods
student.keys()     # returns all keys
student.values()   # returns all values
student.items()    # returns key-value pairs

5 Removing Items
student.pop("age")


'''

# Common Beginner Mistakes:

# Using list brackets [] instead of {}
# Forgetting quotes around string keys
# Trying to access a key that doesn’t exist
# Using duplicate keys








s = {} # empty dictionary make

marks = {
    "Harry":100,
    "rafay":100,
    "hammad" : 200
}
print(marks, type(marks))
# print(marks[0]) # create a error 

print(marks["rafay"])


# in  python list in also a list is valid but  dictionary is used list complexity and computional expensive . 
# mutuable 




#dictionary_methods.py

marks = {
    "Harry":100,
    "rafay":100,
    "hammad" : 200,
    0:"rafay"
} 
print(marks.items()) #return a list in brackets of each comma keys 
print(marks.keys()) #return keys  means left side of dictionary list
print(marks.values())  #retun values right side of list

marks.update({"Harry": 99 , "rafayur": 44})# dictionary update because of dictionary mutuable  if not include in dictionary then also add
print(marks)



print(marks.get(0)) # print NONE if element does not exist in dictionary
print(marks[0])  #return error if in list doesnot exist element 
# pop()
#  popitem()



# Excersize:

d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang}) # update method add
the element in dictionary

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})
 # value update when two keys are same then second key value return because of update but value are same ( value = right side)




print(d)

