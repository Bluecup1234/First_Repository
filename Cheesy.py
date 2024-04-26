import rabdom


name = "Big Cheesy"
age = 15
amount = 30000
print ("""Your name is {}, 
You are {} years old, 
Your balance is ${}, 
Thank you {}
Date:{}""".format(name, age + 3, amount * 3, name, datetime.now()))

name = "Big Cheesy"
age = 15
amount = 350000
timer = int(input("Enter the timer in seconds: "))
number = random.randint(1000, 1000000)
my_list = ['gum gum', 'glint glint', 'fire fire', 'chily chily']
item = random.choice(my_list)
name = "Big Cheesy"
age = 15
amount = 350000
print ("""Your name is {}, 
You are {} years old, 
Your balance is ${}, 
Thank you {}

Date:{}""".format(name, age + 3, amount * 3, name, datetime.now()))
time.sleep(timer)
print("You just won a sum of ${:,}".format(number))
print(f"You also won a {item}")
