#!/usr/bin/env python
# coding: utf-8

# ##### Project Final Submission Template

# ### Step 1a: Planning 
# #### Identify the information in the file your program will read
# 
# The following project will take input from *Motor Vehicle Fatalities* in BC, which will read:
# * The Year the data was taken 
# * Role of person involved (Cyclist, Car Driver, Car Passenger, Other or Pedestrian)
# * Number of Fatalities

# ### Step 1b: Planning 
# #### Write a description of what your program will produce
# 
# The program can produce the following 
# 
# * Line chart -> Produce trends to see which one has the highest average increase in fatalities over the 7 year * period
# 
# * Pie Chart -> The highest average percentage of fatalities across the 7 year period 
# 
# * Histogram -> Highest rate of death in 3 year blocks.
# 
# The following program will produce a pie chart that demonstrates the highest average percentage of fatalities per year across a period of time

# ### Step 1c: Planning 
# #### Write or draw examples of what your program will produce
# 
# You must include an image that shows what your chart or plot will look like. You can insert an image using the Insert Image command near the end of the Edit menu.
# #### plot_average_motor_vehicle_deaths_per_category('motor_vehicle_fatalities_per_role.csv', None)
# ![IMG_7EDFB02E40F4-1.jpeg](attachment:IMG_7EDFB02E40F4-1.jpeg)
# 
# 
# 

# ### Step 2a: Building
# #### Design data definitions
# 
# Double click this cell to edit.
# 
# Before you design data definitions in the code cell below, you must explicitly document here which information in the file you chose to represent and why that information is crucial to the chart or graph that you'll produce when you complete step 2c.

# In[16]:


from cs103 import *
from typing import NamedTuple, List
from enum import Enum 
import csv

##################
# Data Definitions

Roles = Enum('Roles', ['PEDESTRIAN', 'CAR_DRIVER', 'CAR_PASSENGER', 'CYCLIST', 'OTHER'])
#interp. the role of the person in an accident, either as a Pedestrian (PEDESTRIAN)
#person who drives a car (CAR DRIVER), passenger in a car (CAR PASSENGER), a cyclist 
#(CYCLIST) or a type that is not one of the 4 (OTHER). 
#examples are redundant for enumerations 
             
#template based on Enumeration (5 cases)
@typecheck 
def fn_for_roles (r: Roles) -> ...: 
    if r == Roles.PEDESTRIAN:
        return ...
    elif r == Roles.CAR_DRIVER:
        return ...
    elif r == Roles.CAR_PASSENGER: 
        return ...
    elif r == Roles.CYCLIST: 
        return ... 
    elif r == Roles.OTHER:
        return ...

Accident = NamedTuple('Accident', [('role', Roles), 
                                   ('fatalities', int)]) #in range [0, ...]
#interp. data about a role in an accident and the number of accidents  
#that have occured for it
A1 = Accident(Roles.PEDESTRIAN, 71)
A2 = Accident(Roles.CYCLIST, 39)
A3 = Accident(Roles.CAR_DRIVER, 23)
A4 = Accident(Roles.CAR_PASSENGER, 20)
A5 = Accident(Roles.OTHER, 12)
    
# template based on compound (2 fields) and reference rule (once)
@typecheck
def fn_for_accident(a: Accident) -> ...:
    return ...(fn_for_accident(a.role),
               a.fatalities)

#List[Accident]
#interp. a list of accidents
LOA0 = []
LOA1 = [A1]
LOA2 = [A1, A2, A3, A4, A5]

@typecheck
def fn_for_loa(loa: List[Accident]) -> ...:
    # template based on arbitary-sized data and reference rule 
    acc = ... #type: ...
    for a in loa:
        acc = ...(fn_for_accident(a), acc)
    return ... (acc)


# ### Step 2b and 2c: Building
# #### Design a function to read the information and store it as data in your program
# #### Design functions to analyze the data
# 
# 
# Complete these steps in the code cell below. You will likely want to rename the analyze function so that the function name describes what your analysis function does.

# In[17]:


###########
# Functions
import matplotlib.pyplot as plt
from cs103 import *
from typing import List

