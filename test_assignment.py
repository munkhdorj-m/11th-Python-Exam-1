import pytest
import inspect
from pathlib import Path

from assignment import second_last_digit_is_5, is_prime, count_ending_with_5, calculate_balance, Car

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source
    
@pytest.mark.parametrize("num, expected", [
    (157, True),
    (432, False),
    (5, False),
    (1050, True),
    (99, False)
])
def test1(num, expected):
    assert second_last_digit_is_5(num) == expected
    
@pytest.mark.parametrize("n, expected", [
    (7, True),
    (12, False),
    (1, False),
    (2, True),
    (29, True),
    (30, False)
])

def test2(n, expected):
    assert is_prime(n) == expected
    assert check_contains_loop(is_prime)

@pytest.mark.parametrize(
    "transactions, expected_balance",
    [
        (
            "+200\n-50\n+100\n-30\n",
            "Final Balance: 220",
        ),
        (
            "+10\n+20\n+30\n",
            "Final Balance: 60",
        ),
        (
            "-5\n-15\n-10\n",
            "Final Balance: -30",
        ),
        (
            "",
            "Final Balance: 0",
        ),
    ],
)
def test3(tmp_path, transactions, expected_balance):
    input_file = tmp_path / "transactions.txt"
    output_file = tmp_path / "summary.txt"
    input_file.write_text(transactions)

    calculate_balance(input_file, output_file)
    result = output_file.read_text().strip()

    assert result == expected_balance

# ---------- Test Accelerate ----------
@pytest.mark.parametrize("brand, model, steps, expected_speed", [
    ("Toyota", "Supra", [50, 90], 140),
    ("BMW", "M5", [100, 200], 200),       # cannot exceed 200
    ("Honda", "Civic", [0, 0], 0),
])
def test4_1(brand, model, steps, expected_speed):
    car = Car(brand, model)
    for s in steps:
        car.accelerate(s)
    assert car.speed == expected_speed


# ---------- Test Brake ----------
@pytest.mark.parametrize("brand, model, accel, brake, expected_speed", [
    ("Toyota", "Supra", 100, 30, 70),
    ("Audi", "A6", 50, 100, 0),          # cannot go below 0
    ("Ford", "GT", 200, 200, 0),
])
def test4_2(brand, model, accel, brake, expected_speed):
    car = Car(brand, model)
    car.accelerate(accel)
    car.brake(brake)
    assert car.speed == expected_speed


# ---------- Test Status ----------
@pytest.mark.parametrize("brand, model, accel, brake, expected_status", [
    ("Toyota", "Supra", 50, 0, "Toyota Supra - Speed: 50 km/h"),
    ("Nissan", "GTR", 300, 50, "Nissan GTR - Speed: 150 km/h"),
    ("Ford", "Mustang", 0, 20, "Ford Mustang - Speed: 0 km/h"),
])
def test4_3(brand, model, accel, brake, expected_status):
    car = Car(brand, model)
    car.accelerate(accel)
    car.brake(brake)
    assert car.get_status() == expected_status
