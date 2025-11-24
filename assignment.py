# Exercise 1
def second_last_digit_is_5(n):
    n = abs(n)
    s = str(n)

    if len(s) < 2:
        return False

    # find second last using loop
    for i in range(len(s)):
        if i == len(s) - 2:
            return s[i] == "5"


# Exercise 2
def is_prime(n):
    if n <= 1:
        return False

    # loop through possible divisors
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# Exercise 3
def count_ending_with_5(numbers):
    count = 0

    for num in numbers:
        s = str(abs(num))
        if s.endswith("5"):
            count += 1

    return count


# Exercise 4
def calculate_balance(input_file, output_file):
    balance = 0

    # read file line by line
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if line:  # skip empty lines
                balance += int(line)

    # write output
    with open(output_file, "w") as f:
        f.write(f"Final Balance: {balance}")


# Exercise 5
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, amount):
        # increase step-by-step using loop
        for _ in range(amount):
            if self.speed < 200:
                self.speed += 1

    def brake(self, amount):
        # decrease step-by-step using loop
        for _ in range(amount):
            if self.speed > 0:
                self.speed -= 1

    def get_status(self):
        return f"{self.brand} {self.model} — Speed: {self.speed} km/h"
