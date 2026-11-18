#wap to check whether the given number is prime or not

number = int(input("enetr a number : "))

for i in range(2,number):

    if number % i == 0:

        print(f"the {number} is not prime")

        break

else:

    print(f"the {number} is prime")