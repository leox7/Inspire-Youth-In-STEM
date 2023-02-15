names=["leon","waweru","john","kamau","jay","shan"]
#accessing items in a list 
print(names)
print(names[0])
print(names[-1])
print(names[2])
print(names[0:3])
#create a list of fruits 
fruits = ["apple","watermelon","pear","banana","orange","kiwi","avocados"]
print(fruits)
print(fruits[3])
print("my favourite fruits is:",fruits[-1].upper())
#adding two lists
vegetables = ["kales","spinnach","cabbage","carrots","brocoli"]
stationary = ["pens","ruler","pencils","rubber","stapler"]
shoppings = (vegetables) + (stationary)
print(shoppings)
print(shoppings[5])
for vegetable in vegetables:
    print(vegetable)    
    for shopping in shoppings:
        print(shopping)
print("My name is:" + names[0] + "and my favourite fruit is:" + fruits[-1])        
