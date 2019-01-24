def main():
    # problem1()
    # problem2()
    # problem3()
    problem4()

# Problem1
# Create a function in your program that counts from 0 to [NUMBER]

# def problem1():
#     numbers = int(input("Enter your favorite number: "))
#     loops(numbers)
# def loops(numbers):
#     for loops in range(0,numbers):
#         print(loops)
#

# Problem2
# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
#
# def problem2():
#    afterp = ""
#    while(afterp != 'q'):
#         afterp = input("Enter the alphabet.")

# Problem3
# Create 4 functions called add, subtract, multiply, and divide.
# Create them to allow a user to perform the name of the function to the two numbers and return the result.

# def problem3():
#     numnum1 = int(input("Type in a number "))
#     numnum2 = int(input("Again! "))
#     print(f"The sum of both numbers is equal to: {add(numnum1,numnum2)}")
#     print(f"The difference of both numbers is equal to: {subtract(numnum1,numnum2)}")
#     print(f"The product of both numbers is equal to: {multiply(numnum1,numnum2)}")
#     print(f"The quotient of both numbers is equal to: {divide(numnum1,numnum2)}")
#
# def add(numnum1, numnum2):
#     sumOfBothNums = numnum1 + numnum2
#     return  sumOfBothNums
#
# def subtract(numnum1, numnum2):
#     diffOfBothNums = numnum1 -numnum2
#     return diffOfBothNums
#
# def multiply(numnum1, numnum2):
#     prodOfBothNums = numnum1 * numnum2
#     return prodOfBothNums
#
# def divide( numnum1, numnum2):
#     quotOfBothNums = numnum1 // numnum2
#     return quotOfBothNums


# Problem4
# Create a function that will ask the user for a number.
# Use the function to get two numbers, then pass the two numbers to a function
# and ask a user if they want to add, subtract, multiple, or divide them.
# Return a string that prints the two numbers, which operation it did, and the result.

def problem4():
    numnum1 = int(input("Enter your favorite number "))
    numnum2 = int(input("Enter your second favorite number "))
    op = input("Enter one of the following operations: add, subtract, multiply or divide. ")
    print(Bartholomew(numnum1, numnum2, op))

def Bartholomew(numnum1,numnum2, op):
    if op == "add":
       return (f"{numnum1} + {numnum2} = {numnum1 + numnum2}")
    elif op == "subtract":
       return(f"{numnum1} - {numnum2} = {numnum1 - numnum2}")
    elif op == "multiply":
       return(f"{numnum1} * {numnum2} = {numnum1 * numnum2}")
    elif op == "divide":
       return(f"{numnum1} / {numnum2} = {numnum1 / numnum2}")





if __name__ == '__main__':
    main()
