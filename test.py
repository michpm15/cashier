import mysql.connector
import getpass
import os
import commands as C

def startup():
    cond = False
    os.system('cls' if os.name == 'nt' else 'clear')
    while not cond:
        
        print('Admin Login')
        username = input('Database Username: ')
        password = getpass.getpass()
        try:
            cnct = mysql.connector.connect(host="127.0.0.1", port = "3306", user = username ,passwd = password, db="mydb")
            cond = True
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Database Login Successful')
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Invalid Login')
    return cnct

def EmployeeLogin(x):
    prep = "Select Employee.EmployeeID, Employee.FirstName, Employee.LastName, Employee.Title from Employee Where Employee.CorpEmail = %s and Employee.Password = %s"
    while 1:
        temp = 0
        print("Employee Login")
        email = input("E-mail: ")
        password = getpass.getpass()
        try:
            x.execute(prep, (email, password))
            row = x.fetchall()
            
            os.system('cls' if os.name == 'nt' else 'clear')
            if x.rowcount > 0:
                print ("Welcome %s %s!" % (row[0][1], row[0][2]))
            
                if row[0][3] == 'M':
                    temp = Manager(x)
                    if temp == 2:
                        return
                else:
                    temp = Cashier(x)
                    if temp == 2:
                        return
            else:
                print ("Incorrect Email or Password, Try Again")
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Incorrect Input Format, Try Again")

def Manager(x):
    switch = {
        'L': C.Logout,
        'AE': C.AddEmp,
        'DE': C.DelEmp,
        'UE': C.UpdEmp,
        'CE': C.CheckEmp,
        'AI': C.AddInv,
        'CI': C.CheckInv,
        'CR': C.CheckRec,
        'AM': C.AddMem,
        'CM': C.CheckMem,
        'DM': C.DelMem,
        'Q': C.Quit,
    }
    while(1):
        temp = 0
        print ("""
            
        Input:
        L  - logout
        AE - Add Employee
        DE - Delete Employee
        UE - Update Employee
        CE - Check Employee
        AI - Add Inventory
        CI - Check Inventory
        CR - Check Receipts
        AM - Add Member
        CM - Check Member
        DM - Delete Member
        Q  - Quit
            
            """)
        entry = input("Type Action: ")

        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            temp = switch[entry](x)
        except:
            print("\nInvalid Input! Try again.")
        if temp == 1 or temp == 2:
            return temp;
def Cashier(x):
    switch = {
        'L': C.Logout,
        'R': C.Receipt,
        'CM': C.CheckMem,
        'Q' : C.Quit,
    }
    while(1):
        temp = 0
        print ("""
            
            Input:
            L  - logout
            R  - Receipt
            CM - Check Member
           
            """)
        entry = input("Type Action: ")
        
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            temp = switch[entry](x)
        except:
            print("\nInvalid Input! Try again.")
        if temp == 1 or temp == 2:
            return temp;

cnct = startup()
cursor = cnct.cursor(buffered=True)

EmployeeLogin(cursor)

