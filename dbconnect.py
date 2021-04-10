# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:48:23 2021

@author: Rusab
"""

import MySQLdb
try:
    con = MySQLdb.connect("localhost","root","","HospitalDatabase")
except:
    print("Can't Connect")
print("Connected")

cur = con.cursor()
cur.execute("INSERT INTO doctorsmanagement(Name, Expertise, Degree, Position, Chamber, Time, Fee, Contactno, id) VALUES ('Tushi panda', 'Nephrology', 'MBBS', 'Dept Head', '1st Floor', '12:24', 1200, '0132523582', 2);")
con.commit()
cur.execute("SELECT * FROM doctorsmanagement;")

data = cur.fetchone()

print(data)

cur.close()
con.close()


