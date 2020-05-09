num_1 = float(input('Please enter the first number: '))
num_2 = float(input('Please enter the second number: '))

def add(num_1,num2):
    addition = num_1 + num_2
    print('Addition of numbers: ',format(addition,'.3f'))

def sub(num_1,num2):
    substraction = num_1 - num_2
    print('Substraction of numbers: ',format(substraction,'0.3f'))

def multi(num_1,num_2):
    multiply = num_1*num_2
    print('Multiplication of two numbers:',format(multiply,'0.3f'))

def divd(num_1,num_2):
    divide = num_1/num_2
    print('Division of two numbers: ',format(divide,'0.3f'))

def powr(num_1,num_2):
    power = num_1**num_2
    print('to the power: ',format(power,'0.3f'))

print("1,Addition")
print("2,Substraction")
print("3,Multiplication")
print("4,Division")
print("5,Raising a power to number")


choice = int(input("Enter the selected number: "))

if choice == 1:
    add(num_1,num_2)

elif choice == 2:
    sub(num_1,num_2)

elif choice == 3:
    multi(num_1,num_2)

elif choice == 4:
    divid(num_1,num_2)

elif choice == 5:
    powr(num_1,num_2)
else:
    print('Enter Valid input')
