def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def menu():
    print("\n=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == "1":
        temp = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")
    elif choice == "2":
        temp = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")
    elif choice == "3":
        temp = float(input("Enter temperature in Celsius: "))
        result = celsius_to_kelvin(temp)
        print(f"{temp}°C = {result:.2f}K")
    elif choice == "4":
        temp = float(input("Enter temperature in Kelvin: "))
        result = kelvin_to_celsius(temp)
        print(f"{temp}K = {result:.2f}°C")
    elif choice == "5":
        temp = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F = {result:.2f}K")
    elif choice == "6":
        temp = float(input("Enter temperature in Kelvin: "))
        result = kelvin_to_fahrenheit(temp)
        print(f"{temp}K = {result:.2f}°F")
    elif choice == "7":
        print("Thank you for using the converter. Goodbye!")
        return False
    else:
        print("Invalid choice. Please try again.")
    
    return True

while True:
    if not menu():
        break