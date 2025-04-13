user_list = []

while True:
    value = input("Enter a value: ")
    
    # Check if the input is empty
    if value == "":
        break
    
    user_list.append(value)

print("Here's the list:", user_list)
