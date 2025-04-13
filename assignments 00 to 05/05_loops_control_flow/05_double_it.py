def main():
    # User se number lena
    curr_value = int(input("Enter a number: "))

# Jab tak value 100 se chhoti hai, loop chale
    while curr_value < 100:
        curr_value:str = curr_value * 2
        print(curr_value, end=' ')


if __name__ == '__main__':
    main()