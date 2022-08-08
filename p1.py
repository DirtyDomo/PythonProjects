import mysql.connector
import config as c
import getpass
import logging
import admin as a
ruser = a.Username
rpass = a.Password
#For Adding new users
def register(): 
    cnx = mysql.connector.connect(user = c.user, password= c.password, host = c.host , database= "project1")
    cursor = cnx.cursor(buffered=True)
    logger = logging.getLogger(ruser)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s :%(name)s: %(message)s')
    File_Handler = logging.FileHandler("Employee.log")
    logger.addHandler(File_Handler)
    File_Handler.setFormatter(formatter)
    print("Create User")
    Username = input()
    print("Create Password")
    Password = getpass.getpass()
    print("Confirm Password")
    Confirm = getpass.getpass()
    if Password != Confirm:
        print("Passwords Do Not Match, Restart!")
        register()
    elif len(Password)>10:
        print("Characer maxium is 10, restart!")
        register()
    elif Username == cursor.execute("SELECT Username FROM users"):
        print("Username Already Exist, RESTART!")
        register()
    else:
        query = f"INSERT INTO users (username, Password) Values ('{Username}','{Password}')"
        cursor.execute(query)
        cnx.commit()
        logger.info(f"'{Username}' Has been added to the GOGO family Password is: '{Password}'")
        print("User sucessfully added: Welcome to the GoGo family")
        cursor.close
    while cursor == cursor.close:
        print("No further credentials needed")
        break
#Logging in for Registered Users
def login(): 
    cnx = mysql.connector.connect(user = c.user, password= c.password, host = c.host , database= "project1")
    cursor = cnx.cursor()
    print("*******GOGO LOGIN*******")
    print("\nPlease Input Your Registered Username and Password:")
    print("Registered Username?")
    Username = input()
    print("Registered Password?")
    Password = input()
    query = f"SELECT * FROM users WHERE Username = '{Username}' AND Password ='{Password}'"
    cursor.execute(query)
    for user in cursor:
        if user[0] == Username and user[1] == Password:
            print("Welcome back, " + Username + "!")
            cursor.close
        elif user[0] or user[1] != cursor:
            print("User not found: Please Restart")
            login()
    cursor.close()
    cnx.close()
#Tranactions, Will log each transaction by date and time
def transaction():
    cnx = mysql.connector.connect(user = c.user, password= c.password, host = c.host , database= "project1")
    cursor = cnx.cursor(buffered=True)
    print("Registered Username?")
    Username = input()
    print("Registered Password?")
    Password = input()
    print("POS SYSTEM: " + Username)
    logger = logging.getLogger(Username)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s: %(levelname)s :%(name)s: %(message)s')
    File_Handler = logging.FileHandler("SaleHistory.log")
    logger.addHandler(File_Handler)
    File_Handler.setFormatter(formatter)
    print("What is The 'Game ID' of Product?")
    gid = int(input())
    print("What is the price(USD) of Product?")
    price = int(input())
    query = f"SELECT * FROM inventory WHERE Game_ID = '{gid}' AND price = '{price}'"
    cursor.execute(query)
    with cursor:
        for elem in cursor:
            if gid != elem[0]:
                print("No record of product exists")
                logger.info("Wrong Game Id input")
            elif price != elem[2]:
                print("wrong price. Gogo is watching you")
                logger.info("Wrong price")
            elif gid == elem[0] and price == elem[2]:
                print(f"'{elem[1]}' Sold for '{elem[2]}'")
                logger.info(f"Sold'{gid}' for '{price}'")        
                try:
                    input() != int(input())
                except ValueError:
                    logger.error("Input wasn't integer")
        cursor.close
    cnx.close
#Views Table inventory
def viewinv():
    cnx = mysql.connector.connect(user = c.user, password= c.password, host = c.host , database= "project1")
    cursor = cnx.cursor(buffered=True)
    query = "Select * From inventory"
    cursor.execute(query)
    for record in cursor:
        print(record[0], record[1], record[2])
    cursor.close
    cnx.close
#Adds new row to Table inventory
def addinv():
    cnx = mysql.connector.connect(user = c.user, password= c.password, host = c.host , database= "project1")
    cursor = cnx.cursor()
    logging.basicConfig(filename ="Product_Inventory.txt", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
    print("*** Name of Product:***")
    name = input()
    print("*** Price of product?(USD)***")
    price = int(input())
    query = f"INSERT INTO inventory (Game_Name, Price) VALUES ('{name}','{price}')"
    cursor.execute(query)
    cnx.commit()
    cursor.close
    logging.debug(f"Product '{name}' Added")
    print("Item Sucessfuly added!")
#Remove Item from inventory
def reminv():
    cnx = mysql.connector.connect(user = c.user, password= c.password, host = c.host , database= "project1")
    cursor = cnx.cursor()
    logging.basicConfig(filename ="Product_Inventory.txt", level=logging.INFO, format='%(asctime)s :: %(message)s')
    print("***CHOOSE ID TO REMOVE***")
    Gid= int(input())
    query = f"DELETE FROM inventory WHERE Game_ID = '{Gid}'"
    cursor.execute(query)
    cnx.commit()
    cursor.close
    logging.info(f" Product number '{Gid}' removed!")
    print(" Item Sucessfully Removed")
    #Inventory option branch, comeback to add various functions
def Inventory():
    print("\nInventory Management System, choose your option:")
    print("(\t1) View Inventory")
    print("(\t2) Add Item To Inventory")
    print("(\t3) Remove Item from Inventory")
    choice = input(">>> ")
    if choice == "1":
        viewinv()
    elif choice == "2":
        addinv()
    elif choice == "3":
        reminv()
    else:
        print("Invalid Selection, Try again")
        Inventory()
#Used to access many functions of application
def main(): 
    try:
        cnx = mysql.connector.connect(user = c.user, password= c.password, host = c.host , database= "project1")
        cursor = cnx.cursor()
    except mysql.connector.error as mse:
        print(mse.msg)
    pass
    print("***\nWELCOME TO GAMER GOGO!***")
    print("\t1) Login")
    print("\t2) Register New Employee")
    print("\t3) Inventory Options")
    print("\t4) POS System")
    choice = input(">>> ")
    if choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "3":
        Inventory()
    elif choice == "4":
        transaction()
    else:
        print("Invalid Selection")
        return
main()