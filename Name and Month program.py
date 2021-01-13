name = input('What is your name ')
while not name:
    print('Please enter your name ')
    name = input('What is your name ')

# Create a list of the months 
months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# asking the user with validation about the month they were born
month_born = input('What month were you born? ')    
if month_born not in months:
    print('Please enter your birth month spelt correctly')
    month_born = input('What month were you born?')

#Printing the name
print(f'Hello {name}')

#Printing the happy birthday message

if month_born == 'August':
    print('Happy Birthday Month')

name_length = len(name)
print(f'Your name is {name_length} letters long')



# Here is the same program but with functions

from datetime import datetime

def main():
    nname = input('What is your name? ')
    birth_month = input('What is your birth month? ')
    length_of_name = get_length(nname)
    current_month = get_current_month
    if comapre_case_insensitive(birth_month, current_month):
        print('Happy birthday month')
    print(f'Hello {nname}')
    print(f'The length of your name is {length_of_name}')
    

def get_current_month():
    today = datetime.today()
    month_text = today.strftime('%B')
    return month_text

def comapre_case_insensitive(st1, st2):
    return st1.lower() == st2.lower()

def get_length(st1):
    return len(st1)

#Make sure to call the main function
main()            