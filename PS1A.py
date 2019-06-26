1200#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:33:53 2019

@author: max
"""

# PS1A
#
# Portion of cost for down payment = portion_down_payment = 0.25
# Money saved so far = current_savings = 0
# Annual return on savings = r = 0.04
# Annual salary = annual_salary
# Money saved each month = portion_saved
# Cost of dream house = total_cost
# Monthly salary = annual_salary/12 = monthly_salary
# Increase per month = current_savings*r/12
# Increase of savings each month = monthly salary + savings including return
# Total time = months
#
# Task: Calculate how many months it takes to save up for your dream home.
#
# Define variables that exist at beginning
portion_down_payment = 0.25
current_savings = 0
r = 0.04
# Ask user to enter annual salary
annual_salary = int(input("Please enter your annual salary: "))
# Ask user to enter portion of salary saved
portion_saved = float(input("Please enter the portion of your salary you whish to save as a decimal: "))
# Ask user to enter cost of dream home
total_cost = int(input("Please enter the cost of your dream home: "))
# Calculate monthly salary, monthly savings, monthly rate and down payment
monthly_salary = annual_salary/12
monthly_savings = monthly_salary*portion_saved
rmonth = r/12
down_payment  = total_cost*portion_down_payment
#
months = 0
while (current_savings <= down_payment):
    current_savings = (monthly_savings+current_savings)+(monthly_savings+current_savings)*rmonth
    months = months+1
print ("Number of months:",months)