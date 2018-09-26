# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

s = input('Enter strings...')
i = 0
result = ''
temp = ''
while i < len(s):
    if len(temp) > 0:
        if s[i] >= temp[-1]:
            temp += s[i]
            msg = 'temp: ' + temp
        elif len(temp) > len(result):
            result = temp
            temp = s[i]
            msg = 'result: ' + result
        else:
            temp = s[i]
    else:
        temp = s[i]
    i += 1
if len(result) < len(temp):
    print(temp)
else:
    print(result)
    