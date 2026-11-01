import numpy as np


def cold(temp):
    if temp <= 15:
        return 1
    elif 15 < temp < 25:
        return (25 - temp) / 10
    else:
        return 0


def warm(temp):
    if temp <= 20 or temp >= 35:
        return 0
    elif 20 < temp < 27.5:
        return (temp - 20) / 7.5
    else:
        return (35 - temp) / 7.5


def hot(temp):
    if temp <= 30:
        return 0
    elif 30 < temp < 40:
        return (temp - 30) / 10
    else:
        return 1


def fuzzy_controller(temp):
    cold_value = cold(temp)
    warm_value = warm(temp)
    hot_value = hot(temp)

    # Fan speed values
    low_speed = 20
    medium_speed = 50
    high_speed = 100

    numerator = ((cold_value * low_speed) + (warm_value * medium_speed) + (hot_value * high_speed))
    denominator = cold_value + warm_value + hot_value

    if denominator == 0:
        fan_speed = 0
    else:
        fan_speed = numerator / denominator

    return cold_value, warm_value, hot_value, fan_speed


# User Input
temperature = float(input("Enter temperature (°C): "))
cold_value, warm_value, hot_value, fan_speed = fuzzy_controller(temperature)

print("\nFuzzy Values:")
print(f"Cold = {cold_value:.2f}")
print(f"Warm = {warm_value:.2f}")
print(f"Hot = {hot_value:.2f}")
print(f"\nFan Speed = {fan_speed:.2f}%")

if fan_speed < 35:
    print("Fan Status = LOW")
elif fan_speed < 70:
    print("Fan Status = MEDIUM")
else:
    print("Fan Status = HIGH")
