import mysql.connector
import getpass
import os

def printRow(x):
    data = x.fetchall()
    for i in range(0,len(data)):
        for j in range (0,len(data[i])):
            print(str(data[i][j]) + '\t\t', end='', flush=True)
        print('')
    print('')
    entry = input('Type any character to return:')
    os.system('cls' if os.name == 'nt' else 'clear')



def Logout(x):
    return 1;

def Quit(x):
    return 2;

def CheckEmp(x):
    os.system('cls' if os.name == 'nt' else 'clear')
    while(1):
        print("""
    A - Check all Employees
    B - Check One Employee
    Q - Return
          
          """)
        entry = input("Type input: ")
        
        if entry == 'A':
            x.execute('Select * from Employee')
            os.system('cls' if os.name == 'nt' else 'clear')
            printRow(x)
            return 0
        
        
        elif entry == 'B':
            m = 'Select * from Employee where Employee.EmployeeID = %s'
            os.system('cls' if os.name == 'nt' else 'clear')
            while(1):
                entry = input("Enter a Valid Employee ID or X to exit: ")
                
                if entry == 'X':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return 0
                
                try:
                    x.execute( m, (entry,))
                    if x.rowcount > 0:
                        break;
                    else:
                        print('Invalid ID, try again.')
                except:
                    print('Invalid Input Format, try again.')
                    os.system('cls' if os.name == 'nt' else 'clear')
            printRow(x)
            return 0


        elif entry == 'Q':
            print('Q')
            os.system('cls' if os.name == 'nt' else 'clear')
            return 0
        
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Invalid entry, try again')

def CheckInv(x):
    os.system('cls' if os.name == 'nt' else 'clear')
    while(1):
        print("""
            A - Check all Inventory
            B - Check One Item
            Q - Return
            
            """)
        entry = input("Type input: ")
        
        if entry == 'A':
            x.execute('Select * from Item')
            os.system('cls' if os.name == 'nt' else 'clear')
            printRow(x)
            return 0
        
        
        elif entry == 'B':
            m = 'Select * from Item where Item.ItemID = %s'
            os.system('cls' if os.name == 'nt' else 'clear')
            while(1):
                entry = input("Enter a Valid Item ID or X to exit: ")
                
                if entry == 'X':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return 0
                
                try:
                    x.execute( m, (entry,))
                    if x.rowcount > 0:
                        break;
                    else:
                        print('Invalid ID, try again.')
                except:
                    print('Invalid Input Format, try again.')
                    os.system('cls' if os.name == 'nt' else 'clear')
            printRow(x)
            return 0
        
        
        elif entry == 'Q':
            print('Q')
            os.system('cls' if os.name == 'nt' else 'clear')
            return 0
        
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Invalid entry, try again')

def CheckMem(x):
    os.system('cls' if os.name == 'nt' else 'clear')
    while(1):
        print("""
            A - Check all Members
            B - Check One Member
            Q - Return
            
            """)
        entry = input("Type input: ")
        
        if entry == 'A':
            x.execute('Select M.CustomerID, M.CustomerFirstName, M.CustomerLastName, sum(M.QuantitySold*M.price) as Total from (select * from (select * from(select * from mydb.Membership natural join mydb.CustomerReceipt) N natural join mydb.ReceiptItems) O natural join mydb.Item) M Group by M.CustomerID')
            os.system('cls' if os.name == 'nt' else 'clear')
            printRow(x)
            return 0
        
        
        elif entry == 'B':
            m0 = 'Select CustomerID from Membership where CustomerID = %s'
            m1 = 'Select Membership.CustomerID from Membership natural join CustomerReceipt where Membership.CustomerID = %s'
            m2 = 'Select M.CustomerID, M.CustomerFirstName, M.CustomerLastName, sum(M.QuantitySold*M.price) as Total from (select * from (select * from(select * from mydb.Membership natural join mydb.CustomerReceipt) N natural join mydb.ReceiptItems) O natural join mydb.Item) M where M.CustomerID = %s Group by M.CustomerID'

            os.system('cls' if os.name == 'nt' else 'clear')
            while(1):
                entry = input("Enter a Valid Item ID or X to exit: ")
                
                if entry == 'X':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return 0
                
                try:
                    x.execute( m0, (entry,))
                    if x.rowcount > 0:
                        x.execute( m1, (entry,))
                        if x.rowcount > 0:
                            x.execute(m2,(entry,))
                        else:
                            print('Account is empty')
                            return 0
                        break
                    else:
                        print('Invalid ID, try again.')
                except:
                    print('Invalid Input Format, try again.')
                    os.system('cls' if os.name == 'nt' else 'clear')
            printRow(x)
            return 0
        
        
        elif entry == 'Q':
            print('Q')
            os.system('cls' if os.name == 'nt' else 'clear')
            return 0
        
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Invalid entry, try again')

