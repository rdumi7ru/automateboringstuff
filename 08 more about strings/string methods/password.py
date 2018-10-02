# Define the function to check if the password contains minimum a number.
def num_there(num):
    return any(i.isdigit() for i in num)

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')


while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if num_there(password) != True:
        print('The password must contain a number\nThe authentication will exit!')
        break
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
