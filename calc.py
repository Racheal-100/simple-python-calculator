number1 = int(input("Enter number one: "))
sign = input("enter sign ")
number2 = int(input("enter number two: ")) # int convert the input from string to interger value

if sign == "+" :
     answer = number1 + number2
     print(answer)

elif sign == "-" :
     answer = number1 - number2
     print(answer)

elif sign == "/" :
     answer = (number1 / number2)
     print(answer)

elif sign == "*" :
     answer = number1 * number2
     print(answer)

else:
     print(" enter a valid operator or sign next time")