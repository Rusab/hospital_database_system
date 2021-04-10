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

def insert_data(table_name, name, expertise, degree, position, chamber, time, fee, contactno, ids):
    con, cur = connect_db("HospitalDatabase")
    
    cur = con.cursor()
    cur.execute("INSERT INTO {0} (Name, Expertise, Degree, Position, Chamber, Time, Fee, Contactno, id) VALUES ({1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9});".format(table_name, name, expertise, degree, position, chamber, time, fee, contactno, ids))
    con.commit()
    

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
display_all('doctorsmanagement')




    

    

