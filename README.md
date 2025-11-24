# Python Exam

---

## Exercise 1

**Problem:**

Input a number and check whether it is prime using a loop.

**Example:**

    Input: 7  
    Output: True
    
    Input: 12  
    Output: False
    
    Input: 1  
    Output: False

---

## Exercise 2

**Problem:**

Count how many numbers end with 5 from a given list.

**Example:**

    Input: [5, 15, 23, 25, 40]  
    Output: 3
    
    Input: [1, 2, 3, 4, 6]  
    Output: 0


---

## Exercise 3

**Problem:**

Each line in transactions.txt contains a transaction amount:

    +200
    -50
    +100
    -30

Write a program that:  
-Reads all transactions from transactions.txt  
-Calculates the final balance  
-Writes the result to summary.txt like this:  

    Final Balance: 220

    
---

## Exercise 4

**Problem:**

Create a class called Car that simulates a car accelerating and braking.  

Each Car object must have:  
-brand (string)  
-model (string)  
-speed (starts at 0)  

Methods:

accelerate(amount):  
-Increase speed by amount  
-Maximum speed is 200  
-If above 200 → set to 200 

brake(amount):  
-Decrease speed by amount  
-Minimum speed is 0  

get_status():  
-Return string like:  
-"Toyota Supra — Speed: 120 km/h"  

**Example:**

    Input:
        car1 = Car("Toyota", "Supra")
        car1.accelerate(50)
        car1.accelerate(90)
        car1.brake(30)
        
        print(car1.get_status())

    Output:
        Toyota Supra — Speed: 110 km/h
    
---
