# Given a string consisting of words separated by spaces. Determine how many
# words it has. To solve the problem, use the method count.
a=list(input("Enter your string:"))
b=a[0]
d=a[-1]
c=a.count(" ")
if b==" " and d==" ":
	print("In this string " + str(c-1) +" words")
elif d==" ":
	print("In this string " + str(c) +" words")
elif b==" ":
	print("In this string " +str(c) +"words")
else:
	print("In this string " + str(c+1)+"words")	
