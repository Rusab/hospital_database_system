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

def display_all(table_name):
    con, cur = connect_db("HospitalDatabase")

    
    cur.execute("SELECT * from {0};".format(table_name))
    
    data =cur.fetchall()
    

    print(data)


    disconnect_db(con, cur)

def insert_data(table_name, name, expertise, degree, position, chamber, time, fee, contactno, ids):
    con, cur = connect_db("HospitalDatabase")
    
    cur = con.cursor()
    cur.execute("INSERT INTO doctorsmanagement (Name, Expertise, Degree, Position, Chamber, Time, Fee, Contactno, id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", ( name, expertise, degree, position, chamber, time, fee, contactno, ids))
    con.commit()
    

    disconnect_db(con, cur)
    
    


name = 'Uronto Panda'
expertise = 'Cardiology'
position = 'Professor'
chamber = '1st Floor'
degree = 'MBBS'
time = '12:40'
fee = 2400
contactno = '01521436142'
ids = 1


 
# name = input("Doctor Name: ")
# expertise = input("Area of expertise: ")
# position = input("Position: ")
# chamber = input("Chamber Location: ")
# degree = input("Degree: ")
# time = input("Availble at: ")
# fee = input("Fee: ")
# contactno = input("Phone number: ")
# ids = 1

#insert_data('doctorsmanagement', name, expertise, degree, position, chamber, time, fee, contactno, ids)
display_all('doctorsmanagement')




    

    

