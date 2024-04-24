import time











# Python Data Types/ Converters

# # String      str()
# "Hello" 'Somethings about to happen.' "I can feel it"

# # Integers    int()
# 245, 8, -3, 0, 43

# # Floats     float()
# 64.74, 0.556654, 56.7776

# # Booleans   bool()
# True, False

# x = 556
# x = str(x)
# print(type(x))

# x = '556'
# x = int(x)
# print(type(x))

# x = 7
# x = float(x)
# print(type(x),x)

# x = bool('GG')
# print(type(x), x)




# OPERATORS
# Arithmetic operators
#Addition +
# print(4 + 7)

# #Subtraction -
# print(10-4)

# #Multiplication *
# print(4 * 5)

# #Division / // %
# print('Normal Division',10 / 3)
# print('Floor Division',10 // 3)
# print('Modulus',10 % 3)

# #Exponentiation **
# print(10 ** 2)

#Parenthisis ()
#Order of Operations
# P ()
# E **
# M *
# D / // %
# A +
# S -
# x = 54 * 5 / (7 - 8) + 8 ** 2
# print(x)


# Logical operators
# and

# or

# not

# eq1 and eq2 == ans
# subscribed = True
# print(not subscribed)



# Comparison/ Boolean operators
# Greater than                   >
# Less than                      <
# Greater than or Equal to       >=
# Less than or Equal to          <=
# Equal to                       ==
# Not Equal to                   !=

# print(4 + 5 != 9)



# Assignment operators
# =


# Variables
# number = 69
# name = 'Zarbon'
# height = 7.2
# is_horny = True

# print(name, number, height, is_horny)

# number = 50
# name = 'Rooney'
# height = 5.9
# is_active = True

# print(name, number, height, is_active)
# ans = number * 2
# print(ans)


# Assignment
# years = 1095.75
# seconds = 86400
# print(years * seconds)








# account = 1000
# amount = float(input("How much do you want to Deposit? "))
# new_account = account + amount
# print("Your current balance is: $"+str(new_account))











# String Formating
# f string format
#f""

# format method
# .format()


# f"" method
# name = "Giga Chad"
# age = 30
# amount = 650000

# print(f"Your name is {name}, Your are {age + 3} years old, Your balance is ${amount * 3}")



# .format() method
# name = "Big Cheesy"
# age = 15
# amount = 30000
# print ("""Your name is {}, 
# You are {} years old, 
# Your balance is ${}, 
# Thank you {}
# Date:{}""".format(name, age + 3, amount * 3, name, datetime.now()))

# name = "Big Cheesy"
# age = 15
# amount = 350000
# timer = int(input("Enter the timer in seconds: "))
# number = random.randint(1000, 1000000)
# my_list = ['gum gum', 'glint glint', 'fire fire', 'chily chily']
# item = random.choice(my_list)
# name = "Big Cheesy"
# age = 15
# amount = 350000
# print ("""Your name is {}, 
# You are {} years old, 
# Your balance is ${}, 
# Thank you {}

# Date:{}""".format(name, age + 3, amount * 3, name, datetime.now()))
# time.sleep(timer)
# print("You just won a sum of ${:,}".format(number))
# print(f"You also won a {item}")


# Assignment
# name = "Nero"
# age = 24
# amount = 50
# time = int(input("Enter the timer in seconds: "))
# number = random.randint(10, 1000)
# my_list = ['red queen', 'blue rose', 'yellow jacket', 'black rope']
# item = random.choice(my_list)
# print("""Your name is {},
# You are {} years old,
# Your new balance is ${}, 
# Date: {}""".format(name, age, number + amount, datetime.now()))
# print("You just won a sum of ${:,}".format(number))
# print(f"You also won a {item}")
# print("Thank you for playing")

#print(type(number))

# Data Type Converters
# str()
# int()
# float()
# bool()

# print("Hello world!")
# # Zarbon stop humping the couch.
# print("Zarbon")
# print(46 + 25 - 8 / 4)


# Control Flow
 #if, else, elif

# .method() .append(item)

# response = input("Do you want to start the code? (y/n )")
 
# if response .lower() == "y":
#     print(68 + 54 * 3)
          
# elif response.lower() == "n":
#     print("Thanks for using my code.")
    
# else:
#     print("Invalid input, try again!!")    
    
  

# password = 1234567

# pin =int( input("Enter your password: "))

# if pin == password:
#     print("Access Granted")
    
# else:
#     print("Access Denied")
    
# print("password", type(password))
# print("pin", type(pin))        


# amount = float(input("How much do you want to stake: "))

