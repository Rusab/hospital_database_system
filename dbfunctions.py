# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 03:10:16 2021

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
   
    cur.execute("SELECT * from {0} WHERE is_deleted = 0;".format(table_name))
    
    data =cur.fetchall() 
    
    
    for row in data:
        for col in row:
            print(col)
            
    # print(data)
    
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


    
def view_entry(table_name, field_name, data, view_port, field_names):    
    con, cur = connect_db("HospitalDatabase")
    
    cols = ""
    firstField = True
    
    for col in view_port:
        if firstField:
            cols = cols + col
            firstField = False
        else:
            cols = cols + ", " + col
    
    try:
        cur.execute("SELECT {cols} from {table} WHERE {field} = {data} AND is_deleted = 0;".format(cols = cols, table = table_name, field = field_name, data = data))
        row = cur.fetchone() 
        
        for (entry, field) in zip(row, field_names):
            print(field, entry)

    except:
        print("Couldn't find entry")
    
        
    disconnect_db(con, cur)

def insert_data(table_name, name, sex, expertise, degree, position, chamber, time, fee, contactno):
    con, cur = connect_db("HospitalDatabase")
    
    cur.execute("INSERT INTO {0} (Name, Sex, Expertise, Degree, Position, Chamber, Time, Fee, Contactno) VALUES ({1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9});".format(table_name, name, sex, expertise, degree, position, chamber, time, fee, contactno))
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
    

def soft_delete(table_name, field_name, data):
    update_data(table_name, field_name, data, "is_deleted", 1)