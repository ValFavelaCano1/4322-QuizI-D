"""
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
"""

import csv

# open the file

infile = open("employee_data.csv", "r")

employees = csv.reader(infile, delimiter=",")

next(employees)

# create an empty dictionary
Employee_List = {}

# use a loop to iterate through the csv file
for employee in employees:
    first_name = employee[1]
    last_name = employee[2]
    salary = employee[5]
    title = employee[4]
    department = employee[3]

    # check if the employee fits the search criteria
    if department == "Marketing":
        if title == "CSR":
            managers = first_name + " " + last_name
            Employee_List["Manager"] = managers
            Employee_List["Salary"] = salary
        print(Employee_List)

print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per printout
# for manager in Employee_List:
