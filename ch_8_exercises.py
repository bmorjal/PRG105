"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 8.1 Basic string Operation
print("=" * 10, "Section 8.1 string operations", "=" * 10)
# 1) Print all the characters from the name variable by accessing one character at a time
name = "John Jacob Jingleheimer Schmidt"
i = 0
while i < len(name):
    print(name[i])
    i += 1

# 2) Use the index value to access and print the capital s in Schmidt from the variable name
length = len(name)
print(length)
print(name[24:25])
# 3) Use a negative index value to print the letters from the last name "Schmidt" in name
print(name[-7:])

# TODO 8.2 String slicing
print("=" * 10, "Section 8.2 string slicing", "=" * 10)
# 1) Use string slicing to assign the middle name "Jacob" from name to the variable middle, replace the ""
# 2) Print middle
middle = name[5:10]
print(middle)


# TODO 8.3 Testing, Searching, and manipulating strings
print("=" * 10, "Section 8.3 manipulating strings", "=" * 10)
# 1) Test to see if the string "Jacob" is in name, print the result
j = name.find('Jacob')
if j > 0:
    print('yes')
print(j)
# 2) Test to see if the string "Michael" is in name, print the result
m = name.find('Michael')
if m > 0:
    print('yes')
else:
    print('no')
print(m)
# 3) Test to see if name contains a number, print the result
n = name.find('1')
if n > 0:
    print('yes')
else:
    print('no')
print(n)
# 4) Test to see if number contains a number, print the result
number = "42"
z = number.find('42')
print(z)

# 5) Search for "J" in name, replace with "j" (lower case), print the result
#    Note: You can assign this to a variable first, or just print
c = name.replace("J", "j")
print(c)


# 6) Split the string name into the variable name_list, replace the "", print the result
name_list = name.split(",")
print(name_list)
