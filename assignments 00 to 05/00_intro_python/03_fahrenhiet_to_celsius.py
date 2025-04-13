def fahrenheit_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  celsius = (fahrenheit - 32) * 5.0 / 9.0
  return celsius

def main():
  """Prompts the user for Fahrenheit and prints Celsius."""
  try:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"Temperature: {fahrenheit}F = {celsius}C")
  except ValueError:
    print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  main()