def CheckRec(x):
    os.system('cls' if os.name == 'nt' else 'clear')
    while(1):
        print("""
            A - Check all Receipts
            B - Check One Receipt
            Q - Return
            
            """)
        entry = input("Type input: ")
        
        if entry == 'A':
            x.execute('select R.ReceiptID, sum(R.price * R.QuantitySold)  as Total from (select * from (select * from mydb.Receipt  natural join mydb.ReceiptItems) as M natural join mydb.Item) as R Group by R.ReceiptID')
            os.system('cls' if os.name == 'nt' else 'clear')
            printRow(x)
            return 0
        
        
        elif entry == 'B':
            m = 'select R.ReceiptID, sum(R.price * R.QuantitySold)  as Total from (select * from (select * from mydb.Receipt  natural join mydb.ReceiptItems) as M natural join mydb.Item) as R where R.ReceiptID = %s Group by R.ReceiptID'
            os.system('cls' if os.name == 'nt' else 'clear')
            while(1):
                entry = input("Enter a Valid Receipt ID or X to exit: ")
                
                if entry == 'X':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return 0
                
                try:
                    x.execute( m, (entry,))
                    if x.rowcount > 0:
                        break;
                    else:
                        print('Invalid ID, try again.')
                except:
                    print('Invalid Input Format, try again.')
                    os.system('cls' if os.name == 'nt' else 'clear')
            printRow(x)
            return 0
        
        
        elif entry == 'Q':
            os.system('cls' if os.name == 'nt' else 'clear')
            return 0
        
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Invalid entry, try again')