@typecheck
def plot_average_motor_vehicle_deaths_per_category(filename: str)-> None:
    """
    Reads the file from given filename, analyzes the data, returns the result 
    """
    # Template from HtDAP, based on function composition 
    #1. filter the data for each one
    #2. return sum of fatalties for each Role
    #3. determine the number of years 
    #4. divide the sum by number of years present to determine average for each Role 
    #5. Produce graph
    
    pedestrian = average_deaths_pedestrian(read(filename))
    driver = average_deaths_driver(read(filename))
    passenger = average_deaths_passenger(read(filename))
    cyclist = average_deaths_cyclist(read(filename))
    other = average_deaths_other(read(filename))
    
    labels = 'Pedestrian', 'Driver', 'Passenger', 'Cyclist', 'Other'
    num = [pedestrian, driver, passenger, cyclist, other]
    
    plt.pie(num, labels=labels , autopct='%.0f%%', shadow=False)
    plt.show()

@typecheck
def read(filename: str) -> List[Accident]:
    """    
    reads information from the specified file and returns a list of Accidents 
    """
    #return []  #stub
    # Template from HtDAP
    
    # loa contains the result so far
    loa = [] # type: List[Accident]

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:
            a = Accident(parse_roles(row[1]), parse_int(row[2]))
            loa.append(a)
    
    return loa

@typecheck
def read(filename: str) -> List[Accident]:
    """    
    reads information from the specified file and returns a list of Accidents 
    """
    #return []  #stub
    # Template from HtDAP
    
    # loa contains the result so far
    loa = [] # type: List[Accident]

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:
            a = Accident(parse_roles(row[1]), parse_int(row[2]))
            loa.append(a)
    
    return loa

@typecheck
def parse_roles(s: str) -> Roles:
    """
    Input a string that must be one of "Pedestrian", "Driver",
    "Passenger", or "Cyclist", returns the corresponding Roles
    """
    #return Roles.PEDESTRIAN  #stub
    #return ... (s) #template
   
    if s == "Pedestrian":
        return Roles.PEDESTRIAN
    elif s == "Car Driver":
        return Roles.CAR_DRIVER
    elif s == "Car Passenger":
        return Roles.CAR_PASSENGER
    elif s == "Cyclist":
        return Roles.CYCLIST 
    elif s == "Other":
        return Roles.OTHER

@typecheck
def sum_deaths(loa: List[Accident]) -> int:
    '''
    sum the amount of deaths for a given role, where all categories have to be present. 
    '''
    #return 0.0 #stub 
    
    acc = 0 #type: float
    for a in loa:
        acc = acc + a.fatalities
    return acc

@typecheck 
def number_of_years(loa: List[Accident]) -> float:
    '''
    determine the number of years present in a csv file, where all categories have to be present. 
    '''
    #return 0.0 #stub
    #Template based on List[Accident]
    
    # template based on arbitary-sized data and reference rule 
    acc = 0.0 #type: float
    for a in loa:
        acc = acc + 1 
    return acc/5   
    
@typecheck
def filter_deaths_pedestrian(loa: List[Accident]) -> List[Accident]:
    '''
    sums the number of fatalties for a given Role  
    '''
    #return 0 #stub
    #Template based on Accident
    
    # template based on arbitary-sized data  
    acc = [] #type: []
    for a in loa:
        if a.role == Roles.PEDESTRIAN:
            acc.append(a)
    return acc

@typecheck 
def average_deaths_pedestrian(loa: List[Accident]) -> float:
    '''
    determine the average deaths per year
    '''
    #return 0.0
    #Template based on List[Accident]
    
    return sum_deaths(filter_deaths_pedestrian(loa))/number_of_years(loa)

@typecheck
def filter_deaths_driver(loa: List[Accident]) -> List[Accident]:
    '''
    sums the number of fatalties for a given Role  
    '''
    #return 0 #stub
    #Template based on Accident
    
    # template based on arbitary-sized data  
    acc = [] #type: []
    for a in loa:
        if a.role == Roles.CAR_DRIVER:
            acc.append(a)
    return acc

