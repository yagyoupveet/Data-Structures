def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)  
 
num = int(input("Enter a number: "))  

if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num))

def factorial(n):

	fact = 1
	for i in range(1, n + 1):
		fact = fact * i

	return fact


if __name__ == '_main_':
    print("The Factorial of", n, "is", factorial(n))

#using iteration
def fact(number):
   
    fact = 1
  
    for number in range(5, 1,-1):
    
        fact = fact * number
    return fact

number = int(input("Enter a number for iteration : "))

factorial = fact(number)
print("Factorial is "+str(factorial))