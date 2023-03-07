#block of code that are executed together
#function use def key word
def print_name():
    print("my name is leon")
    print("i am from nairobi")
    print("i love playing basketball")
    print("i am 18 years old")

    # evoking the function
print_name()

def add_number(num1, num2):
    sum_num= num1 + num2
    print(sum_num)

add_number(10,30)
add_number(50,60)
add_number(40,45)


def add_number(num1,num2):
    prod_num = num1 * num2
    print(prod_num)


add_number(10,40)
add_number(70,9)
add_number(3,4)



#assignment
#write a program to print factorial of a number using function
def factorial(n):
    for i in range (1,n):
        fact_n = n * i 
        print(fact_n)
factorial(3)








p=float(input("enter the principal amount:"))
r=float(input("enter the rate:"))
t=float(input("enter the duration:"))
simple_interest=int(p) * int(r) * int(t)/100
print(simple_interest)