@typecheck 
def average_deaths_driver(loa: List[Accident]) -> float:
    '''
    determine the average deaths per year
    '''
    #return 0.0
    #Template based on List[Accident]
    
    return sum_deaths(filter_deaths_driver(loa))/number_of_years(loa)

@typecheck
def filter_deaths_cyclist(loa: List[Accident]) -> List[Accident]:
    '''
    sums the number of fatalties for a given Role  
    '''
    #return 0 #stub
    #Template based on Accident
    
    # template based on arbitary-sized data  
    acc = [] #type: []
    for a in loa:
        if a.role == Roles.CYCLIST:
            acc.append(a)
    return acc

@typecheck 
def average_deaths_cyclist(loa: List[Accident]) -> float:
    '''
    determine the average deaths per year
    '''
    #return 0.0
    #Template based on List[Accident]
    
    return sum_deaths(filter_deaths_cyclist(loa))/number_of_years(loa)

@typecheck
def filter_deaths_passenger(loa: List[Accident]) -> List[Accident]:
    '''
    sums the number of fatalties for a given Role  
    '''
    #return 0 #stub
    #Template based on Accident
    
    # template based on arbitary-sized data  
    acc = [] #type: []
    for a in loa:
        if a.role == Roles.CAR_PASSENGER:
            acc.append(a)
    return acc

@typecheck 
def average_deaths_passenger(loa: List[Accident]) -> float:
    '''
    determine the average deaths per year
    '''
    #return 0.0
    #Template based on List[Accident]
    
    return sum_deaths(filter_deaths_passenger(loa))/number_of_years(loa)

@typecheck
def filter_deaths_other(loa: List[Accident]) -> List[Accident]:
    '''
    sums the number of fatalties for a given Role  
    '''
    #return 0 #stub
    #Template based on Accident
    
    # template based on arbitary-sized data  
    acc = [] #type: []
    for a in loa:
        if a.role == Roles.OTHER:
            acc.append(a)
    return acc


@typecheck 
def average_deaths_other(loa: List[Accident]) -> float:
    '''
    determine the average deaths per year
    '''
    #return 0.0
    #Template based on List[Accident]
    
    return sum_deaths(filter_deaths_other(loa))/number_of_years(loa)

# Begin testing
start_testing()

# Examples and tests for read
expect(read('blank.csv'), [])
expect(read('test_1.csv'),[A1])
expect(read('test_1.csv'),LOA1)
expect(read('test_2.csv'),LOA2)

#examples and tests for parse_roles
expect(parse_roles("Pedestrian"), Roles.PEDESTRIAN)
expect(parse_roles("Car Driver"), Roles.CAR_DRIVER)
expect(parse_roles("Car Passenger"), Roles.CAR_PASSENGER)
expect(parse_roles("Cyclist"), Roles.CYCLIST)
expect(parse_roles("Other"), Roles.OTHER)

#examples and tests sum_deaths 
expect(sum_deaths(LOA2), 165)

#examples and test number_of_years
expect(number_of_years(LOA2), 1)

#examples and tests filter_deaths 
expect(filter_deaths_cyclist(LOA2), [A2])
expect(filter_deaths_pedestrian(LOA2), [A1])
expect(filter_deaths_other(LOA2), [A5])
expect(filter_deaths_passenger(LOA2), [A4])
expect(filter_deaths_driver(LOA2), [A3])

#examples and tests for average calculator for each Role 
expect(average_deaths_passenger(LOA2), 20.0)
expect(average_deaths_driver(LOA2), 23.0)
expect(average_deaths_other(LOA2), 12.0)
expect(average_deaths_cyclist(LOA2), 39.0)
expect(average_deaths_pedestrian(LOA2), 71.0)

#examples and tests for plot 
expect(plot_average_motor_vehicle_deaths_per_category('test_2.csv'), None)
expect(plot_average_motor_vehicle_deaths_per_category('motor_vehicle_fatalities_by_role.csv'), None)
expect(plot_average_motor_vehicle_deaths_per_category('test_1.csv'), None)

# show testing summary
summary()

