number_1= int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))
if number_1 > number_2:
    print("{} is greater than {}".format(number_1, number_2))
elif number_2 > number_1:
    print("{} is greater than {}".format(number_2, number_1))
if number_1 == number_2:
    print("The numbers are equal")
