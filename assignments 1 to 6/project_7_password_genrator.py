import random 
import string

def generated_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter The Length Of Your Desired Password :"))

password = generated_password(length)
print("Your Desired Generated Password : ",password)