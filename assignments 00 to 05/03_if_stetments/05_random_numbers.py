
import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
   for _ in range(10):
    number = random.randint(1, 100)
    print(number, end=' ')

if __name__ == '__main__':
    main()