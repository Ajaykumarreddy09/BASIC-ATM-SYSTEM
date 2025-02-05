#!/usr/bin/python
import getpass

# Creating lists of users, their PINs, and bank balances
users = ['user', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]

# Introduction
print('-------------------------------------')
print('***** WELCOME TO THE ATM SYSTEM *****')
print('-------------------------------------')

# User authentication
while True:
    print('\nPLEASE ENTER YOUR CREDENTIALS TO LOGIN')
    user = input('ENTER USERNAME: ')
    user = user.lower()

    if user in users:
        n = users.index(user)
        print('USERNAME ACCEPTED')
        print('-----------------------------')
        break
    else:
        print('-----------------------------')
        print('INVALID USERNAME. PLEASE TRY AGAIN.')
        print('-----------------------------')

# PIN validation (maximum 3 attempts)
attempts = 0
while attempts < 3:
    print('\nENTER YOUR PIN')
    pin = getpass.getpass('PIN: ')

    if pin == pins[n]:
        print('PIN ACCEPTED')
        print('-----------------------------')
        break
    else:
        attempts += 1
        print('-----------------------------')
        print(f'INVALID PIN ({3 - attempts} attempts left). PLEASE TRY AGAIN.')
        print('-----------------------------')

# If user exceeds PIN attempts
if attempts == 3:
    print('-----------------------------------')
    print('3 UNSUCCESSFUL ATTEMPTS. EXITING.')
    print('!!!!! YOUR CARD HAS BEEN LOCKED !!!!!')
    print('-----------------------------------')
    exit()

# Login successful
print('--------------------------------')
print(f'WELCOME {user.upper()} TO YOUR ATM ACCOUNT')
print('--------------------------------')

# ATM Menu Loop
while True:
    print('--------------------------------------')
    print('PLEASE SELECT AN OPTION:')
    print('1. View Balance (S)')
    print('2. Withdraw Money (W)')
    print('3. Deposit Money (L)')
    print('4. Change PIN (P)')
    print('5. Exit (Q)')
    print('--------------------------------------')

    response = input('YOUR CHOICE: ').lower()

    if response == 's':  # Balance Inquiry
        print('---------------------------------------------')
        print(f'YOUR CURRENT BALANCE IS: {amounts[n]} EURO')
        print('---------------------------------------------')

    elif response == 'w':  # Withdrawal
        print('---------------------------------------------')
        print('WITHDRAW MONEY')
        print('---------------------------------------------')

        try:
            cash_out = int(input('ENTER AMOUNT TO WITHDRAW: '))
            print('---------------------------------------------')

            if cash_out % 10 != 0:
                print('WITHDRAWAL AMOUNT MUST BE IN MULTIPLES OF 10')
            elif cash_out > amounts[n]:
                print('INSUFFICIENT FUNDS! TRANSACTION FAILED.')
            else:
                amounts[n] -= cash_out
                print('TRANSACTION SUCCESSFUL!')
                print(f'NEW BALANCE: {amounts[n]} EURO')

        except ValueError:
            print('INVALID INPUT! PLEASE ENTER A NUMERIC AMOUNT.')

    elif response == 'l':  # Deposit
        print('---------------------------------------------')
        print('DEPOSIT MONEY')
        print('---------------------------------------------')

        try:
            cash_in = int(input('ENTER AMOUNT TO DEPOSIT: '))
            print('---------------------------------------------')

            if cash_in % 10 != 0:
                print('DEPOSIT AMOUNT MUST BE IN MULTIPLES OF 10')
            else:
                amounts[n] += cash_in
                print('DEPOSIT SUCCESSFUL!')
                print(f'NEW BALANCE: {amounts[n]} EURO')

        except ValueError:
            print('INVALID INPUT! PLEASE ENTER A NUMERIC AMOUNT.')

    elif response == 'p':  # Change PIN
        print('---------------------------------------------')
        print('CHANGE PIN')
        print('---------------------------------------------')

        new_pin = getpass.getpass('ENTER A NEW PIN: ')
        print('---------------------------------------------')

        if new_pin.isdigit() and len(new_pin) == 4 and new_pin != pins[n]:
            confirm_pin = getpass.getpass('CONFIRM NEW PIN: ')
            print('---------------------------------------------')

            if confirm_pin == new_pin:
                pins[n] = new_pin
                print('PIN CHANGED SUCCESSFULLY!')
            else:
                print('ERROR! PINS DO NOT MATCH. TRY AGAIN.')

        else:
            print('NEW PIN MUST BE 4 DIGITS AND DIFFERENT FROM THE OLD PIN.')

    elif response == 'q':  # Exit
        print('---------------------------------------------')
        print('THANK YOU FOR USING OUR ATM SERVICE.')
        print('HAVE A GREAT DAY!')
        print('---------------------------------------------')
        exit()

    else:
        print('INVALID CHOICE! PLEASE SELECT A VALID OPTION.')
