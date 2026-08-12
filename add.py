#write program to addition of two numbers
def add_numbers(num1, num2):
    return num1 + num2      
#need to passthe numbers to the function
number1 = float(input("Enter first number: "))          
number2 = float(input("Enter second number: "))         
result = add_numbers(number1, number2)                 
print(f"The sum of {number1} and {number2} is {result}") 
