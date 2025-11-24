# Exercise 1
def second_last_digit_is_5(n):
    # Write your code here
    num = abs(num)

    # convert to string so we can loop through characters
    s = str(num)

    if len(s) < 2:
        return False

    # loop to find second last character
    for i in range(len(s)):
        if i == len(s) - 2:     # second last position
            return s[i] == '5'
    pass

# Exercise 2
def is_prime(n):
    # Write your code here
    if n <= 1:
        return False

    # check divisors from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True
    pass

# Exercise 3
def count_ending_with_5(n):
    # Write your code here
    count = 0

    for n in numbers:
        s = str(abs(n))     # use loop with string
        if s[-1] == '5':
            count += 1

    return count
    pass

# Exercise 4
def calculate_balance(input_file,output_file):
    # Write your code here
    balance = 0

    # read file using loop
    with open("transactions.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                balance += int(line)

    # write result
    with open("summary.txt", "w") as f:
        f.write(f"Final Balance: {balance}")
    pass
    
# Exercise 5
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, amount):
        for _ in range(amount):
            if self.speed < 200:
                self.speed += 1

    def brake(self, amount):
        for _ in range(amount):
            if self.speed > 0:
                self.speed -= 1

    def get_status(self):
        return f"{self.brand} {self.model} — Speed: {self.speed} km/h"
    pass
