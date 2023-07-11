# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2
lower_name = name.lower()

t = lower_name.count('t')
r = lower_name.count('r')
u = lower_name.count('u')
e = lower_name.count('e')

l = lower_name.count('l')
o = lower_name.count('o')
v = lower_name.count('v')
e = lower_name.count('e')

a = str(t+r+u+e)
b = str(l+o+v+e)
c = int(a + b)

if c < 10 or c > 90:
    print(f"Your score is {c}, you go together like coke and mentos.")
elif c > 40 and c < 50:
    print(f"Your score is {c}, you are alright together.")
else:
    print(f"Your score is {c}.")