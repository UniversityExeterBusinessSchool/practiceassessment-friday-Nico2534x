#######################################################################################################################################################
# 
# Name:Nihal Sabu
# SID:750031979
# Exam Date:28/03/2025
# Module:BEMM458_J_2_202425
# Github link for this assignment:https://github.com/UniversityExeterBusinessSchool/practiceassessment-friday-Nico2534x.git  
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Data Processing and Loops
# You are given a string representing customer reviews. Use a for loop to process the text and count occurrences of specific keywords.
# Your allocated keywords are determined by the first and last digit of your SID.
# Count and store occurrences of each keyword in a dictionary called keyword_counts.
 
customer_reviews = """The product is well-designed and user-friendly. However, I experienced some issues with durability. The customer service was helpful, 
but I expected a faster response. The quality of the materials used is excellent. Overall, the purchase was satisfactory."""

# Keywords dictionary
keywords = {
    0: 'user-friendly',
    1: 'helpful',
    2: 'durability',
    3: 'response',
    4: 'satisfactory',
    5: 'quality',
    6: 'service',
    7: 'issues',
    8: 'purchase',
    9: 'materials'
}

# Write your code to process the text and count keyword occurrences

#My SID is 750031979 therefore the first digit is 7 and last digit is 9 
first_digit = 7
last_digit = 9

keyword_to_count_1 = keywords[first_digit]
keyword_to_count_2 = keywords[last_digit]

#set a keyword dictionary to store values 

keywords_count = {
    keyword_to_count_1 : 0,
    keyword_to_count_2 : 0
}

# convert reviews to a lowercase to reduce case sensitivity 
reviews_lower = customer_reviews.lower()

#split the customer reviews 
words = reviews_lower.split()

#count word occurences of each keyword
for word in words :
    #remove punctuations 
    clean_word = word.strip(".,!?")
    if clean_word == keyword_to_count_1:
        keywords_count[keyword_to_count_1]
    if keyword_to_count_2 == keyword_to_count_2:
        keywords_count[keyword_to_count_2]

print(keywords_count)

##{'issues': 0, 'materials': 0}



##########################################################################################################################################################

# Question 2 - Business Metrics
# Scenario - You work in an online retail company as a business analyst. Your manager wants weekly reports on financial performance, including:
# Gross Profit Margin, Inventory Turnover, Customer Retention Rate (CRR), and Break-even Analysis. Implement Python functions 
# that take relevant values as inputs and return the computed metric. Use the first two and last two digits of your ID number as input values.

# Insert first two digits of ID number here:75
# Insert last two digits of ID number here:79

# Write your function for Gross Profit Margin
def gross_profit_margin(revenue, cogs):
    return ((revenue - cogs) / revenue) * 100
# Write your function for Inventory Turnover
def inventory_turnover(cogs, avg_inventory):
    return cogs / avg_inventory

# Write your function for Customer Retention Rate (CRR)
def customer_retention_rate(customers_start, customers_end, new_customers):
    return ((customers_end - new_customers) / customers_start) * 100
# Write your function for Break-even Analysis
def break_even_analysis(fixed_costs, selling_price, variable_cost):
    return fixed_costs / (selling_price - variable_cost)
# Call your functions here

# Inputs (using SID digits)
revenue = 75_000    # First two digits (75) scaled for realism
cogs = 79_000       # Last two digits (79) scaled (hypothetical, since COGS > Revenue is unusual)
avg_inventory = 15_000
customers_start = 75
customers_end = 100
new_customers = 25
fixed_costs = 75_000
selling_price = 79
variable_cost = 30

# Compute metrics
gpm = gross_profit_margin(revenue, cogs)
inv_turnover = inventory_turnover(cogs, avg_inventory)
crr = customer_retention_rate(customers_start, customers_end, new_customers)
break_even = break_even_analysis(fixed_costs, selling_price, variable_cost)

# Print results
print(f"Gross Profit Margin: {gpm:.2f}%")
print(f"Inventory Turnover: {inv_turnover:.2f}")
print(f"Customer Retention Rate: {crr:.2f}%")
print(f"Break-even Units: {break_even:.2f}")
##########################################################################################################################################################





"""
# Question 3 - Forecasting and Regression
# A logistics company has gathered data on delivery costs and shipment volumes. The table below provides different costs and their corresponding shipment volumes.
# Develop a linear regression model and determine:
# 1. The optimal delivery cost that maximizes profit
# 2. The expected shipment volume when the cost is set at £68


Delivery Cost (£)    Shipment Volume (Units)
-------------------------------------------
25                  500
30                  480
35                  450
40                  420
45                  400
50                  370
55                  340
60                  310
65                  290
70                  250
"""

# Write your regression model code here

##########################################################################################################################################################
"""
# Question 4 - Debugging and Data Visualization

import rand as random
import matplotlib.pyplt as plt

# Generate 100 random numbers between 1 and student ID number
your_ID=input("Enter your Student ID: ")
max_value = int(your_ID)
random_numbers = [random.randint(your_ID, max_valu) in range(100)]

# Plotting the numbers in a histogram
plt.histogram(random_number, bin=10, edgecolour='blue', alpha=0.7, colour='red')
plt.title="Histogram of 100 Random Numbers"
plt.xlabel="Value Range"
plt.ylabel="Frequency"
plt.grid("True")
plt.show("plot")

"""