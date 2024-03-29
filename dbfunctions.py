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

        
        return con, cur
        
    except:
        print("Can't Connect")


def disconnect_db(con, cur):
    
    cur.close()
    con.close()    
    
def quote_str(text):
    return "\"" + text + "\""

def comma_join(text):
    cols = ""
    firstField = True
    
    for col in text:
        if firstField:
            cols = cols + col
            firstField = False
        else:
            cols = cols + ", " + col
    
    return cols

def date_process(text):
    d = text.split("-")
    if len(d) == 3:
        return d[2] + "-" + d[1] + "-"+ d[0]
    else:
        raise Exception("Wrong Format")
        
def list_make(*data):
    data_list = list()
    for col in data:
        data_list.append(col)
    
    return data_list
   
def choice_make(*choices):
    i = 1
    prompt = ""
    
    for choice in choices:
        prompt = prompt + str(i) + ". " + choice + "\n"
        i = i + 1
    
    return int(input(prompt))    

def select_make(choices):
    i = 1
    prompt = ""
    
    for choice in choices:
        prompt = prompt + str(i) + ". " + choice + "\n"
        i = i + 1
    
    return int(input(prompt))    



def display_all(table_name):
    con, cur = connect_db("HospitalDatabase")
   
    cur.execute("SELECT * from {0} WHERE is_deleted = 0;".format(table_name))
    
    data =cur.fetchall() 
    
    
    for row in data:
        for col in row:
            print(col)
            
    # print(data)
    
    disconnect_db(con, cur)
    
    
# def display_multiple()
def check_entry(table_name, field_name, data, view_port, field_names, table_combo = [], order = "", jointype = "LEFT JOIN"):    
    con, cur = connect_db("HospitalDatabase")
    
    keyword = ""
    for (name, dat) in zip(field_name, data):
        keyword = keyword + table_name[0] +"."+name + " = " + dat + " AND "
    
    from_table = table_name[0]
    
    if len(table_name) > 1:
        for combo in table_combo:
            from_table +=  " " + jointype +" " + combo[1] + " ON " + combo[0]+"."+combo[2] + " = " + combo[1]+"."+combo[2] 
        
    
    first_table = True
    for table in table_name:
        if(not first_table):
            keyword += " AND "
        keyword += table + "." + "is_deleted = 0"
        first_table = False
    
    if len(order):
        keyword += " ORDER BY " + order + " DESC LIMIT 1"

        
    
    #string of columns to select
    cols = comma_join(view_port)
    selector_array = []
    i = 0
    
    # print("SELECT {cols} from {table} WHERE {keyword};".format(cols = cols, table = from_table, keyword = keyword))
    
    try:
        cur.execute("SELECT {cols} from {table} WHERE {keyword};".format(cols = cols, table = from_table, keyword = keyword))
         
        
        row = cur.fetchone() 
        cur.execute("SELECT {cols} from {table} WHERE {keyword};".format(cols = cols, table = from_table, keyword = keyword))     
        data =cur.fetchall() 
        
        # disconnect_db(con, cur)
        disconnect_db(con, cur)
        
        # print(data)
    #check if one or more columns have been selected
        if len(data) <= len(row):    
            for row in data:
                i += 1
                select = []
                print("Entry no. ", i)
                print("---------------")
                for (entry, field, coln) in zip(row, field_names, view_port):
                    print(field, entry)
                    entry = quote_str(str(entry))
               
                    if len(table_combo) == 0 :
                        select.append(""+ table_name[0] +"."+ coln + " = " + entry)
                    elif table_name[0] in coln:
                        select.append("" + coln + " = " + entry)
                    
                selector_array.append(select)
                
                    
                print("\n")
        
        
        else:
            select = []
            i += 1
            print("Entry no. ", i)
            print("---------------")
            for (entry, field, coln) in zip(row, field_names, view_port):
                print(field, entry)
                entry = quote_str(str(entry))
                
                if len(table_combo) == 0:
                    select.append("" + table_name[0] +"."+ coln + " = " + entry)
                elif table_name[0] in coln:
                    select.append("" + coln + " = " + entry)
                
            selector_array.append(select)         

        
    except:
        print("No Entries Found")
        return
        
   


 
    if i > 1:
        x  = int(input("\nMultiple results found !!! \nSelect an entry: "))
    else:
        x = 1
        
    
    selection = selector_array[x-1]
    # print(selection)
    keyword = ""
    
    first_cell = True
    for cell in selection:
        if(not first_cell):
            keyword += " AND "
        keyword += cell 
        first_cell = False
    
    # print(keyword)
    
    
    return keyword

    
    
        
    



