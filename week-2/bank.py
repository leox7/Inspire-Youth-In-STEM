#!/usr/bin/env python3

#this is a single line comment
#python program to illustrate operators
#Name : Leon John 
#Email : leonjohn397@gmail.com
#Date ; 17th Feb 2023
#File :bank.py


# write a program that calculates 16% tax on income ranging 100k- 150k
#19%vtax if income is between 150k-300k

#30% if income is above 300k

#5% if income is than 100k

#print gross income and net income 



gross_income=int(input("Enter your gross income:"))

#above 300k
if (gross_income>=300000):
    net_income= gross_income - ((30/100)*gross_income)
    print(" if your gross income is:{} your net income is{}".format(gross_income,int(net_income)))

#150k to less than 300k
if (gross_income>=150000) & (gross_income <300000):
    net_income=gross_income - ((19/100)*gross_income)
    print(" if your gross income is:{} your net income is{}".format(gross_income,int(net_income)))


if(gross_income >= 1) & (gross_income < 100000):
	net_income = gross_income - ((5/100)*gross_income)
	print(" if your gross income is:{} your net income is{}".format(gross_income,int(net_income)))
        









gross_income = int(input("Enter the gross income amount?"))
tax_group_a = gross_income * 0.05
tax_group_b = gross_income * 0.16
tax_group_c = gross_income * 0.19
tax_group_d = gross_income * 0.30

if (gross_income <= 100000):
    print("Gross Income:", gross_income)
    print("Net Income:", gross_income - tax_group_a)

elif (gross_income > 100000) & (gross_income < 150000):
    print("Gross Income:", gross_income)
    print("Net Income:", gross_income - tax_group_b)

elif (gross_income >= 150001) & (gross_income <= 300000):
    print("Gross Income:", gross_income)
    print("Net Income:", gross_income - tax_group_c)

else:
    print("Gross income",gross_income)
    print("Net income",gross_income - tax_group_d)



        
