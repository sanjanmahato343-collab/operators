# Python Operators - Notes

# 1. Arithmetic Operators
# +  Addition
# -  Subtraction
# *  Multiplication
# /  Division
# %  Modulus (remainder)
# // Floor Division
# ** Exponentiation

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)


# 2. Comparison Operators
# == Equal to
# != Not equal to
# >  Greater than
# <  Less than
# >= Greater than or equal to
# <= Less than or equal to

print(a == b)
print(a != b)
print(a > b)
print(a < b)


# 3. Assignment Operators
# =, +=, -=, =, /=, %=, //=, *=

x = 10
x += 5
print(x)


# 4. Logical Operators
# and - True if both conditions are true
# or  - True if at least one condition is true
# not - Reverses the result

print(a > 5 and b < 5)
print(a > 5 or b > 5)
print(not(a > 5))


# 5. Membership Operators
# in     - Checks whether a value exists
# not in - Checks whether a value does not exist

numbers = [1, 2, 3, 4, 5]
print(3 in numbers)
print(10 not in numbers)


# 6. Identity Operators
# is     - Checks whether two objects are the same object
# is not - Checks whether two objects are different objects

x = [1, 2]
y = x

print(x is y)
print(x is not y)


# 7. Bitwise Operators
# &  AND
# |  OR
# ^  XOR
# ~  NOT
# << Left shift
# >> Right shift
