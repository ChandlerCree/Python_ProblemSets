import math

print("\nPS1 Question 1 (David Chandler Cree)")

a = int(input("please enter the length of side a: "))
b = int(input("please enter the length of side b: "))
c = int(input("please enter the length of side c: "))

s = 0.5*(a + b + c)

print("s: ", s)

print("calculating area...")

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("area of triangle: ", area)

