# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 11:46:58 2021

@author: Josiah
"""
account_list = {}
name_list =[]
loop1 = 1
loop2 = 2
attempts = 0
name_dict = {}
name_count = 0
access_dictionary = {}

#Name - dict or string?
#First time, list/dict empty

def view_list(name):
    try:
        print(account_list[account_list.index(name)])
    except:
        print("You have no passwords in your list")
        
    remove_determine = input("Press Enter to continue or type 'Remove' to remove an object from the list")
    if remove_determine == "":
        menu(name)
    else:
        remove = input("Enter the website name of the password you wish removed or press enter to return to the menu")
        if remove == "":
            menu(name)
        elif remove in account_list[account_list.index(name)]:
            account_list[account_list.index(name.pop(remove))]

def search(name):
     global loop2
     loop2 == 2
     while loop2 == 2:
         search = ""
         search = input("Enter website name or press Enter to return to menu ")
         if search.strip().lower() == "":
             loop2 = 1
                
         else:
            try:
                print(account_list[account_list.index(name[search.strip().lower()])])
            except IndexError:
               print("This website could not be found, check your spelling and try again")

def Password_save(name, site, password):
    global name_dict
    global access_dictionary
    temp_name = []
    temp_name = [name, {site:password}]
    if temp_name or access_dictionary[name] in account_list:
        #Hopefully this works
        account_list[account_list.index([name, {}])[2]][site] = password
        access_dictionary[name] = {}.append(site, password)
    else:
        account_list.append(temp_name)

def menu(name):
    loop2 = 1
    #global name_storage
    while loop2 == 1:
        menu = int(input("Type 1 to view your password list, Type 2 to search, Type 3 to add password, Type 4 to exit/log out "))
        if menu == 1:
            view_list(name)
            
        elif menu == 2:
            search(name)
           
        elif menu == 3:
            website = input("Enter website name ")
            password = input("Enter password ")
            Password_save(name, website, password)
            

def create_account():
    global account_list
    global name_list
    global loop1
    global name_dict
    global name_count
    name = input("Please enter your name ")
    age = int(input("Please enter your age "))
    if age >= 13 and age <= 125:
        name_count += 1
        name_dict[name] = name_count
        password = input("Enter your password ")
        name_list.append([name, password])
        print("Account created")
        menu(name)
        
    else:
        print("You do not meet the age requirement")
        loop1 = 5
        

def log_in():
    global name_list
    global attempts
    global loop1
    global name_storage
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
            loop1 = 3
        
print("Welcome")
while loop1 == 1:
    entry = input("Type 1 to log in, Type 2 to create an account ")
    if int(entry) == 1:
        log_in()
                
    elif int(entry) == 2:
        create_account()
        break
            
    elif type(entry) != int:
        print("Please select a number")
                
    else:
        continue
    
    
    
    
    
