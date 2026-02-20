# # Today answer
3



# Important Concepts:

#  Sets Do Not Allow Duplicate Values
# data = {1, 2, 2, 3}
# print(data)

# Output:

# {1, 2, 3}

# Duplicate values are automatically removed.

#  Sets Are Unordered

# You cannot access elements using index.

# This will give an error:

# numbers = {10, 20, 30}
# print(numbers[0])

# Sets do not support indexing.

#   Sets Are Mutable (But Elements Must Be Immutable)

# You can add or remove items:

# numbers = {1, 2, 3}
# numbers.add(4)
# numbers.remove(2)
# print(numbers)
# 4 Empty Set Warning
# empty = {}

# This creates a dictionary, not a set.

# Correct way:

# empty = set()



# Common Beginner Mistakes:


# Confusing {} with dictionary

# Trying to access elements using index
#  Forgetting that sets remove duplicates

# s = {10, 20, 30 , "rafay"}

# # empty = set() # empty set create 
# # donot repeat because of donot print repeat value only one time print donot ordered 
# print(s, type(s))

# s.add(556)
# print(s)
# s.remove(20)
# # sets are unindex donot index get
# print(s)


# s1 = {1,32,11}
# s2 = {1,32,12}
# print(s1-s2)# return 11 because of 11 in set 1 not 2 

# s1={1,45,6}
# s2={7,8,1,78}
# print(s1.union(s2))   # print all s1 and s2 sequence wise numbers donot repeat same numbers 
# print(s2.intersection(s1)) # print only common numbers in s2



# # excersize how to create a set 

# # we use sets for uniques values because in sets donot have repeat value 
# subjects = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]
# unique_subjects = set(subjects)
# classrooms_needed = len(unique_subjects)
# print("Classrooms needed:", classrooms_needed)

# s = set()
# n=input("enter the number")
# s.add(int(n))
# n=input("enter the number")
# s.add(int(n))
# n=input("enter the number")
# s.add(int(n))
# n=input("enter the number")
# s.add(int(n))
# print(s)




# # check 
# a=set([18 , "18"])
# print(a )
# print(type(a))
