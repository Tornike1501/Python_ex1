# დავალება 1
inputs = []
for i in range(5):
	inputs.append(input("input string: "))
print ("lentght of longest string is "+str(len(max(inputs, key=len))))

# დავალება 2
numbers = [5,7,10,15,-5,-11,-25,-30]
print (max(numbers))

# დავალება 3
x= int(input("Factorial of: "))
def factorial(x):
    if x<=1:
        return 1
    else:
        return x* factorial(x-1)
print (factorial(x))
