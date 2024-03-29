#Bank_Management_System
#Author:  Ankan Ghosh | 25.3.24 | Innovixion Tech Task 3
'''
Create a system that simulates basic bank account functions such as
account creation, balance checking, deposits, and withdrawals.
'''


import pymysql

# Connect to the MySQL database
mydb = pymysql.connect(
    host='localhost',
    user='root',
    password='Zeus#@..0010',
    database='BANK_MANAGEMENT_SYSTEM'
)

def OpenAcc():
    # Get user input for account details
    n = input("\t\t\tEnter Name: ")
    acc = input("\t\t\tEnter Account Number: ")
    dob = input("\t\t\tEnter Date of Birth:")
    add = input("\t\t\tEnter Address:")
    cn = input("\t\t\tEnter Contact NO.:")
    ob = int(input("\t\t\tEnter Opening Balance: "))

    # Insert data into the account table
    with mydb.cursor() as cursor:
        sql1 = 'INSERT INTO account VALUES (%s, %s, %s, %s, %s, %s)'
        cursor.execute(sql1, (n, acc, dob, add, cn, ob))

    # Insert data into the amount table
    with mydb.cursor() as cursor:
        sql2 = 'INSERT INTO amount VALUES (%s, %s, %s)'
        cursor.execute(sql2, (n, acc, ob))

    mydb.commit()
    print("\t\t\t DATA ENTERED SUCCESSFULLY")
    main()

def DepoAmount():
    amount = input("\t\t\tEnter amount you want to Deposit: ")
    acc = input("\t\t\tEnter Account Number: ")

    # Update balance in the amount table
    with mydb.cursor() as cursor:
        cursor.execute('SELECT balance FROM amount WHERE AccNo = %s', (acc,))
        result = cursor.fetchone()
        t = result[0] + int(amount)
        cursor.execute('UPDATE amount SET balance = %s WHERE AccNo = %s', (t, acc))

    mydb.commit()
    main()

def WithAmount():
    amount = input("\t\t\tEnter amount you want to Withdraw: ")
    acc = input("\t\t\tEnter Account Number: ")

    # Update balance in the amount table
    with mydb.cursor() as cursor:
        cursor.execute('SELECT balance FROM amount WHERE AccNo = %s', (acc,))
        result = cursor.fetchone()
        t = result[0] - int(amount)
        cursor.execute('UPDATE amount SET balance = %s WHERE AccNo = %s', (t, acc))

    mydb.commit()
    main()

def BalEnq():
    acc = input("\t\t\tEnter Account Number: ")

    # Fetch and print balance from the amount table
    with mydb.cursor() as cursor:
        cursor.execute('SELECT * FROM amount WHERE AccNo = %s', (acc,))
        result = cursor.fetchone()
        print("Balance of Account Number", acc, "is:", result[-1])

    main()

def CusDetails():
    acc = input("\t\t\tEnter Account Number: ")

    # Fetch and print customer details from the account table
    with mydb.cursor() as cursor:
        cursor.execute('SELECT * FROM account WHERE AccNo = %s', (acc,))
        result = cursor.fetchone()
        for i in result:
            print(i)

    main()

def CloseAcc():
    acc = input("\t\t\tEnter Account Number: ")

    # Delete account details from both tables
    with mydb.cursor() as cursor:
        cursor.execute('DELETE FROM account WHERE AccNo = %s', (acc,))
        cursor.execute('DELETE FROM amount WHERE AccNo = %s', (acc,))

    mydb.commit()
    main()

def main():
    print("\t\t\tBank Management System")
    print('''
        1. OPEN NEW ACCOUNT
        2. DEPOSIT AMOUNT
        3. WITHDRAW AMOUNT 
        4. BALANCE ENQUIRY
        5. CUSTOMER DETAILS
        6. CLOSE AN ACCOUNT ''')

    choice = input("Enter task to perform: ")
    if choice == '1':
        OpenAcc()
    elif choice == '2':
        DepoAmount()
    elif choice == '3':
        WithAmount()
    elif choice == '4':
        BalEnq()
    elif choice == '5':
        CusDetails()
    elif choice == '6':
        CloseAcc()
    else:
        print("\n\t\t\tInvalid Choice\n\t\t\tTry Again!!")


if __name__ == "__main__":
    main()
