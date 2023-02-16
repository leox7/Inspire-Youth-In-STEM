number=10
if (number%2 ==0):
    print("even number")
else:
    print("odd number")





#write a program to list all even numbers from 1-100
for even_numbers in range(1, 101):
    if even_numbers % 2 == 0:
        print(even_numbers)


#write a program to list all odd numbers from 1-100
        for odd_numbers in range(1, 101):
            if odd_numbers % 2 != 0:
                 print(odd_numbers)
                 


                 # calculate the arithmetic progression of numbers from 1 to 20

# set the starting number
start = 1

# set the common difference
diff = 1

# calculate the terms of the arithmetic progression
for i in range(0,100):
    term = start + i*diff
    print(term)


    

