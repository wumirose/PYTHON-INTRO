#This module has 3 functions and one dictionary

#Dictionary of a persons' name, age and state
person = {
            "name": "John",
            "age": 36,
            "country": "Norway"
          } 

#Functions to add arbitrary length of numbers
def adder1(*numbers):
    print("sum = ", sum(numbers))

#Functions to multiply arbitrary length of numbers
def Mul(*numbers):
    product = 1
    for i in numbers:
        product*=i
    print("Multiplied = ", product)

#Functions to print that module has ended
def done():
    print("You have reach the end of this module")