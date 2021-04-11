# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 14:32:58 2021

@author: Josiah
"""

def Exit():
    #Order consistency useful
    global account_list
    global passwords
    global name_dict
    global name_list
    global name_count
    global passdict

    save_list = [account_list, passwords, name_dict, name_list, name_count, passdict]
    save = open("Password_storage.txt", "w")
    for i in save_list:
        save.write(str(i) + "\n")

    
def Password_save(name, website, password):
    global passwords
    global account_list
    passdict = {}
    passwords[name] += 1
    #print(passwords[name])
    if passwords[name] > 1:
        account_list[name_dict[name]][website] = password
    else:
        passdict[website] = password
        account_list.append(passdict)
        pass
    #print(account_list)
        
def view_list(name):
    global account_list
    global name_dict
    presentation_list = []
    try:
        for i in account_list[name_dict[name]].keys():
            presentation_list.append(i)

        for i in presentation_list:
            print(str(i) + " : " + str(account_list[name_dict[name]][i]))
            
    except IndexError:
        print("You have no passwords in your list")
    
def menu(name):
    loop2 = 1
    #global name_storage
    while loop2 == 1:
        menu = int(input("Type 1 to view your password list, Type 2 to add password, Type 3 to exit/log out "))
        if menu == 1:
            view_list(name)
           
        elif menu == 2:
            website = input("Enter website name ")
            password = input("Enter password ")
            Password_save(name, website, password)
        
        elif menu == 3:
            
            print("Thank you for using our service")
            print("goodbye")
            run()
            loop2 = 2
        
        else:
            print("Please enter a number listed above")
            continue

def create_account():
    global name_count
    global name_list
    global passwords
    name = input("Please enter your name ")
    age = input("Please enter your age ")
    try:
        age = int(age)
    except:
        try:
            age = int(round(float(age)))
        except:
            print("Please enter your age in number format")
            create_account()
        
    if age >= 13 and age <= 125:
        name_count += 1
        name_dict[name] = name_count
        password = input("Enter your password ")
        name_list.append([name, password])
        print("Account created")
        #print(name_dict)
        passwords[name] = 0
        menu(name)
        
    else:
        print("You do not meet the age requirement")
        #run()
        

def log_in():
    global name_list
    global attempts
    global loop1
    global name_storage
    global attempts
    name = input("Enter your name ")
    name_storage = name
    potential_password = input("Enter you password ")
    if [name, potential_password] in name_list:
        menu(name)
    else:
        print("Name or Password is incorrect ")
        attempts += 1
        if attempts < 3:
            log_in()
        else:
            print("Try again later")
            #run()

#import json      

def run():
    global attempts
    attempts = 0
    loop1 = 1    
    while loop1 == 1:
        entry = input("Type 1 to log in, Type 2 to create an account ")
        if int(entry) == 1:
            log_in()
                    
        elif int(entry) == 2:
            create_account()
            break

        elif type(entry) != int:
            print("Please select one of the listed numbers")
                
        else:
            continue

print("Welcome")
name_count = -1
name_dict = {}
name_list = []
passdict = {}
account_list = []
passwords = {}
run()
'''except:
    save_list = []
    for i in open("Password_storage.txt", "r"):
        save_list.append(i)
    print(save_list)
    account_list = save_list[0]
    passwords = int(save_list[1])
    print(save_list[2])
    print(isinstance(save_list[2], str))
    name_dict = save_list[2]
    name_dict = json.loads(name_dict)
    name_list = save_list[3]
    name_count = int(save_list[4])
    passdict = json.loads(json.dumps(save_list[5]))
    
print(account_list)
print(name_dict)
print(isinstance(name_dict, dict))'''

    
    
