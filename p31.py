# Given a string consisting of words separated by spaces. Determine how many
# words it has. To solve the problem, use the method count.
string=list(input("Enter your string:")).strip()
a=string.count(" ")
print(a+1,' word(s)')