# winning_number1 = 14
# winning_number2 = 3
# winning_number3 = 10
# winning_number4 = 20
# winning_number5 = 16

# un1 = int(input("Pick a number btw 1 - 20: "))
# amount1 = float(input("How much do you want to stake for 1: "))
# un2 = int(input("Pick another number btw 1 - 20: "))
# amount2 = float(input("How much do you want to stake for 2: "))
# un3 = int(input("Pick another number btw 1 - 20: "))
# amount3 = float(input("How much do you want to stake for 3: "))
# un4 = int(input("Pick another number btw 1 - 20: "))
# amount4 = float(input("How much do you want to stake for 4: "))
# un5 = int(input("Pick another number btw 1 - 20: "))
# amount5 = float(input("How much do you want to stake for 5: "))

# for num in win_num_list:
#     if un1 == num:
#     new_amount = amount1 * num
#     print(f"You won a sum of ${new_amount}")
# else:
#     print(f"User1 You lost a sum of ${amount1}")    
    
# elif un2 == winning_number2:
#     new_amount = amount2 * winning_number2
#     print(f"You won a sum of ${new_amount}") 

# elif un3 == winning_number3:
#     new_amount = amount3 * winning_number3
#     print(f"You won a sum of ${new_amount}") 

# elif un4 == winning_number4:
#     new_amount = amount4 * winning_number4
#     print(f"You won a sum of ${new_amount}") 

# elif un5 == winning_number5:
#     new_amount = amount5 * winning_number5
#     print(f"You won a sum of ${new_amount}") 

# else:
#     print(f"You lost ${sum([amount1, amount2, amount3, amount4, amount5])}!")
    
# print("winning_number1", winning_number1)
# print("winning_number2", winning_number2)
# print("winning_number3", winning_number3)
# print("winning_number4", winning_number4)
# print("winning_number5", winning_number5)


# numbers_to_guess = [random.randint(1, 10) for num in range(5)]

# print("Welcome to the Game! Try to pick a number between 1 and 10.")

# amount_staked = int(input("Enter the amount you want to stake: "))

# guessed_numbers = []

# for num in range(5):
#     guessed_numbers.append(int(input("Enter the number between 1 and 10: ")))
    
# matches = 0

# for guessed_num in guessed_numbers:
#     if guessed_num in numbers_to_guess:
#         matches += 1
        
# if matches > 0:
#     print(f"Congratulations! You Matched{matches} number(s). You win {amount_staked * matches}!")
    
# else:
#     print("Sorry, you didn't match any numbers. Better luck next time")    








# Python Data Structure:
# List
# Dictionaries
# Tuples
# Sets


# List

my_list = [1, 2, 3, 4]

word_list = ['Get', 'bag', 'cap', 'run']
#              0      1      2      3

x = word_list[2]
#print(x)

color = "Red"
xb = [234, 'hello', True, 3.234, color, (1, 2, 3, 4)]


# Methods in Python List

# .append ()

my_list = [1, 2, 3, 4]
my_list.append('gooby')

#print(my_list)

# .extend() very important for data analysis

x = [1, 2, 3, 4]

y = [5, 6, 7, 8]

x.extend(y)

#print(x)

# .insert()

x = [1, 2, 3, 4]

x.insert(1, 5)

#print(x)

# .remove()

x = [1, 2, 3, 2, 4]

x.remove(2)

#print(x)

# .pop()

x = [1, 2, 3, 4]

num = x.pop(3)

#print(x)
#print(num)

# .index()

x = ['a', 'b', 'c', 'd', 'e', 'f' ]

position = x.index('d')

#print(position)

# .count()

x = ['a', 'b', 'c', 'd', 'e', 'f']

num =x.count('d')

#print(num)

# .sort()

x = [64, 25, 77, 88, 20, 55, 90]

x.sort()

#print(x)



# .reverse()

x = [87, 36, 86, 55, 100, 34, 97, 167]

x.reverse()

#print(x)


# .copy()

x = [35, 67, 77, 23, 98, 28, 64]

y = x.copy()

#print("y", y)
#print("x", x)







# Dictionaries

# word : "meaning"

# x = {"key" : "value",
# "key" : "value",
# "key" : "value",
# "key" : "value"}


# var = {"key" : "value"}


# Car Model Dictionary

car = dict()

#print(car)

car["name"] = "Toyota"
car["Brand"] = "Corola"
car["Type"] = "SE"
car["Engine type"] = "6 Plug"
# car["Price"] = "N{:,}".format(4000000)
car["Price"] = 4000000

#print(car.items())

car["Price"] = "N{:,}".format(car["Price"] + 1500000)
car["Type"] = "XLE"

#print(car.items())