# def check_entry(table_name, field_name, data):    
#     con, cur = connect_db("HospitalDatabase")
    
#     try:
#         cur.execute("SELECT * from {table} WHERE {field} = {data};".format(table = table_name, field = field_name, data = data))
#         data = cur.fetchall()
        
#         if data:
#             return True
#         else:
#             return False
#     except:
#         return False
    
        
#     disconnect_db(con, cur)


    
def view_entry(table_name, field_name, data, view_port, field_names, table_combo = [], order = "", jointype = "LEFT JOIN"):    
    con, cur = connect_db("HospitalDatabase")
    
    keyword = ""
    for (name, dat) in zip(field_name, data):
        keyword = keyword + table_name[0] +"."+name + " = " + dat + " AND "
    
    from_table = table_name[0]
    
    if len(table_name) > 1:
        for combo in table_combo:
            from_table +=  " " + jointype +" " + combo[1] + " ON " + combo[0]+"."+combo[2] + " = " + combo[1]+"."+combo[2] 
        
    
    first_table = True
    for table in table_name:
        if(not first_table):
            keyword += " AND "
        keyword += table + "." + "is_deleted = 0"
        first_table = False
    
    if len(order):
        keyword += " ORDER BY " + order + " DESC LIMIT 1"

        
    
    #string of columns to select
    cols = comma_join(view_port)
    
    # print("SELECT {cols} from {table} WHERE {keyword};".format(cols = cols, table = from_table, keyword = keyword))
    
    try:
        cur.execute("SELECT {cols} from {table} WHERE {keyword};".format(cols = cols, table = from_table, keyword = keyword))
         
    
        row = cur.fetchone() 
        cur.execute("SELECT {cols} from {table} WHERE {keyword};".format(cols = cols, table = from_table, keyword = keyword))     
        data =cur.fetchall() 
        
        print("\nShowing Results:\n--------------------")
        #check if one or more columns have been selected
        if len(data) <= len(row):    
            for row in data:
                for (entry, field) in zip(row, field_names):
                    print(field, entry)
                print("\n")
        
        
        else:
            for (entry, field) in zip(row, field_names):
                print(field, entry)
        
    except:
        print("No Entries Found")
    
        
    disconnect_db(con, cur)
    

    
def view_range(table_name, field_name, data_range, view_port, field_names, inequality, table_combo = [], order = "", jointype = "LEFT JOIN"):    
    con, cur = connect_db("HospitalDatabase")
    
    
    
    keyword = ""
    for (name, dat, inequal) in zip(field_name, data_range, inequality):
        keyword = keyword + table_name[0] +"."+name + inequal + dat + " AND "
   

    from_table = table_name[0]
    
    if len(table_name) > 1:
        for combo in table_combo:
            from_table += " " + jointype +" "  + combo[1] + " ON " + combo[0]+"."+combo[2] + " = " + combo[1]+"."+combo[2] 
        
    
    first_table = True
    for table in table_name:
        if(not first_table):
            keyword += " AND "
        keyword += table + "." + "is_deleted = 0"
        first_table = False
    
    if len(order):
        keyword += " ORDER BY " + order + " DESC"
        
        
    
    #string of columns to select
    cols = comma_join(view_port)
    
    # print("SELECT {cols} from {table} WHERE {keyword};".format(cols = cols, table = from_table, keyword = keyword))

    try:
        cur.execute("SELECT {cols} from {table} WHERE {keyword};".format(cols = cols, table = from_table, keyword = keyword))
         
    
        row = cur.fetchone() 
        cur.execute("SELECT {cols} from {table} WHERE {keyword};".format(cols = cols, table = from_table, keyword = keyword))     
        data =cur.fetchall() 
        
        print("\nShowing Results:\n--------------------")
        #check if one or more columns have been selected
        if len(data) <= len(row):    
            for row in data:
                for (entry, field) in zip(row, field_names):
                    print(field, entry)
                print("\n")
        
        
        else:
            for (entry, field) in zip(row, field_names):
                print(field, entry)
        
    except:
        print("Couldn't find entry")
    
        
    disconnect_db(con, cur)    


