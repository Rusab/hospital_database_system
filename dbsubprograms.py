# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:24:14 2021

@author: Rusab
"""


import dbfunctions as db

table_fields = {'doctorsmanagement' : ["Doctor id: ", "Doctor Name: ", "Sex: ", "Expertise: ", "Degree: ", "Position: ", "Chamber: ", "Time: ", "Fee: ", "Contact no: ", "Email: "],
                'patientmanagement': ["Patient ID: ", "Patient Name: ", "Sex: ", 'Age: ', 'Bloodgroup: ', "Medical History: ", "Address: ", "Contact No: ", "Email: "],
                'admin:last-pres': ["Prescription No: ", "Diagnosis: ", "Date: ", "Time: ", "Prescribed Medicine: ", "Prescribed Tests: ","Prescribed By: ", "Department: "],
                'admin:last-rep': ["Prescription No: ", "Test Name: ", "Report Summary: ", "Date: ", "Time: ", "Report prepared by: ", "Department: "],
                'admin:outdoor': ["Patient ID: ", "Patient Name: ", "Sex: ", "Age: ", "Blood Group: ", "Contact No: ", "Visit Date: ", "Visit Time: ", "Duty Doctor: ","Doctor ID: ", "Department: "],
                'admin:emergency': ["Patient ID: ", "Patient Name: ", "Sex: ", "Age: ", "Blood Group: ", "Contact No: ", "Visit Date: ", "Visit Time: ", "Duty Doctor: ","Doctor ID: ", "Department: "],
                'admin:admission': ["Patient ID: ", "Patient Name: ", "Sex: ", "Age: ", "Blood Group: ", "Contact No: ", "Admission Status: ", "Admission Date: ", "Admission Time: ", "Room No: ", "Room Type: ", "Bed No: ", "Release Date: ", "Release Time: ", "Admitted Under: ","Doctor ID: ", "Department of "],
                'admin:prescription': ["Prescription No: ", "Patient ID: ", "Patient Name: ", "Sex: ", "Age: ", "Blood Group: ", "Date: ", "Time: ", "Diagnosis: ", "Prescribed Medicine: ", "Prescribed Tests: ","Prescribed By: ", "Doctor ID: ", "Department of "],
                'admin:report': ["Prescription No: ", "Patient ID: ", "Patient Name: ", "Sex: ", "Age: ", "Blood Group: ", "Test Name: ", "Report Summary: ", "Date: ", "Time: ", "Report prepared by: ", "Department: "],
                'admin:staffmanagement' : ["Staff id: ", "Staff Name: ", "Sex: ", "Age: ", "Position:  ", "Contact no: ", "Email: ", "Salary: "],
                'admin:staffduty': ["Staffid: ", "Staff Name: ", "Position: ", "Room No: ", "Date: ", "Time: "],
                'admin:docduty': ["Doctor id: ", "DoctorName: ", "Department: ", "Position: ", "Room No: ", "Date: ", "Time: "],
                'medicine':["Med id: ", "Brand Name: ", "Generic Name: ", "Manufecturer: ", "Litarature: ", "Stock: "],
                'medequipment': ["Equipment ID: ", "Equipment Name: ", "Stock: "],
                'diagnostictests': ["Test ID: ", "Test Name: ", "Room No: "],
                'room': ["Room No: ", "Room Type: ", "Number of Beds: "]}

view_ports = {'dview:doctorsmanagement': ["docid", "name", "sex", "expertise", "degree", "position", "chamber", "time", "fee", "contactno", "email"],
              'admin:patientmanagement': ["patientid","name", "sex", "age", "bloodgroup", "medicalhistory", "address",  "contactno", "email"],
              'admin:last-pres': ["prescription.presid", "prescription.diagnosis", "prescription.date", "prescription.time", "medicine.brandname", "diagnostictests.name","doctorsmanagement.name", "doctorsmanagement.expertise"],
              'admin:last-rep': ["prescription.presid", "diagnostictests.name", "diagnosticreport.report", "diagnosticreport.date", "diagnosticreport.time", "doctorsmanagement.name", "doctorsmanagement.expertise"],
              'admin:outdoor': ["patientmanagement.patientid", "patientmanagement.name", "patientmanagement.sex", "patientmanagement.age", "patientmanagement.bloodgroup", "patientmanagement.contactno", "outdoor.date", "outdoor.time", "doctorsmanagement.name","doctorsmanagement.docid", "doctorsmanagement.expertise"],
              'admin:emergency': ["patientmanagement.patientid", "patientmanagement.name", "patientmanagement.sex", "patientmanagement.age", "patientmanagement.bloodgroup", "patientmanagement.contactno", "emergency.date", "emergency.time", "doctorsmanagement.name","doctorsmanagement.docid", "doctorsmanagement.expertise"],
              'admin:admission': ["patientmanagement.patientid", "patientmanagement.name", "patientmanagement.sex", "patientmanagement.age", "patientmanagement.bloodgroup", "patientmanagement.contactno", "admission.admissionstat", "admission.admissiondate", "admission.admissiontime", "room.roomid", "room.roomtype", "admission.bedno",  "admission.releasedate",  "admission.releasetime", "doctorsmanagement.name","doctorsmanagement.docid", "doctorsmanagement.expertise"],
              'admin:prescription': ["prescription.presid", "patientmanagement.patientid", "patientmanagement.name", "patientmanagement.sex", "patientmanagement.age", "patientmanagement.bloodgroup",  "prescription.date", "prescription.time", "prescription.diagnosis", "medicine.brandname", "diagnostictests.name", "doctorsmanagement.name", "doctorsmanagement.docid", "doctorsmanagement.expertise"],
              'admin:report': ["prescription.presid", "patientmanagement.patientid", "patientmanagement.name", "patientmanagement.sex", "patientmanagement.age", "patientmanagement.bloodgroup", "diagnostictests.name", "diagnosticreport.report", "diagnosticreport.date", "diagnosticreport.time", "doctorsmanagement.name", "doctorsmanagement.expertise"],
              'admin:staffmanagement': ["staffid", "name", "sex", "age", "position", "contactno", "email", "salary"],
              'admin:staffduty': ["roomduty.staffid", "staffmanagement.name", "staffmanagement.position", "roomduty.roomid", "roomduty.date", "roomduty.time"],
              'admin:docduty': ["roomduty.docid", "doctorsmanagement.name", "doctorsmanagement.expertise", "doctorsmanagement.position","roomduty.roomid", "roomduty.date", "roomduty.time"],
              'medicine':["medid", "brandname", "genericname", "manufecturer", "literature", "stock"],
              'medequipment': ["equipid", "name", "stock"],
              'diagnostictests': ["testid", "name", "roomid"],
              'room': ["roomid", "roomtype", "bedcount"]}

select_ports = {'dview:doctorsmanagement': ["docid", "name", "sex", "expertise", "degree", "position", "chamber", "time", "fee", "contactno", "email"],
                'drange:doctorsmanagement': ["docid", "name", "fee"],
                'admin:patientmanagement': ["patientid", "name", "sex", "age", "bloodgroup", "contactno", "email"],
                'drange:patientmanagement': ["patientid", "name", "age"],
                'outdoor:admin': ["patientid", "docid", "date"],
                'emergency:admin': ["patientid", "docid", "date"],
                'admission:admin': ["patientid", "docid", "admissiondate", "releasedate", "admissionstat"],
                'admin:prescription': ["presid", "patientid", "docid", "date"],
                'admin:report': ["presid", "patientid", "docid", "date"],
                'admin:staffmanagement': ["staffid", "name", "sex", "age", "position", "contactno", "email", "salary"],
                'admin:staffduty': ["staffid", "roomid", "date", "time"],
                'admin:docduty': ["docid", "roomid", "date", "time"],
                'medicine':["medid", "brandname", "genericname", "manufecturer", "stock"],
                'medequipment': ["equipid", "name", "stock"],
                'diagnostictests': ["testid", "name", "roomid"],
                'room': ["roomid", "roomtype", "bedcount"]}


insert_scope = {'dview:doctorsmanagement': ["name", "sex", "expertise", "degree", "position", "chamber", "time", "fee", "contactno", "email"], 
                'admin-doc:roomduty': ["docid", "roomid", "date", "time"],
                'admin-staff:roomduty': ["staffid", "roomid", "date", "time"],
                'admin-patient:patientmanagement': ["name", "sex", "age", "bloodgroup", "medicalhistory", "address", "contactno", "email"],
                'patinet:outdoor-emergency': ["patientid", "docid", "date", "time"],
                'admin:admission': ["patientid", "admissionstat","roomid", "bedno", "docid",  "admissiondate", "admissiontime", "releasedate", "releasetime"],
                'admin:prescription': ["patientid", "docid", "diagnosis", "medid", "testid", "date", "time"],
                'admin:report': ["presid", "docid", "date", "time", "report"],
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
    degree = db.quote_str(input("Degree: "))
    position = db.quote_str(input("Position: "))
    chamber = db.quote_str(input("Chamber Location: "))
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
    presid = input("Enter Prescription ID: ")
    docid = input("Enter Doctor ID: ")
    date = db.quote_str(db.date_process(input("Enter Date (DD-MM-YYYY): ")))
    time = db.quote_str(input("Enter time: "))
    report = db.quote_str(input("Report: "))
    
    data = db.list_make(presid, docid, date, time, report)
    
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
        
    
def doctor_view_admin():
    table_name = ['doctorsmanagement']
    
    another = "Y"
    field_array = []
    data_array = []
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports['dview:doctorsmanagement'])
        
        field_name =  select_ports['dview:doctorsmanagement'][f_no - 1]
        
        field_array.append(field_name)
        
        data = db.quote_str(input("Enter {field}: ".format(field = select_ports['dview:doctorsmanagement'][f_no - 1])))
        
        data_array.append(data)
        
        another = input("Do you want to enter another field ? [Y/N]")
    
        
    db.view_entry(table_name, field_array, data_array, select_ports['dview:doctorsmanagement'], table_fields['doctorsmanagement'])  
    
    
def doctor_range_admin():
    table_name = ['doctorsmanagement']
    
    another = "Y"
    field_array = []
    data_array = []
    inequality_array =[]
    
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports['drange:doctorsmanagement'])
        
        
        
        data_lesser = db.quote_str(input("{field} > ".format(field = select_ports['drange:doctorsmanagement'][f_no - 1])))
                
        if data_lesser != '""' :
            data_array.append(data_lesser)
            field_array.append(select_ports['drange:doctorsmanagement'][f_no - 1])
            inequality_array.append(" > ")
        
        data_greater = db.quote_str(input("{field} < ".format(field = select_ports['drange:doctorsmanagement'][f_no - 1])))
        
        if data_greater != '""' :
            data_array.append(data_greater)
            field_array.append(select_ports['drange:doctorsmanagement'][f_no - 1])
            inequality_array.append(" < ")
    
       
        another = input("Do you want to enter another field ? [Y/N]")
    
       
    db.view_range(table_name, field_array, data_array, view_ports['dview:doctorsmanagement'], table_fields[table_name[0]], inequality_array)  
    
    
    
def patient_view_admin():
    table_name = ['patientmanagement']
    another = "Y"
    field_array = []
    data_array = []
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports['admin:patientmanagement'])
        
        field_name =  select_ports['admin:patientmanagement'][f_no - 1]
        
        field_array.append(field_name)
        
        data = db.quote_str(input("Enter {field}: ".format(field = select_ports['admin:patientmanagement'][f_no - 1])))
        
        data_array.append(data)
        
        another = input("Do you want to enter another field ? [Y/N]")
    
        
    db.view_entry(table_name, field_array, data_array, view_ports['admin:patientmanagement'], table_fields['patientmanagement'])  
    print("\nLatest Prescription: ")
    delete_check = ['prescription', 'patientmanagement', 'doctorsmanagement']
    combo = [ ["prescription", 'patientmanagement', "patientid"], ["prescription", "doctorsmanagement", "docid"], ["prescription", "diagnostictests", "testid"], ["prescription", "medicine", "medid"]]
    db.view_entry(delete_check, field_array, data_array, view_ports['admin:last-pres'], table_fields['admin:last-pres'], combo, "prescription.date")
    
    print("\nLatest Report: ")
    delete_check = ['prescription', 'patientmanagement']
    combo = [ ["prescription", 'patientmanagement', "patientid"], ["prescription", "diagnosticreport", "presid"], ["prescription", "diagnostictests", "testid"], ["diagnosticreport", "doctorsmanagement", "docid"]]
    db.view_entry(delete_check, field_array, data_array, view_ports['admin:last-rep'], table_fields['admin:last-rep'], combo, "prescription.date")
    
def patient_range_admin():
    table_name = ['patientmanagement']
    another = "Y"
    field_array = []
    data_array = []
    inequality_array =[]
    
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports['drange:patientmanagement'])
        
        field_name =  select_ports['drange:patientmanagement'][f_no - 1]
        
        field_array.append(field_name)
        
        data_lesser = db.quote_str(input("{field} > ".format(field = field_name)))
                
        if data_lesser != '""' :
            data_array.append(data_lesser)
            field_array.append(field_name)
            inequality_array.append(" > ")
        
        data_greater = db.quote_str(input("{field} < ".format(field = field_name)))
        
        if data_greater != '""' :
            data_array.append(data_greater)
            field_array.append(field_name)
            inequality_array.append(" < ")
    
        
        another = input("Do you want to enter another field ? [Y/N]")
        
        
        
    db.view_range(table_name, field_array, data_array, view_ports['admin:patientmanagement'], table_fields['patientmanagement'], inequality_array)  
    
def outdoor_view_admin():

    another = "Y"
    field_array = []
    data_array = []
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports['outdoor:admin'])
        
        field_name =  select_ports['outdoor:admin'][f_no - 1]
        
        field_array.append(field_name)
        
        if field_name == "date":
           data = db.quote_str(db.date_process(input("Enter Date(DD-MM-YYYY): ")))
        
        else:
            data = db.quote_str(input("Enter {field}: ".format(field = select_ports['outdoor:admin'][f_no - 1])))
        
        data_array.append(data)
        
        another = input("Do you want to enter another field ? [Y/N]")
    
        
  
    delete_check = ['outdoor', 'patientmanagement', 'doctorsmanagement']
    combo = [ ["outdoor", 'patientmanagement', "patientid"], ["outdoor", "doctorsmanagement", "docid"]]
    db.view_entry(delete_check, field_array, data_array, view_ports['admin:outdoor'], table_fields['admin:outdoor'], combo)
    
def outdoor_range_admin():

    another = "Y"
    field_array = []
    data_array = []
    inequality_array =[]
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports['outdoor:admin'])
        
        field_name =  select_ports['outdoor:admin'][f_no - 1]
               
        
        if field_name == "date":
           data_lesser = db.quote_str(db.date_process(input("Date(DD-MM-YYYY) > ")))
        
        else:        
            data_lesser = db.quote_str(input("{field} > ".format(field = field_name)))
                
        if data_lesser != '""' :
            data_array.append(data_lesser)
            field_array.append(field_name)
            inequality_array.append(" > ")
            
        if field_name == "date":
         data_greater = db.quote_str(db.date_process(input("Enter Date(DD-MM-YYYY) < ")))
        
        else:      
            data_greater = db.quote_str(input("{field} < ".format(field = field_name)))
        
        if data_greater != '""' :
            data_array.append(data_greater)
            field_array.append(field_name)
            inequality_array.append(" < ")
        
        another = input("Do you want to enter another field ? [Y/N]")
    
        
  
    delete_check = ['outdoor', 'patientmanagement', 'doctorsmanagement']
    combo = [ ["outdoor", 'patientmanagement', "patientid"], ["outdoor", "doctorsmanagement", "docid"]]
    db.view_range(delete_check, field_array, data_array, view_ports['admin:outdoor'], table_fields['admin:outdoor'], inequality_array, combo)
    
def emergency_view_admin():

    another = "Y"
    field_array = []
    data_array = []
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports['emergency:admin'])
        
        field_name =  select_ports['emergency:admin'][f_no - 1]
        
        field_array.append(field_name)
        
        if field_name == "date":
           data = db.quote_str(db.date_process(input("Enter Date(DD-MM-YYYY): ")))
        
        else:
            data = db.quote_str(input("Enter {field}: ".format(field = select_ports['emergency:admin'][f_no - 1])))
        
        data_array.append(data)
        
        another = input("Do you want to enter another field ? [Y/N]")
    
        
  
    delete_check = ['emergency', 'patientmanagement', 'doctorsmanagement']
    combo = [ ["emergency", 'patientmanagement', "patientid"], ["emergency", "doctorsmanagement", "docid"]]
    db.view_entry(delete_check, field_array, data_array, view_ports['admin:emergency'], table_fields['admin:emergency'], combo)
    
def emergency_range_admin():

    another = "Y"
    field_array = []
    data_array = []
    inequality_array =[]
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports['emergency:admin'])
        
        field_name =  select_ports['emergency:admin'][f_no - 1]
               
        
        if field_name == "date":
           data_lesser = db.quote_str(db.date_process(input("Date(DD-MM-YYYY) > ")))
        
        else:        
            data_lesser = db.quote_str(input("{field} > ".format(field = field_name)))
                
        if data_lesser != '""' :
            data_array.append(data_lesser)
            field_array.append(field_name)
            inequality_array.append(" > ")
            
        if field_name == "date":
         data_greater = db.quote_str(db.date_process(input("Enter Date(DD-MM-YYYY) < ")))
        
        else:      
            data_greater = db.quote_str(input("{field} < ".format(field = field_name)))
        
        if data_greater != '""' :
            data_array.append(data_greater)
            field_array.append(field_name)
            inequality_array.append(" < ")
        
        another = input("Do you want to enter another field ? [Y/N]")
    
        
  
    delete_check = ['emergency', 'patientmanagement', 'doctorsmanagement']
    combo = [ ["emergency", 'patientmanagement', "patientid"], ["emergency", "doctorsmanagement", "docid"]]
    db.view_range(delete_check, field_array, data_array, view_ports['admin:emergency'], table_fields['admin:emergency'], inequality_array, combo)
    
def admission_view_admin():

    another = "Y"
    field_array = []
    data_array = []
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports['admission:admin'])
        
        field_name =  select_ports['admission:admin'][f_no - 1]
        
        field_array.append(field_name)
        
        if field_name == "admissiondate" or field_name == "releasedate":
           data = db.quote_str(db.date_process(input("Enter Date(DD-MM-YYYY): ")))
        
        else:
            data = db.quote_str(input("Enter {field}: ".format(field = select_ports['admission:admin'][f_no - 1])))
        
        data_array.append(data)
        
        another = input("Do you want to enter another field ? [Y/N]")
    
        
  
    delete_check = ['admission', 'patientmanagement', 'doctorsmanagement', 'room']
    combo = [ ["admission", 'patientmanagement', "patientid"], ["admission", "doctorsmanagement", "docid"], ["admission", "room", "roomid"]]
    db.view_entry(delete_check, field_array, data_array, view_ports['admin:admission'], table_fields['admin:admission'], combo)
    
    
def admission_range_admin():

    another = "Y"
    field_array = []
    data_array = []
    inequality_array =[]
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports['admission:admin'])
        
        field_name =  select_ports['admission:admin'][f_no - 1]
               
        
        if field_name == "admissiondate" or field_name == "releasedate":
           data_lesser = db.quote_str(db.date_process(input("Date(DD-MM-YYYY) > ")))
        
        else:        
            data_lesser = db.quote_str(input("{field} > ".format(field = field_name)))
                
        if data_lesser != '""' :
            data_array.append(data_lesser)
            field_array.append(field_name)
            inequality_array.append(" > ")
            
        if field_name == "admissiondate" or field_name == "releasedate":
         data_greater = db.quote_str(db.date_process(input("Enter Date(DD-MM-YYYY) < ")))
        
        else:      
            data_greater = db.quote_str(input("{field} < ".format(field = field_name)))
        
        if data_greater != '""' :
            data_array.append(data_greater)
            field_array.append(field_name)
            inequality_array.append(" < ")
        
        another = input("Do you want to enter another field ? [Y/N]")
    
        
  
    delete_check = ['admission', 'patientmanagement', 'doctorsmanagement']
    combo = [ ["admission", 'patientmanagement', "patientid"], ["admission", "doctorsmanagement", "docid"], ["admission", "room", "roomid"]]
    db.view_range(delete_check, field_array, data_array, view_ports['admin:admission'], table_fields['admin:admission'], inequality_array, combo)
    
    
def generic_view_value(select_ports, view_ports, table_fields, delete_check, combo, datefield1="", datefield2="", jointype = "LEFT JOIN"):

    another = "Y"
    field_array = []
    data_array = []
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports)
        
        field_name =  select_ports[f_no - 1]
        
        field_array.append(field_name)
        
        if field_name == datefield1 or field_name == datefield2:
           data = db.quote_str(db.date_process(input("Enter Date(DD-MM-YYYY): ")))
        
        else:
            data = db.quote_str(input("Enter {field}: ".format(field = select_ports[f_no - 1])))
        
        data_array.append(data)
        
        another = input("Do you want to enter another field ? [Y/N]")
    
        
    db.view_entry(delete_check, field_array, data_array, view_ports, table_fields, combo)
    
    
def generic_view_range(select_ports, view_ports, table_fields, delete_check, combo, datefield1="", datefield2="", jointype = "LEFT JOIN"):

    another = "Y"
    field_array = []
    data_array = []
    inequality_array =[]
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports)
        
        field_name =  select_ports[f_no - 1]
        
        if field_name == datefield1 or field_name == datefield2:
           data_lesser = db.quote_str(db.date_process(input("Date(DD-MM-YYYY) > ")))
        
        else:        
            data_lesser = db.quote_str(input("{field} > ".format(field = field_name)))
                
        if data_lesser != '""' :
            data_array.append(data_lesser)
            field_array.append(field_name)
            inequality_array.append(" > ")
            
        if field_name == datefield1 or field_name == datefield2:
         data_greater = db.quote_str(db.date_process(input("Enter Date(DD-MM-YYYY) < ")))
        
        else:      
            data_greater = db.quote_str(input("{field} < ".format(field = field_name)))
        
        if data_greater != '""' :
            data_array.append(data_greater)
            field_array.append(field_name)
            inequality_array.append(" < ")
        
        another = input("Do you want to enter another field ? [Y/N]")
    
        
    db.view_range(delete_check, field_array, data_array, view_ports, table_fields, inequality_array, combo, jointype = jointype)
    


def generic_view_singletable(select_ports, view_ports, table_fields, table):
    table_name = [table]
    
    another = "Y"
    field_array = []
    data_array = []
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports)
        
        field_name =  select_ports[f_no - 1]
        
        field_array.append(field_name)
        
        if field_name == "date":
           data = db.quote_str(db.date_process(input("Enter Date(DD-MM-YYYY): ")))
        
        else:
            data = db.quote_str(input("Enter {field}: ".format(field = select_ports[f_no - 1])))
        
        data_array.append(data)
        
        another = input("Do you want to enter another field ? [Y/N]")
    
        
    db.view_entry(table_name, field_array, data_array ,select_ports, table_fields)  

def generic_range_singletable(select_ports, view_ports, table_fields, table):
    table_name = [table]
    
    another = "Y"
    field_array = []
    data_array = []
    inequality_array =[]
    
    while(another.lower() == "y"):
        print("Enter field: \n")
        f_no = db.select_make(select_ports)
        
        field_name =  select_ports[f_no - 1]
 
        if field_name == "date":
           data_lesser = db.quote_str(db.date_process(input("Date(DD-MM-YYYY) > ")))
        
        else:         
            data_lesser = db.quote_str(input("{field} > ".format(field = field_name)))
                
        if data_lesser != '""' :
            data_array.append(data_lesser)
            field_array.append(field_name)
            inequality_array.append(" > ")
            
        if field_name == "date":
            data_greater = db.quote_str(db.date_process(input("Enter Date(DD-MM-YYYY) < ")))
            
        else:
            data_greater = db.quote_str(input("{field} < ".format(field = field_name)))
        
        if data_greater != '""' :
            data_array.append(data_greater)
            field_array.append(field_name)
            inequality_array.append(" < ")
    
       
        another = input("Do you want to enter another field ? [Y/N]")
    
       
    db.view_range(table_name, field_array, data_array, view_ports, table_fields, inequality_array)  


    
    
    
    
    
    
    
        
        