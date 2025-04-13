def print_ones_digit(num):
    ones_digit = abs(num) % 10  # abs use kiya negative numbers handle karne ke liye
    print(f"The ones digit is {ones_digit}")

def main():
    try:
        user_input = int(input("Enter a number: "))
        print_ones_digit(user_input)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
