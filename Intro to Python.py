print('Hello Capstone!')

# Variables do not need to be consise

school = 'MCTC'
gpa = 3.7
students_in_class = 22


# if-statements

if gpa == 4:
    print('WOW! nice GPA')
elif gpa > 3:
    print('Awesome GPA')   
else:
    print('Cool')


# Lists

schools = ['MCTC', 'DCTC', 'North Hennepin Technical College']

# Check if things are in a list

if 'MCTC' in schools:
    print('MCTC is one of the schools in the list')
#sorts and prints the list 

schools.sort()
print(schools)
#adds in something to a list

schools.append('Century College')
print(schools)
# Reverses the list and prints it

schools.reverse
print(schools)

#Strings 

class_name = 'Software Development Capstone'
# making the string upper case

print(class_name.upper())
# finding the length of the string

print(len(class_name))
# breaks the string up into mutliple strings

print(class_name.split())
# breaks up the string on every letter o

print(class_name.split('o'))

if "Capstone" in class_name:
    print('This class must be the capstone')

#Loops - for loops over range

for x in range(10):
    print(x)

# Loops - for loops over sequence

# prints all the schools in our list in uppercase

for s in schools:
    print(s.upper())
# prints all letters in our variable school

for letter in school:
    print(letter)
    
# prints each letter 10 times

for letter in school:
    print(letter * 10)
#makes a new list with 10 0's in it

data = [0] * 10
print(data)
#making a list of 10 things not being used yet

more_data = [None] * 10
print(more_data)

# While Loops

# name = input('Enter your name')

# #while name does not have input ask again

# while len(name) == 0:
#     print('Please enter at least one character')
#     name = input('Enter your name: ')
# # This can also be written like this

# while not name:
#     print('Please enter at least one character')
#     name = input('Enter your name: ')

# True and False and None
    

start_of_semester = True
winter = False

if winter:
    print('Brr!')
else:
    print('it is not winter')    

# Dictionaries
 
class_code = {2905: 'Capstone', 2560: 'Web', 2545: 'Java'}

#this will print web
print(class_code[2560])

for code in class_code:
    #prints just the code

    print(code)
    #prints the value for the code

    print(class_code[code])

# This prints a good format for printing the items in the dictionary 

for code, name in class_code.items():
    print('The class code is ' + str(code) + ' and the name is ' + name)
# This will print it better with string formatting

for code, name in class_code.items():
    print(f'The class code is {code}  and the name is {name}')

# Sclicing strings, lists

schools = ['MCTC', 'DCTC', 'North Hennepin Technical College']

#This will print the first two schools

first_two = schools[0:2]
print(first_two)

#This will print the last school in the list
last_school = schools[-1]
print(last_school)

#This will print the last two schools

last_two_schools = schools[-2:]
print(last_two_schools)


#This will slice the string to just give us minneapolis
school_name = 'Minneapolis Community and Techinical College'
city = school_name[:11]
print(city)


# File input and output

#Writing data to a file
with open('data.txt', 'w') as f:
    f.writelines('schools \n homework \n food')

# Reading from a file
with open('data.txt') as f:
    print(f.read())

# Functions

def get_name():
    print('Hello please enter your name!')
    name = input('Your name is: ')
    return name

name = get_name()   

print(name)