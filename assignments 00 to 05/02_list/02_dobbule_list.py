

list_of_numbers = [10,20,30,40,50]

def double_numbers():
    for i in range(len(list_of_numbers)):
        results : int = list_of_numbers[i] * 2
        print(results)

double_numbers()