def UpdEmp(x):
    m0 = 'Select * from Employee where EmployeeID = %s'
    m1 = 'Update Employee Set salary = %s where EmployeeID = %s;'
    print("""
    A - Update Salary
    B - Update Title
    Q - Return
    
    """)
    entry = input("Type input: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    while(1):
        if entry == 'A':
            entry = input ("Type a valid user ID: ")
            try:
                x.execute(m0,(entry,))
                if x.rowcount > 0:
                    printRow(x)
                    while (1):
                        entry2 = input('Type valid Salary, or X to return: ')
                        if entry2 == 'X':
                            return 0
                        while(1):
                            if int(entry2) > 0 and int(entry2) < 999999:
                                entry3 = input("New Salary %s. \nTo Confirm Type Y\nTo return press any key." % entry2)
                                if entry3 != 'Y':
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    return 0;
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x.execute(m1,(entry2,entry))
                                    x.execute('Commit')
                                    print('Done!!')
                                    return 0
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Salary Out of Range")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("ID not found")
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid Input Format")


        elif entry == 'B':
            m1 = 'Update Employee Set Title = %s where EmployeeID = %s;'
            os.system('cls' if os.name == 'nt' else 'clear')
            entry = input ("Type a valid user ID: ")
            try:
                x.execute(m0,(entry,))
                if x.rowcount > 0:
                    printRow(x)
                    while (1):
                        entry2 = input('Type valid Title\n\tC - Cashier\n\tM - Manager \n\tOr press X to return: ')
                        if entry2 == 'X':
                            return 0
                        while(1):
                            if entry2 == 'M' or entry2 == 'C':
                                entry3 = input("New Title %s. \nTo Confirm Type Y\nTo return press any key." % entry2)
                                if entry3 != 'Y':
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    return 0;
                                else:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x.execute(m1,(entry2,entry))
                                    x.execute('Commit')
                                    print('Done!! Logged-out')
                                    return 1
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Invalid Title")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("ID not found")
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid Input Format")

    
        elif entry == 'Q':
            os.system('cls' if os.name == 'nt' else 'clear')

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Invalid Input')

def AddEmp(x):
    os.system('cls' if os.name == 'nt' else 'clear')
    x.execute('Select max(EmployeeID) from Employee')
    m = 'Select CorpEmail From Employee where CorpEmail = %s'
    if x.rowcount > 0:
        row = x.fetchall()
        newID = int(row[0][0]) + 1
    else:
        newID = 101
    
    fName = input("Write First Name: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    lName = input("Write Last Name: ")
    if fName == "":
        fName = "None"
    if lName == "":
        lName = "None"

    os.system('cls' if os.name == 'nt' else 'clear')
    while (1):
        salary = input("Write Salary: ")
        try:
            if int(salary) > 0 and int(salary) < 999999:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid Salary")
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Invalid Format!!')
    os.system('cls' if os.name == 'nt' else 'clear')
    while (1):
        title = input('Write Employee Title: ')
        if title == 'M' or title == 'C':
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Invalid Type. Try Again!')

    os.system('cls' if os.name == 'nt' else 'clear')
    while (1):
        email = input("Input Unique Corp Email in format xxxx@abc.com: ")
        x.execute(m,(email,))
        if x.rowcount == 0:
            break;
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Email is already used! try a different one')

    os.system('cls' if os.name == 'nt' else 'clear')
    while(1):
        password = getpass.getpass("Type a password: ")
        password2 = getpass.getpass("retype password: ")
        if password != "":
            if password == password2:
                break;
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("passwords do not match!")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("No Password Typed")

    os.system('cls' if os.name == 'nt' else 'clear')
    print(str(newID) + " " + str(salary) + " " + fName + " " + lName + " " + email + " " + title)
    entry = input("\nConfirm - Y\nReturn - Any key")

    if entry == 'Y':
        m2 = 'insert into Employee (EmployeeID, Salary, FirstName, LastName, CorpEmail, Title, Password) Values (%s,%s,%s,%s,%s,%s,%s)'
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            x.execute(m2,(newID,salary,fName,lName,email,title,password))
            x.execute('Commit')
        except:
            print('Input Failed')
        os.system('cls' if os.name == 'nt' else 'clear')
        return 0

def DelEmp(x):
    m0 = 'Select * from Employee where EmployeeID = %s'
    m1 = 'Delete From Employee where EmployeeID = %s'
    os.system('cls' if os.name == 'nt' else 'clear')
    while(1):
        entry = input('Input Employee ID you want to delete, or X to return: ')
        if entry == 'X':
            return 0
        else:
            try:
                x.execute(m0,(entry,))
                if x.rowcount > 0:
                    printRow(x)
                    entry2 = input("Confirm Delete - Y\nReturn - Any Key: ")
                    if entry2 == 'Y':
                        x.execute(m1,(entry,))
                        x.execute('Commit')
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return 1
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("ID Not Found! Try Again.")
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid Input Format, Try Again!")


def DelMem(x):
    m0 = 'Select * from Membership where CustomerID = %s'
    m1 = 'Delete From Membership where CustomerID = %s'
    m2 = 'Delete from CustomerReceipt where CustomerID = %s'
    os.system('cls' if os.name == 'nt' else 'clear')
    while(1):
        entry = input('Input Customer ID you want to delete, or X to return: ')
        if entry == 'X':
            return 0
        else:
            try:
                x.execute(m0,(entry,))
                if x.rowcount > 0:
                    printRow(x)
                    entry2 = input("Confirm Delete - Y\nReturn - Any Key\n\nInput: ")
                    if entry2 == 'Y':
                        x.execute(m2,(entry,))
                        x.execute(m1,(entry,))
                        x.execute('Commit')
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return 1
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("ID Not Found! Try Again.")
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid Input Format, Try Again!")

def AddInv(x):
    m0 = 'Select ItemID, ItemName from Item where ItemID = %s'
    m1 = 'Update Item Set Quantity = Quantity + %s where ItemID = %s'
    while(1):
        entry = input('Input Item ID you want to add, or X to return: ')
        if entry == 'X':
            return 0
        else:
            try:
                x.execute(m0,(entry,))
                if x.rowcount > 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    while(1):
                        try:
                            entry2 = input("How much do you want to add: \n")
                            if int(entry2)>0 and int(entry2)<999999:
                                row = x.fetchall()
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(str(row[0][0]) + '\t\t' + str(row[0][1]) + '\t\tadd ' + entry2 )
                                entry3 = input("\nConfirm - Y\nReturn - Any Key\n\nInput: ")
                                if entry3 == 'Y':
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    x.execute(m1,(entry2,entry))
                                    x.execute('commit')
                                return 0
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print ('Invalid Quantity! Try Again')
                        except:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print ('Invalid Quantity Format! Try Again')
                            
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("ID Not Found! Try Again.")
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid Input Format, Try Again!")

def AddMem(x):
    os.system('cls' if os.name == 'nt' else 'clear')
    x.execute('Select max(CustomerID) from Membership')
    
    m = 'insert into Membership (CustomerID, FirstName, LastName) Values (%s,%s,%s)'
    
    if x.rowcount > 0:
        row = x.fetchall()
        newID = int(row[0][0]) + 1
    else:
        newID = 1

    fName = input("Write First Name: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    lName = input("Write Last Name: ")

    if fName == "":
        fName = "None"
    if lName == "":
        lName = "None"
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print ( '%s\t\t%s\t\t%s' % (str(newID), lName, fName))
    entry = input("\n\nConfirm - Y\nReturn - Any Key\n\nInput: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    try:
        if entry == 'Y':
            x.execute(m,(newID,fName,lName))
            x.execute('Commit')
    except:
        print('Process Failed!')
    return 0

def Receipt(x):
    os.system('cls' if os.name == 'nt' else 'clear')

    x.execute('Select max(ReceiptID) from Receipt')
    try:
        if x.rowcount > 0:
            row = x.fetchall()
            newID = int(row[0][0]) + 1
        else:
            newID = 1
    except:
        newID = 1


    ItemDict = {}
    entry = 'N'
    while (1):
        entry = input('Enter Item ID or X to exit: ')
        if entry == 'X':
            break
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        try:
            x.execute('Select * from Item where ItemID = %s', (entry,))
            row = x.fetchall()
            if x.rowcount > 0:
                while(1):
                    entry2 = input('Enter Quantity or X to cancel item:')
                    if entry2 == 'X':
                        break;
                    try:
                        if int(entry2)>0 and int(entry2)<999999:
                            if int(row[0][2]) >= int(entry2):
                                print(str(row[0][1]) + '\t\t' + str(entry2) + '\n')
                                entry3 = input("\n\nConfirm - Y\nReturn - Any Key\n\nInput: ")
                                os.system('cls' if os.name == 'nt' else 'clear')
                                if entry3 == 'Y':
                                    ItemDict[entry] = entry2
                                break
                            else:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print('Insufficient Quantity in Inventory!')
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print('Quantity out of range! Enter valid ID')
                    except:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('Invalid Quantity Format! Enter valid ID')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('ID Not Found! Enter valid ID')
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Invalid Input Format! Try again')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    if ItemDict:
        for key in ItemDict:
            x.execute('Select ItemName from Item where ItemID = %s', (key,))
            row = x.fetchall()
            print(str(row[0][0]) + '\t\t' + str(ItemDict[key]) + '\n')
        entry3 = input("\n\nConfirm - Y\nReturn - Any Key\n\nInput: ")
                  
        os.system('cls' if os.name == 'nt' else 'clear')
        if entry3 == 'Y':
            while(1):
                print('Employee Re-Login: ')
                email = input('Email: ')
                password = getpass.getpass()
                try:
                    x.execute('Select EmployeeID from Employee Where CorpEmail = %s and Password = %s', (email,password))
                    if x.rowcount > 0:
                      row = x.fetchall()
                      EID = str(row[0][0])
                      break
                    else:
                      os.system('cls' if os.name == 'nt' else 'clear')
                      print('Incorrect Email Or Password! Try Again')
                except:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Invalid Input Format! Try Again!')
            try:
                x.execute('insert into Receipt (ReceiptID, EmployeeID) Values (%s,%s)', (newID, EID))
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                x.execute('rollback')
                print('Receip Was Not Processed! Terminating')
                return 0

            try:
                for key in ItemDict:
                    x.execute('Update Item set Quantity = Quantity - %s where ItemID = %s',(ItemDict[key], key))
                    x.execute('Insert into ReceiptItems (ReceiptID, ItemID, QuantitySold) Values (%s,%s,%s)',(newID,key,ItemDict[key]))
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                x.execute('rollback')
                print('Receipt Items were not added Correctly! Reverting Changes!')
                return 0
            
            x.execute('commit')
            print('Receipt Uploaded Successfully')
            
                      
            while(1):
                entry = input('if you are a Customer Write ID or press X: ')
                if entry == 'X':
                      break
                else:
                    try:
                      x.execute('Select * from Membership where CustomerID = %s',(entry,))
                      if x.rowcount > 0:
                        x.execute('insert into CustomerReceipt (CustomerID, ReceiptID) Values (%s,%s)',(entry,newID))
                        break
                      else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("ID Not Found! Try Again.")
                    except:
                      os.system('cls' if os.name == 'nt' else 'clear')
                      print("Invalid Input Format2, Try Again!")
            os.system('cls' if os.name == 'nt' else 'clear')
            x.execute('Select Sum(M.QuantitySold * M.Price) from (select * from(select * from ReceiptItems natural join Receipt) as A natural join Item) as M where M.ReceiptID = %s', (newID,))
            row = x.fetchall()
            print('Total: ' + str(row[0][0]))
            entry = input('Press any key to return: ')
    return 0

            










