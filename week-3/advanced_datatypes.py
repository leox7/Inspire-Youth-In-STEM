#advanced data types 
#mutable vs immutable
#mutable are data types that can be edited during program life cycle 
#add/remove elements 
#immutable cannot be edited during life cycle 

#1-LIST (mutable)
#2-TUPLES(immutable)
#3-dictionaries aka dict
#4-sets


friends = ["mark","anita","keith",'mary']


students = ["marie","micheal","mark","keith"]

friends.extend(students)
friends.append("carti")
friends.sort()
friends.reverse()



stationarys = ("pens","pencil","sharpener","ink")
# replaces the whole list
stationarys = ("ruler","colours","eraser")

for stationary in stationarys:
    print(stationarys)
    



    #dictionary uses key and value

student = {"name" : "leon","age" : 18 , "gender": "male","is tall": False}
print(student["name"])
print(student["age"])
print(student["gender"])
print(student["is tall"])
    
#"name":"leon"--> name(key)leon(value)    


#friends= fav-colorur,hobby,course,weight, height



friends = {"fav_colour": "blue" ,"hobby" : "playing basketball", "course" : "softwaredeveloper" , "weight": "60","height" : "160 cm"}
print(friends["fav_colour"])
print(friends["hobby"])
print(friends["course"])
print(friends["weight"])
print(friends["height"])

print(student.values())
print(student.keys())

