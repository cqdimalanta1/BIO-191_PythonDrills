

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_first_n_primes(n):
    prime_count = 0
    num = 2
    while prime_count < n:
        if is_prime(num):
            print(num, end=" ")
            prime_count += 1
        num += 1

# Example usage:
n = int(input("Enter the value of n: "))
print("First", n, "prime numbers:")
print_first_n_primes(n)


def print_multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i*j, end=" ")
        print()

print_multiplication_table(10)

n = int(input("Enter the size of the square: "))

def filled_square(n):
    if n == 1:
        print('*')
    else:
        for i in range(n):
            print('*' * n, end=' ')
            print()

def hollow_square(n):
    if n == 1:
        print('*')
    else:
        print('*' * n)
        for i in range(n - 2):
            print('*' + ' ' * (n - 2) + '*')
        print('*' * n)

filled_square(n)
hollow_square(n)


side_length = int(input("Enter the side length of the diamond: "))


for i in range(1, side_length + 1):
    print(" " * (side_length - i) + "*" * (2 * i - 1))


for i in range(side_length - 1, 0, -1):
    print(" " * (side_length - i) + "*" * (2 * i - 1))


def main():
    age = int(input("How old are you? "))

    has_license = input("Do you have a fishing license? (yes/no): ").lower() == "yes"

    if age <= 15:
        parent_has_license = input("Does your parent have a fishing license? (yes/no): ").lower() == "yes"
        if parent_has_license:
            print("You are legally allowed to fish in Minnesota.")
        else:
            print("Sorry, you are not legally allowed to fish in Minnesota.")
    else:
        if has_license:
            print("You are legally allowed to fish in Minnesota.")
        else:
            print("Sorry, you are not legally allowed to fish in Minnesota.")


if __name__ == "__main__":
    main()


def main():
    eligible = True

    natural_born_citizen = input("Are you a natural born citizen of the United States? (yes/no): ").lower()
    age = int(input("What is your age? "))
    years_resident = int(input("How many years have you been a resident within the United States? "))

    if natural_born_citizen != "yes":
        eligible = False
    if age < 35:
        eligible = False
    if years_resident < 14:
        eligible = False


    if eligible:
        print("Congratulations! You are eligible to run for President of the United States.")
    else:
        print("Sorry, you are not eligible to run for President of the United States.")

if __name__ == "__main__":
    main()

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))


largest_odd = None


if num1 % 2 != 0:
    largest_odd = num1
elif num2 % 2 != 0 and (largest_odd is None or num2 > largest_odd):
    largest_odd = num2
elif num3 % 2 != 0 and (largest_odd is None or num3 > largest_odd):
    largest_odd = num3


if largest_odd is not None:
    print("The largest odd integer is:", largest_odd)
else:
    print("None of the integers are odd.")





