# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:48:23 2021

@author: Rusab
"""


import dbfunctions as db

table_fields = {'doctorsmanagement' : ["Doctor Name: ", "Sex: ", "Expertise: ", "Degree: ", "Position: ", "Chamber: ", "Time: ", "Fee: ", "Contact no: ", "id: "]}

view_ports = {'dview:doctorsmanagement': ["name", "sex", "expertise", "degree", "position", "chamber", "time", "fee", "contactno"]}

table_name = 'doctorsmanagement'



while(True):
    
    print("\nWelcome to Panda Hospital Database \n What would you like to do:")
    print("1. Add new entry\n2. See all entries\n3. Delete entry\n4. View entry\n5. Update entry\n6. Cancel")
    x = int(input())
    
    if x == 1:
        print("Enter the following data: \n")
        name = db.quote_str(input("Doctor Name: "))
        sex = db.quote_str(input("Sex: "))
        expertise = db.quote_str(input("Area of expertise: "))
        position = db.quote_str(input("Position: "))
        chamber = db.quote_str(input("Chamber Location: "))
        degree = db.quote_str(input("Degree: "))
        time = db.quote_str(input("Availble at: "))
        fee = input("Fee: ")
        contactno = db.quote_str( input("Phone number: "))
        
        db.insert_data(table_name, name, sex, expertise, degree, position, chamber, time, fee, contactno) 
        
    elif x == 2:
        print("Displaying all data: ")
        
        db.display_all(table_name) 
    
    elif x == 3:
        3
        field_name = input("Choose a field: ")
        data = db.quote_str(input("Enter data: "))
    
        d = int(input("1.Soft Delete\n2.Hard Delete\n"))
    
        if d == 2:             
            db.delete_data(table_name, field_name, data)
            
        elif d == 1:
            db.soft_delete(table_name, field_name, data)
            
        
    elif x == 4:
        field_name = input("Enter field: ")
        data = db.quote_str(input("Enter {field}: ".format(field = field_name)))
        db.view_entry(table_name, field_name, data, view_ports['dview:doctorsmanagement'], table_fields[table_name])  
        
    elif x == 5:
        print("Search for a entry to make changes: ")
        s_field_name = input("Enter field: ")
        s_data = db.quote_str(input("Enter {field}: ".format(field = s_field_name))) 
        
        if db.check_entry(table_name, s_field_name, s_data):
            rep = 'Y'
        
            while(rep == 'Y'):    
                
                print("Enter the changes you want to make: ")
                u_field_name = input("Enter field: ")
                u_data = db.quote_str(input("Enter {field}: ".format(field = u_field_name)))      
                
                db.update_data(table_name, s_field_name, s_data, u_field_name, u_data)
                
                rep = input("Do you want to update more fields ? [Y/N]")
        
        else:
            print("No such entry found.")
    
    else: 
        break



#insert_data('doctorsmanagement', name, expertise, degree, position, chamber, time, fee, contactno, ids)





    

    