#print("N{:,}".format(car["Price"]))


# Assignment

Name = "The students name is Tony"
Age = "He is 16 years old"
Gender = "He is a Male"
Class = "His class is Year 4"

# print(Name, Age, Gender, Class)

student = dict()

student["Name"] = "The students name is Tony"
student["Age"] = "He is 16 years old"
student["Gender"]= "He is a Male"
student["Class"] = "His class is Year 4"

# print(student.items())









# name = input("Enter your name: ")
# age = int(input("How old are you: "))
# Class = input("What class are you: ")
# gender = input("What gender are you: ")

name = "Perry"
age = 25
Class = "Firts Class"
gender = "Male"

student = dict()

student["name"] = name
student["age"] = age
student["Class"] = Class
student["gender"] = gender

# print(student.items())

# for key, values in student.items():
    # print({key:values})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# Bank Statement
bankname = "First Bank"
account_no = 3234586543
balance = 4500.86
account_name = "John Doe"

bankDB = dict()

user1 = dict()
user1["bankname"] = bankname
user1["account_name"] = account_name
user1["balance"] = balance
user1["account_no"] = account_no

# Add individual details to the account
user2 = dict()
user2["bankname"] = "Union Bank"
user2["account_name"] = "Carmen Sandi"
user2["balance"] = 534600.67
user2["account_no"] = 2345678932

# Add individual details to the account
user3 = dict()
user3["bankname"] = "Sterling Bank"
user3["account_name"] = "Jerry Lawler"
user3["balance"] = 456789.23
user3["account_no"] = 5672346781

# Add individual details to the account
user4 = dict()
user4["bankname"] = "GTBank"
user4["account_name"] = "Dong Zhong"
user4["balance"] = 4345.32
user4["account_no"] = 4357894321

# Add Individual details to the account
user5 = dict()
user5["bankname"] = "Wema Bank"
user5["account_name"] = "Terry Vader"
user5["balance"] = 132000.34
user5["account_no"] = 2045678763

# Add account details to the main dict bankDB
bankDB["user1"] = user1
bankDB["user2"] = user2
bankDB["user3"] = user3
bankDB["user4"] = user4
bankDB["user5"] = user5

# List out the total account details in each account

# for key, val in bankDB.items():
#     print({key: val})
    

# for key, val in bankDB.items():
#     for item, sub in val.items():
#         print({key: {item: sub}})
    
# Automating the bankDB
while True:
    try:
        print("Welcome to the Space Jam")
        # Retrive account from bankDB
        accountNumber = int(input("Enter your account number: "))
        
    # search the bank database to verify if account exits
        for user, details in bankDB.items():
            if details['account_no'] == accountNumber:
                found_account = details
                print(found_account.items())
                break
            
            else:
                continue
                
        if found_account:
                
            response = int(input("""
                press 1 to Deposit
                press 2 to Withdraw
                press 3 to View Account details
                press 4 to Exit
            """))

            if response == 1:
                deposit = float(input("How much do you want to Deposit: "))
                found_account['balance'] += deposit
                print(f"Your account has been Credited with N{deposit:,}".format(deposit=deposit))
                print(f"Your current balance is N{found_account['balance']:,}".format(found_account['balance']))

            elif response == 2:
                # withdraw from account
                    withdraw = float(input("How much do you want to Withdraw: "))
                    found_account['balance'] -= withdraw
                    print(f"Your account has been Debited with N{withdraw:,}".format(withdraw=withdraw))
                    print(f"Your current balance is N{found_account['balance']:,}".format(found_account['balance']))

            elif response == 3:
            # view account details
                for key, val in found_account.items():
                    print({key: val})
                    
            elif response == 4:
                print("Thanks for comimg to slam.")
                print("Leaving the jam....")
                time.sleep(3)
                break            
        
    except:
        print("Could not slam, Error")
        continue        

    # for user, details in bankDB.items():
    #     if details['account_no'] == accountNumber:
    #         found_account = details
    #         print(found_account.items())
    #         break

    # view account details 
    # if found_account:
    #     deposit = float(input("How much do you want to Deposit: "))
    #     found_account['balance'] += deposit
    #     print(f"Your account has been Credited with N{deposit:,}".format(deposit=deposit))
    #     print(f"Your current balance is N{found_account['balance']:,}".format(found_account['balance']))

    # if found_account:
    #     withdraw = float(input("How much do you want to Withdraw: "))
    #     found_account['balance'] -= withdraw
    #     print(f"Your account has been Debited with N{withdraw:,}".format(withdraw=withdraw))
    #     print(f"Your current balance is N{found_account['balance']:,}".format(found_account['balance']))


