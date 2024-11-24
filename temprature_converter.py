def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32

def temperature_converter():
    print("Welcome to the Temperature Converter!")
    print("Available units: Celsius, Fahrenheit, Kelvin")
    print("Example input: 100 Celsius")

    while True:
        user_input = input("\nEnter temperature (or type 'exit' to quit): ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break

        try:
            temp_value, temp_unit = user_input.split()
            temp_value = float(temp_value)
        except ValueError:
            print("Invalid input. Please enter the temperature followed by the unit (e.g., '100 Celsius').")
            continue

        temp_unit = temp_unit.capitalize()
        if temp_unit not in ["Celsius", "Fahrenheit", "Kelvin"]:
            print("Invalid unit. Please use Celsius, Fahrenheit, or Kelvin.")
            continue

        if temp_unit == "Celsius":
            print(f"Celsius: {temp_value}")
            print(f"Fahrenheit: {celsius_to_fahrenheit(temp_value)}")
            print(f"Kelvin: {celsius_to_kelvin(temp_value)}")
        elif temp_unit == "Fahrenheit":
            print(f"Fahrenheit: {temp_value}")
            print(f"Celsius: {fahrenheit_to_celsius(temp_value)}")
            print(f"Kelvin: {fahrenheit_to_kelvin(temp_value)}")
        elif temp_unit == "Kelvin":
            print(f"Kelvin: {temp_value}")
            print(f"Celsius: {kelvin_to_celsius(temp_value)}")
            print(f"Fahrenheit: {kelvin_to_fahrenheit(temp_value)}")

if _name_ == "_main_":
    temperature_converter()
