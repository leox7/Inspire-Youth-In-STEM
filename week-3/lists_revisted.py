#!/usr/bin/env python3

#this is a single line comment
#python program to illustrate operators
#Name : Leon John 
#Email : leonjohn397@gmail.com
#Date ; 20th Feb 2023
#File :lists_revisted.py


myFavouritesFruits=["banana","apple","avocado","watermelon","orange"]
for fruit in myFavouritesFruits:
    print(fruit)
print(len(myFavouritesFruits))


friends=["mark","keith","michelle","shan"]
print(friends)
friends[0]= "mary"
print(friends)
print("----------------------------------------------")
new_friends = friends.copy()
print(new_friends)
new_friends.sort()
print(new_friends)


new_friends.pop()
print(new_friends)



#asignment
#listsofsports
#listoffavmusicians
#listofemptylistoffavmusicians
#addusingforloopaddfivemusicians
#copylisttoanewlists