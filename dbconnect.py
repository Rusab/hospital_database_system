# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:48:23 2021

@author: Rusab
"""


import MySQLdb

def connect_db(db_name):
    try:
        con = MySQLdb.connect("localhost","root","", db_name)
    except:
        print("Can't Connect")
    print("Connected")    
    cur = con.cursor()
    
    return con, cur

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
    
def view_entry(table_name, field_name, data):    
    con, cur = connect_db("HospitalDatabase")
    
    try:
        cur.execute("SELECT * from {table} WHERE {field} = {data};".format(table = table_name, field = field_name, data = data))
        row = cur.fetchone() 
        
        for (entry, field) in zip(row, table_fields[table_name]):
            print(field, entry)

        # for field in table_fields[table_name] :
        #     print(field)

  
    except:
        print("Couldn't find entry")
    
        
    disconnect_db(con, cur)

def insert_data(table_name, name, expertise, degree, position, chamber, time, fee, contactno, ids):
    con, cur = connect_db("HospitalDatabase")
    
    cur = con.cursor()
    cur.execute("INSERT INTO {0} (Name, Expertise, Degree, Position, Chamber, Time, Fee, Contactno, id) VALUES ({1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9});".format(table_name, name, expertise, degree, position, chamber, time, fee, contactno, ids))
    con.commit()
    

    disconnect_db(con, cur)
    
def delete_data(table_name, field_name, data):
    con, cur = connect_db("HospitalDatabase")
    
    cur = con.cursor()
    
    try:
        cur.execute("DELETE FROM {table} WHERE {field} = {data}".format(table = table_name, field = field_name, data=  data))       
        con.commit()
    except:
        print("Data not found")
        
    disconnect_db(con, cur)

# name = quote_str('Dragon We')
# expertise = "'Cardiology'"
# position = "'Professor'"
# chamber = "'1st Floor'"
# degree = "'MBBS'"
# time = "'12:40'"
# fee = 2400
# contactno = "'01521436142'"
# ids = 5


table_fields = {'doctorsmanagement' : ["Doctor Name: ", "Expertise: ", "Degree: ", "Position: ", "Chamber: ", "Time: ", "Fee: ", "Contact no: ", "id: "]}





while(True):
    
    print("\nWelcome to Panda Hospital Database \n What would you like to do:")
    print("1. Add new entry\n2. See all entries\n3. Delete entry\n4.View entry\n5.Cancel\n")
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
        ids = 1
        
        insert_data('doctorsmanagement', name, expertise, degree, position, chamber, time, fee, contactno, ids) 
        
    elif x == 2:
        print("Displaying all data: ")
        
        display_all('doctorsmanagement') 
    
    elif x == 3:
        field_name = input("Choose a field: ")
        data = input("Enter data: ")
        
        delete_data('doctorsmanagement', field_name, data)   
        
    elif x == 4:
        field_name = input("Enter field: ")
        data = quote_str(input("Enter {field}: ".format(field = field_name)))
        view_entry('doctorsmanagement', field_name, data)  
    
    else: 
        break



#insert_data('doctorsmanagement', name, expertise, degree, position, chamber, time, fee, contactno, ids)





    

    

