MAX_LENGTH = 3

def shorten(lst):
    # While the list is longer than the MAX_LENGTH, remove the last item
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Removes and returns the last item
        print(removed_item)

def main():
    # Sample list passed into shorten function
    sample_list = ["apple", "banana", "cherry", "date", "elderberry"]
    
    shorten(sample_list)
    print("Final list:", sample_list)

# Call the main function to execute
main()
