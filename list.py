
# Today answer is :


nums = [5, 50, 15]







mportant Concepts:
1️⃣ Lists Are Ordered

Each element has an index (starting from 0).

names = ["Ali", "John", "Sara"]
print(names[0])


Output:

Ali

2️⃣ Lists Are Mutable (Very Important)

Unlike strings, lists can be changed.

numbers = [10, 20, 30]
numbers[0] = 100
print(numbers)


Output:

[100, 20, 30]

3️⃣ Lists Can Store Different Data Types
data = ["Ali", 20, 3.5, True]


Python allows mixed data types inside a list.

4️⃣ Adding Items to a List
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)


Output:

[1, 2, 3, 4]











# Practice 
#  make list  from empty list 
fruits = []

f1=input("enter fruit name: ")

fruits.append(f1)
f2=input("enter fruit name: ")

fruits.append(f2)
f3=input("enter fruit name: ")

fruits.append(f3)
f4=input("enter fruit name: ")

fruits.append(f4)
f5=input("enter fruit name: ")

fruits.append(f5)


print(fruits)




# list methods 
friends=["apple",1234565,False,"Rohan"]
print(friends)
friends.append("Harry") # append method insert karta ha list ky end parh
print(friends)

li = [1,21,22,78,9,5]
li.sort() #sorted the numbers in list 
li.reverse() # reverse the numbers without sorted in  list 
li.insert(3,4444) # 3 index , object 4444 add element in list
li.pop(3) # remove item at index 3 
li.remove(78) # remove particular element
print(li.pop(3)) # print a given index

value = li.pop(3)
print(value)
print(li)

friends=["apple",1234565,False,"Rohan"]
print(friends[0])
friends[0] = "Graphs" #unlike strings, lists are mutuable

print(friends[0])
print(friends)
#slicing
print(friends[1:4])

# questions 

movies=[]
enter_movies1=input("enter favourite movies : ")
enter_movies2=input("enter favourite movies : ")
movies=[enter_movies1,enter_movies2]
print(movies)
# good way 


# # # Create an empty list
# # favorite_movies = []

# # # Ask user to enter 3 movie names
# # for i in range(3):
# #     movie = input(f"Enter favorite movie {i+1}: ")
# #     favorite_movies.append(movie)

# # # Display the list
# # print("Your favorite movies are:", favorite_movies)



# # WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method

# start = input("enter elements seprated by spaces ").split()

# list_copy=start.copy()

# list_copy.reverse()

# if start == list:
#     print(" palindrome")
# else:
#     print("not  palindrome")

A= ( "A","B","A","C")
print(A.count("A"))
print(A)
    
list_convert = list(A)

list_convert.sort()
print(list_convert)