def view_all(table_name, view_port, field_names, table_combo = [], order = "", jointype = "LEFT JOIN"):    
    con, cur = connect_db("HospitalDatabase")
    
    
    
    keyword = ""


    from_table = table_name[0]
    
    if len(table_name) > 1:
        for combo in table_combo:
            from_table += " " + jointype +" "  + combo[1] + " ON " + combo[0]+"."+combo[2] + " = " + combo[1]+"."+combo[2] 
        
    
    first_table = True
    for table in table_name:
        if(not first_table):
            keyword += " AND "
        keyword += table + "." + "is_deleted = 0"
        first_table = False
    
    if len(order):
        keyword += " ORDER BY " + order + " DESC"
        
        
    
    #string of columns to select
    cols = comma_join(view_port)
    
    # print("SELECT {cols} from {table} WHERE {keyword};".format(cols = cols, table = from_table, keyword = keyword))

    try:
        cur.execute("SELECT {cols} from {table} WHERE {keyword};".format(cols = cols, table = from_table, keyword = keyword))
         
    
        row = cur.fetchone() 
        cur.execute("SELECT {cols} from {table} WHERE {keyword};".format(cols = cols, table = from_table, keyword = keyword))     
        data =cur.fetchall() 
        
        print("\nShowing Results:\n--------------------")
        #check if one or more columns have been selected
        if len(data) <= len(row):    
            for row in data:
                for (entry, field) in zip(row, field_names):
                    print(field, entry)
                print("\n")
        
        
        else:
            for (entry, field) in zip(row, field_names):
                print(field, entry)
        
    except:
        print("Couldn't find entry")
    
        
    disconnect_db(con, cur)    



def insert_data(table_name, fields_inserted, field_data):
    con, cur = connect_db("HospitalDatabase")

    fields = comma_join(fields_inserted)
    data = comma_join(field_data)
    
    try:
        cur.execute("INSERT INTO {table} ({fields}) VALUES ({data});".format(table = table_name, fields = fields, data = data))
        con.commit()
        
        print("Entry Added Succesfully")
        
    except:
        print("Failed to add entry")
        
    disconnect_db(con, cur)
    
    
    
def delete_data(table_name, where):
    con, cur = connect_db("HospitalDatabase")
    
    
    try:
        cur.execute("DELETE FROM {table} WHERE {where}".format(table = table_name[0], where = where))       
        con.commit()
        print("Entry Successfully Deleted")
        
    except:
        print("Data not found")
        
    disconnect_db(con, cur)



def update_data(table_name, where, field_name, data):
    con, cur = connect_db("HospitalDatabase")  
    

    
    keyword = ""
    first = True
    for (name, dat) in zip(field_name, data):
        if(not first):
            keyword += ", "
        keyword = keyword + table_name[0] +"."+name + " = " + dat 
        first = False
    
    # print("UPDATE {table} SET {keyword} WHERE {where};".format(table = table_name[0], keyword = keyword, where = where))
    try:
        cur.execute("UPDATE {table} SET {keyword} WHERE {where};".format(table = table_name[0], keyword = keyword, where = where))
        con.commit()
        print("Updated")
        
    except:
        print("Couldn't update entry")    
   
    disconnect_db(con, cur)
    




# def soft_delete(table_name, field_name, data):
#     update_data(table_name, field_name, data, "is_deleted", 1)