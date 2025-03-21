#conditional statement

x = 10
if x > 11:
    print("True")
else:
    print("False")

#----------------------------------------

x = 10
if x > 11:
    print(x, "is greater than 11")
elif x < 11:
    print(x, "is less than 11")
else:
    print("something went wrong")

#----------------------------------------

x = 11
if x > 11:
    print(x, "is greater than 11")
elif x < 11:
    print(x, "is lesser than 11")
elif x == 11:
    print(x, "is equal to 11")
else:
    print("something went wrong")

#-------------------------------------

#control flow:
#loops 
#for:

for i in range(1, 11, 2):
    print(i)
print("------------------------------")

#--------------------------------------

#while:

x = 1
while x < 10:
    print(x)
    x = x + 1

print("-----------------------")


#------------------------------

#prime even numbers

for i in range(2, 21):
    if i % 2 == 0:
        print(i, end = " ")

print("\n-----------------------")

#------------------------------

#even, odd

even = []
odd = []

for i in range(1, 21):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

print("-----------------------------")

#--------------------------------

for i in "Nellore":
    print(i)

print("-----------------------")

#--------------------------------

city = "Nellore"
vowels = ['a', 'e', 'i', 'o', 'u']
c = 0
for i in city:
    if i in vowels:
        c += 1
print("No.of vowel letters in", city, "is", c)