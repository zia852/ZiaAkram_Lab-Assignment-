#1 Simple Countdown
count = 10
while count >= 1:
    print(count)
    count -= 1
print("Loop complete!")
#2 Even Numbers Only
num = 2
while num <= 20:
    print(num)
    num += 2
#3 Sum of First N Natural Numbers
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum of first", n, "natural numbers is:", sum)
#4 Basic Input Validation
number = -1
while number <= 0:
    number = int(input("Enter a positive number: "))
print("Thank you!")
#5. Print Characters of a String
s = "Data"
i = 0
while i < len(s):
    print(s[i])
    i += 1
#6 Password Retry System
correct_password = "analytics123"
password = ""

while password != correct_password:
    password = input("Enter password: ")
print("Access granted.")
#7 Guess the Number Game
secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the number: "))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
print("Correct! You guessed the number.")
#8 Count Digits in a Number
number = int(input("Enter a positive integer: "))
count = 0

if number == 0:
    count = 1  
else:
    while number > 0:
        number //= 10
        count += 1

print("Number of digits:", count)
#9 Multiplication Table Generator
num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
#10 Average Until Sentinel Value
total = 0
count = 0
num = int(input("Enter a number (-1 to stop): "))

while num != -1:
    total += num
    count += 1
    num = int(input("Enter a number (-1 to stop): "))

if count > 0:
    average = total / count
    print("Average of entered numbers:", average)
else:
    print("No valid numbers entered.")