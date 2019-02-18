# Simple prints

msg = "Hello world"
print(msg)

x = 1
if x == 1:
    print("1")
else:
    print("0")

print("Goodbye, world")
print("wow what a complex project")

## Variables and types
## Python is completely object oriented - we do not need to declare variables when we use them

myInt = 7
print(myInt)

myFloat = 8.5
print(myFloat)

myString = "hi this is v basic stuff but whatev"
print(myString)

## Simple operators, mixing operators is not supported e.g. one + two + string

one = 1
two = 2
three = one + two
print(three)

## Appending string

str1 = "hello"
str2 = "world"
fullstring = str1 + " " + str2
print(fullstring)

a, b = 3, 4
print(a, b)  # this prints 3 4

## Exercise

string = "hello"
floaty = 10.0
inty = 20

if string == "hello":
    print("String: %s" % string)
if isinstance(floaty, float) and floaty == 10.0:
    print("Float: %f" % floaty)
if isinstance(inty, int) and inty == 20:
    print("Integer: %d" % inty)

# Lists - similar to arrays, can contain any type of variable
prime = []
prime.append(2)
prime.append(3)
prime.append(5)
prime.append(7)

## prints my array of prime numbers
print(prime) 
## access 3rd element of prime array
print(prime[2]) 

## loop through my array and print out all the prime numbers
for number in prime:
    print(number)

seasons = []
seasons.append("winter")
seasons.append("spring")
seasons.append("summer")
seasons.append("autumn")

print("the 2nd season in my list is %s" % seasons[1])

# Basic operators 

## Arithmetic operators

number = 3 + 3 * 2 / 10
print(number) 

remainder = 11 % 3
print(remainder) # 2

### power relationship

squared = 7 ** 2
cubed = 7 ** 3
print(squared) # 49 
print(cubed) # 343

## Operators with strings

lotsofhellos = "hello" * 10
print(lotsofhellos) # prints hello 10 times

## Operators with lsits

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = even_numbers + odd_numbers
print(all_numbers) # concatenates the two

print(all_numbers * 2) # prints these 10 times

## Exercise - create two lists called x list and y list and contain 10 instances of the variables x and y, respectively

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list)) 
print("y_list contains %d objects" % len(y_list)) 
print("big_list contains %d objects" % len(big_list)) 

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("great!!")


array = [0,1,1,1,2,3,4]
occurences = array.count(1) # counts the number of times 1 appears in my list
print("occurrences of 1 is %d" % occurences)

total = len(array)
print("total number of numbers in my array is %d" % total)

# Conditions - Python uses boolean variables to evaluate conditions. Boolean values are returned when an expression is compared or evaluated

x = 2
print(x == 2) # prints true
print(x == 3) # prints false
print(x < 3) # prints true

name = "Jenny"
age = 23

if name == "Jenny" or age == 23:
    print("woo well done jen you know your name and age")
else:
    print("errrrrooor")

## the "in" operator
array = [1,3,5,7]
speshnumber = 5

if speshnumber in array:
    print("wow so spesh")

## when we use "is" - we are not matching the values of the variables, we are match the instances themselves

x = [1,2,3]
y = [1,2,3]
print(x == y) # prints true
print(x is y) # prints false

## using the "not" operator
print(not False) # prints true

## Exercise - changing the variables in the section so that each if statement resolves as true
exnumber = 16
exsecond_number = 10
exfirst_array = [1,2,3]
exsecond_array = [1,2]

if exnumber > 15:
    print("1")

if exfirst_array:
    print("2")

if len(exsecond_array) == 2:
    print("3")

if len(exfirst_array) + len(exsecond_array) == 5:
    print("4")

if exfirst_array and exfirst_array[0] == 1:
    print("5")