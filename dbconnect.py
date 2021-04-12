# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:48:23 2021

@author: Rusab
"""


import MySQLdb

def connect_db(db_name):
    try:
        con = MySQLdb.connect("localhost","root","", db_name)
        cur = con.cursor()
        print("Connected") 
        
        return con, cur
        
    except:
        print("Can't Connect")
   

    


def disconnect_db(con, cur):
    
    cur.close()
    con.close()    
    
def quote_str(text):
    return "\"" + text + "\""

def display_all(table_name):
    con, cur = connect_db("HospitalDatabase")
   
    cur.execute("SELECT * from {0};".format(table_name))
    
    data =cur.fetchall() 
    print(data)
    
    disconnect_db(con, cur)
    
    
    
    
def check_entry(table_name, field_name, data):    
    con, cur = connect_db("HospitalDatabase")
    
    try:
        cur.execute("SELECT * from {table} WHERE {field} = {data};".format(table = table_name, field = field_name, data = data))
        data = cur.fetchall()
        
        if data:
            return True
        else:
            return False
    except:
        return False
    
        
    disconnect_db(con, cur)


    
def view_entry(table_name, field_name, data):    
    con, cur = connect_db("HospitalDatabase")
    
    try:
        cur.execute("SELECT * from {table} WHERE {field} = {data};".format(table = table_name, field = field_name, data = data))
        row = cur.fetchone() 
        
        for (entry, field) in zip(row, table_fields[table_name]):
            print(field, entry)

    except:
        print("Couldn't find entry")
    
        
    disconnect_db(con, cur)

def insert_data(table_name, name, expertise, degree, position, chamber, time, fee, contactno):
    con, cur = connect_db("HospitalDatabase")
    
    cur.execute("INSERT INTO {0} (Name, Expertise, Degree, Position, Chamber, Time, Fee, Contactno) VALUES ({1}, {2}, {3}, {4}, {5}, {6}, {7}, {8});".format(table_name, name, expertise, degree, position, chamber, time, fee, contactno))
    con.commit()
    

    disconnect_db(con, cur)
    
def delete_data(table_name, field_name, data):
    con, cur = connect_db("HospitalDatabase")
    
    
    try:
        cur.execute("DELETE FROM {table} WHERE {field} = {data}".format(table = table_name, field = field_name, data=  data))       
        con.commit()
        
    except:
        print("Data not found")
        
    disconnect_db(con, cur)

def update_data(table_name, s_field_name, s_data, u_field_name, u_data):
    con, cur = connect_db("HospitalDatabase")  
    
    try:
        cur.execute("UPDATE {table} SET {u_field} = {u_data} WHERE {s_field} = {s_data}".format(table = table_name, s_field = s_field_name, s_data = s_data, u_field = u_field_name, u_data = u_data))
        con.commit()
        print("Updated")
        
    except:
        print("Couldn't update entry")    
   
    disconnect_db(con, cur)
    



table_fields = {'doctorsmanagement' : ["Doctor Name: ", "Expertise: ", "Degree: ", "Position: ", "Chamber: ", "Time: ", "Fee: ", "Contact no: ", "id: "]}

table_name = 'doctorsmanagement'



while(True):
    
    print("\nWelcome to Panda Hospital Database \n What would you like to do:")
    print("1. Add new entry\n2. See all entries\n3. Delete entry\n4. View entry\n5. Update entry\n6. Cancel")
    x = int(input())
    
    if x == 1:
        print("Enter the following data: \n")
        name = quote_str(input("Doctor Name: "))
        expertise = quote_str(input("Area of expertise: "))
        position = quote_str(input("Position: "))
        chamber = quote_str(input("Chamber Location: "))
        degree = quote_str(input("Degree: "))
        time = quote_str(input("Availble at: "))
        fee = input("Fee: ")
        contactno = quote_str( input("Phone number: "))
        
        insert_data(table_name, name, expertise, degree, position, chamber, time, fee, contactno) 
        
    elif x == 2:
        print("Displaying all data: ")
        
        display_all(table_name) 
    
    elif x == 3:
        field_name = input("Choose a field: ")
        data = input("Enter data: ")
        
        delete_data(table_name, field_name, data)   
        
    elif x == 4:
        field_name = input("Enter field: ")
        data = quote_str(input("Enter {field}: ".format(field = field_name)))
        view_entry(table_name, field_name, data)  
        
    elif x == 5:
        print("Search for a entry to make changes: ")
        s_field_name = input("Enter field: ")
        s_data = quote_str(input("Enter {field}: ".format(field = s_field_name))) 
        
        if check_entry(table_name, s_field_name, s_data):
            rep = 'Y'
        
            while(rep == 'Y'):    
                
                print("Enter the changes you want to make: ")
                u_field_name = input("Enter field: ")
                u_data = quote_str(input("Enter {field}: ".format(field = u_field_name)))      
                
                update_data(table_name, s_field_name, s_data, u_field_name, u_data)
                
                rep = input("Do you want to update more fields ? [Y/N]")
        
        else:
            print("No such entry found.")
    
    else: 
        break



#insert_data('doctorsmanagement', name, expertise, degree, position, chamber, time, fee, contactno, ids)





    

    

