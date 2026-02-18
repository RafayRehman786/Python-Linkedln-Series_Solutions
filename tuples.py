
# # Answer is :

3





# Important Concepts:
# 1️⃣ Tuples Are Ordered

# Each element has an index starting from 0.

# names = ("Ali", "John", "Sara")
# print(names[1])


# Output:

# John

# #  Tuples Are Immutable 

# Unlike lists, tuples cannot be changed after creation.

# ❌ This will give an error:

# numbers = (10, 20, 30)
# numbers[0] = 100


# # Once created, tuple values cannot be modified.

# Tuples Can Store Different Data Types
# data = ("Ali", 20, 3.5, True)


# # Python allows mixed data types inside a tuple.

# Single Value Tuple

# To create a tuple with one value, you must add a comma:

# value = (5,)


# Without the comma, it is not a tuple.







# Common Beginner Mistakes:

# ❌ Trying to modify tuple values
# ❌ Forgetting comma in single-element tuple
# ❌ Confusing tuple () with list []







# #tuple  is immutable 
# a=(12,154,False,"rafay")

# # a[0]=51 # not change in tuple but create  a new tuple
# a=(1,2,5,4)
# print(type(a))
#  # empty tuple
# a=()
# print(type(a))

# # tuple in which only one element 
# a=(1 ,)
# print(type(a))




# a=(12,154,False,"rafay")
 
# print(a)
# no = a.count(12)# return the 12 how many times in tuple 
# print(no)

# a=(12,154,False,12,"rafay") #when we print index of element in tuple its only print
# # first index element not after the same element like 12
# i = a.index(12)
# print(i)
# print(len(a))# start 0

# #when slicing new tuple return 