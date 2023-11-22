#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Nov. 22, 2023
# This program will show you the conversation of Celsius to Fahrenheit.


def fahrenheit():
    user_temp = input("Enter the temperature (°C): ")
    try:
        user_temp = float(user_temp)
    except ValueError:
        print(f"{user_temp} is not an integer.")
    else:
        fahrenheit_convert = round((9 / 5) * user_temp + 32, 2)
        print(f"{user_temp}°C is equal to {fahrenheit_convert}°F")


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
