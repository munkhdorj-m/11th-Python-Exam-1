# -------------------------
# Exercise 1
# -------------------------

def second_last_is_five(num):
    num = abs(num)
    s = str(num)

    if len(s) < 2:
        return False

    # loop to find the second last index
    for i in range(len(s)):
        if i == len(s) - 2:
            return s[i] == '5'


# -------------------------
# Exercise 2
# -------------------------

def is_prime(n):
    if n <= 1:
        return False

    # check divisors using loop
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# -------------------------
# Exercise 3
# -------------------------

def count_end_with_5(numbers):
    count = 0

    for n in numbers:
        s = str(abs(n))
        if s[-1] == '5':   # ends with 5
            count += 1

    return count


# -------------------------
# Exercise 4
# -------------------------

def calculate_balance():
    balance = 0

    # read file line by line (loop)
    with open("transactions.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:                # skip empty lines
                balance += int(line)

    # write result
    with open("summary.txt", "w") as f:
        f.write(f"Final Balance: {balance}")


# -------------------------
# Exercise 5 - Car Class
# -------------------------

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, amount):
        # use loop to increase speed step-by-step
        for _ in range(amount):
            if self.speed < 200:
                self.speed += 1

    def brake(self, amount):
        # use loop to decrease speed step-by-step
        for _ in range(amount):
            if self.speed > 0:
                self.speed -= 1

    def get_status(self):
        return f"{self.brand} {self.model} — Speed: {self.speed} km/h"
