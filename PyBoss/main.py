# Tameka Kuar
# Date: 06/06/20
# Purpose: To write a script that exports a csv file 
# with the data in the new format

# Modules
import os
import csv
import operator

# Set path for csv file
employee_path = os.path.join("Resources", "employee_data.csv")

# List to store data
emp_id = []
name = []
dob = []
ssn = []
state = []

# A dictionary whose keys are the state names and values are the abbreviations
# Code taken from the link provided
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Open and read employee_data.csv
with open(employee_path) as original_file:

    original_reader = csv.reader(original_file, delimiter=",")
    orginial_header = next(original_file)

    # Loop to fill the lists with data
    for row in original_reader:

        emp_id.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])

# Splits the employees' names creating a list of the empolyees' name
# in place of the original string name
new_name = [i.split(' ') for i in name]

# Splits the numbers in the DOBand puts those numbers in to a lsit 
# in place of the original string of numbers
new_dob = [i.split('-') for i in dob]

# Splits the number in the SSN and puts those numbers in to a lsit 
# in place of the original string of numbers
new_ssn = [i.split('-') for i in ssn]


# Puts the first and last names of the employees into their own lists
first_name = [fn[:][0] for fn in new_name]
last_name = [ln[:][1] for ln in new_name]

# List to store state abbreviations
state_abbrev = []
# Loop to get the abbreviations for each state in the state list
# and put in the state_abbrev list
for item in state:
    if item in us_state_abbrev:
        state_abbrev.append(us_state_abbrev[item])

# New list that reorganizes the DOBs in the sublist to the MM/DD/YYYY order
org_new_dob = list(map(operator.itemgetter(1,2,0), new_dob))
# List that actually has the DOBs in the MM/DD/YYYY format
dob_with_backslash = ['/'.join(sublist) for sublist in org_new_dob]

# List that has the last four digits of employees' SSN
last_four_digits = [''.join(sublist[:][:][2]) for sublist in new_ssn]
# List that has first five digits of the SSN hidden with visible last four digits
star_ssn = ['***-**-' + num for num in last_four_digits]

# Zips all six lists with employee data into tuples
updated_employee_data = zip(emp_id, first_name,last_name,dob_with_backslash,star_ssn,state_abbrev)

# Set variable for output file
output_path = os.path.join("output","new_employee_data.csv")

# Opens the output file, creates a header row, and then writes the zipped object to the csv
with open(output_path, "w") as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    
    for i in updated_employee_data:
        csvwriter.writerow(i)