# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:24:14 2021

@author: Rusab
"""


import dbfunctions as db

table_fields = {'doctorsmanagement' : ["Doctor id: ", "Doctor Name: ", "Sex: ", "Expertise: ", "Degree: ", "Position: ", "Chamber: ", "Time: ", "Fee: ", "Contact no: ", "Email: "]}

view_ports = {'dview:doctorsmanagement': ["docid", "name", "sex", "expertise", "degree", "position", "chamber", "time", "fee", "contactno", "email"]}

insert_scope = {'dview:doctorsmanagement': ["name", "sex", "expertise", "degree", "position", "chamber", "time", "fee", "contactno", "email"], 
                'admin-doc:roomduty': ["docid", "roomid", "date", "time"],
                'admin-staff:roomduty': ["staffid", "roomid", "date", "time"],
                'admin-patient:patientmanagement': ["name", "sex", "age", "bloodgroup", "medicalhistory", "address", "contactno", "email"],
                'patinet:outdoor-emergency': ["patientid", "docid", "date", "time"],
                'admin:admission': ["patientid", "admissionstat","roomid", "bedno", "docid",  "admissiondate", "admissiontime", "releasedate", "releasetime"],
                'admin:prescription': ["patientid", "docid", "diagnosis", "medid", "testid", "date", "time"],
                'admin:report': ["patientid", "docid", "testid", "date", "time", "report"],
                'admin:staffmanagemnet': ["name", "sex", "age", "position", "contactno", "email", "salary"],
                'medicine':["brandname", "genericname", "manufecturer", "literature", "stock"],
                'medequipment': ["name", "stock"],
                'diagnostictests': ["name", "roomid"],
                'room': ["roomtype", "bedcount"]}

room = ["Ward", "Cabin", "Emergency", "Outdoor", "ICU", "OT"]

table_name = 'doctorsmanagement'

def doctor_entry():
    table_name = 'doctorsmanagement'
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
    email = db.quote_str(input("Email: "))
    
    data = db.list_make(name, sex, expertise, position, chamber, degree, time, fee, contactno, email)
    
    db.insert_data(table_name, insert_scope['dview:doctorsmanagement'], data ) 

def roomduty_entry():
    table_name = 'roomduty'
    
    docid = input("Enter Doctor id: ")
    roomid = input("Enter Room id: ")
    date = db.quote_str(db.date_process(input("Enter Date (DD-MM-YYYY): ")))
    print(date)
    time = db.quote_str(input("Enter time: "))
    
    #Where to start from
    data = db.list_make(docid, roomid, date, time)
    
    db.insert_data(table_name, insert_scope['admin-doc:roomduty'], data)
    
def patient_entry():
    table_name = 'patientmanagement'
    print("Enter the following data: \n")
    name = db.quote_str(input("Patient Name: "))
    sex = db.quote_str(input("Sex: "))
    age = input("Age: ")
    bloodgroup = db.quote_str(input("Blood Group: "))
    medicalhistory = db.quote_str(input("Medical History: "))
    address = db.quote_str(input("Address: "))
    contactno = db.quote_str( input("Phone number: "))
    email = db.quote_str(input("Email: "))
    
    
    data = db.list_make(name, sex, age, bloodgroup, medicalhistory, address, contactno, email)
    
    db.insert_data(table_name, insert_scope['admin-patient:patientmanagement'], data )     

def emergency_patient():
    patid = input("Enter Patient ID: ")
    docid = input("Enter Doctor ID: ")
    date = db.quote_str(db.date_process(input("Enter Date (DD-MM-YYYY): ")))
    time = db.quote_str(input("Enter time: "))
    print("Where did the patient come ? ")
    roomtype = db.choice_make("Emergency", "Outdoor")
    
    data = db.list_make(patid, docid, date, time)
    
    if roomtype == 1:
        db.insert_data('emergency', insert_scope['patinet:outdoor-emergency'], data )     
    elif roomtype == 2:
        db.insert_data('outdoor', insert_scope['patinet:outdoor-emergency'], data )  
        
def patient_admission():
    table_name = 'admission'
    patid = input("Enter Patient ID: ")
    docid = input("Enter Doctor ID: ")
    roomid = input("Enter Room ID: ")
    bedno = input("Enter Bed no: ")
    admitdate = db.quote_str(db.date_process(input("Enter Admission Date (DD-MM-YYYY): ")))
    admittime = db.quote_str(input("Enter Admission time: "))
    redate = db.quote_str(db.date_process(input("Enter Release Date (DD-MM-YYYY): ")))
    retime = db.quote_str(input("Enter Release time: "))
    
    data = db.list_make(patid, "1", roomid, bedno, docid, admitdate, admittime, redate, retime)
    
    db.insert_data(table_name, insert_scope['admin:admission'], data) 
    
def prescription():
    table_name = 'prescription'
    patid = input("Enter Patient ID: ")
    docid = input("Enter Doctor ID: ")
    diagnosis = db.quote_str(input("Diagnosis: "))
    medid = input("Enter Med ID: ")
    testid = input("Enter Test ID: ")
    if len(medid) == 0:
        medid = "NULL"
    if len(testid) == 0:
        testid = "NULL"
    date = db.quote_str(db.date_process(input("Enter Date (DD-MM-YYYY): ")))
    time = db.quote_str(input("Enter time: "))
    
    data = db.list_make(patid, docid, diagnosis, medid, testid, date, time)
    
    db.insert_data(table_name, insert_scope['admin:prescription'], data) 
    
    # Need to add med and test list
    
def reports():
    table_name = 'diagnosticreport'
    patid = input("Enter Patient ID: ")
    docid = input("Enter Doctor ID: ")
    testid = input("Enter Test ID: ")
    date = db.quote_str(db.date_process(input("Enter Date (DD-MM-YYYY): ")))
    time = db.quote_str(input("Enter time: "))
    report = db.quote_str(input("Report: "))
    
    data = db.list_make(patid, docid, testid, date, time, report)
    
    db.insert_data(table_name, insert_scope['admin:report'], data)     
    
def staff_entry():
    table_name = 'staffmanagement'
    name = db.quote_str(input("Staff Name: "))
    sex = db.quote_str(input("Sex: "))
    age = input("Age: ")
    position = db.quote_str(input("Position: "))
    contactno = db.quote_str( input("Phone number: "))
    email = db.quote_str(input("Email: "))
    salary = input("Salary: ")
    
    data = db.list_make(name, sex, age, position, contactno, email, salary)
    
    db.insert_data(table_name, insert_scope['admin:staffmanagemnet'], data)    
    
def roomduty_entry_staff():
    table_name = 'roomduty'
    
    staffid = input("Enter Staff id: ")
    roomid = input("Enter Room id: ")
    date = db.quote_str(db.date_process(input("Enter Date (DD-MM-YYYY): ")))
    time = db.quote_str(input("Enter time: "))
    
    #Where to start from
    data = db.list_make(staffid, roomid, date, time)
    
    db.insert_data(table_name, insert_scope['admin-staff:roomduty'], data)
    
def med_entry():
    table_name = 'medicine'
    
    brandname = db.quote_str(input("Brand Name: "))
    genname = db.quote_str(input("Generic Name: "))
    manufecturer = db.quote_str(input("Manufecturer Name: "))
    literature = db.quote_str(input("Literature: "))
    stock= input("Stock: ")
    
    data = db.list_make(brandname, genname, manufecturer, literature, stock)
    
    db.insert_data(table_name, insert_scope['medicine'], data)
    
def equip_entry():
    table_name = 'medequipment'

    name = db.quote_str(input("Equipment Name: "))
    stock= input("Stock: ")
    
    data = db.list_make(name, stock)
    db.insert_data(table_name, insert_scope['medequipment'], data)
    
def test_entry():
    table_name = 'diagnostictests'
    
    name = db.quote_str(input("Test Name: "))
    roomid = input("Enter Room id: ")
    
    #Where to start from
    data = db.list_make(name, roomid)
    
    db.insert_data(table_name, insert_scope['diagnostictests'], data)
    
def room_entry():   
    table_name = 'room'
    
    roomtype = db.quote_str(input("Room Type: "))
    bedcount = input("Bedcount: ")
    
    data = db.list_make(roomtype, bedcount)
    
    db.insert_data(table_name, insert_scope['room'], data)
        
    
    
    

    

    
    


    
    
    
    
    
    
    
        
        