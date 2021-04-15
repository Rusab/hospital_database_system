# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:48:23 2021

@author: Rusab
"""


import dbfunctions as db
import dbsubprograms as dsub

table_fields = {'doctorsmanagement' : ["Doctor id: ", "Doctor Name: ", "Sex: ", "Expertise: ", "Degree: ", "Position: ", "Chamber: ", "Time: ", "Fee: ", "Contact no: ", "Email: "]}

view_ports = {'dview:doctorsmanagement': ["docid", "name", "sex", "expertise", "degree", "position", "chamber", "time", "fee", "contactno", "email"]}

insert_scope = {'dview:doctorsmanagement': ["name", "sex", "expertise", "degree", "position", "chamber", "time", "fee", "contactno", "email"], 
                'admin-doc:roomduty': ["docid", "roomid", "date", "time"]}

room = ["Ward", "Cabin", "Emergency", "Outdoor", "ICU", "OT"]

table_name = 'doctorsmanagement'



while(True):
    
    print("\nWelcome to Panda Hospital Database \nLogin As:")
      
    login = db.choice_make("Doctor", "Staff", "Patient", "Central Admin", "Cancel")
    
    
    if login == 1:
        while(True):
            x = int(input("1. View Schedule\n2. Patient Infromation\n3. Doctor Information\n4. Staff information\n6. Cancel"))

    elif login == 2:
        while(True):
            x = int(input("1. Add new entry\n2. See all entries\n3. Delete entry\n4. View entry\n5. Update entry\n6. Cancel"))
        
    elif login == 3:
        while(True):
            x = int(input("1. Add new entry\n2. See all entries\n3. Delete entry\n4. View entry\n5. Update entry\n6. Cancel"))
        
    elif login == 4:     
        while(True):
            
            x = db.choice_make("Add new entry", "See all entries", "Delete entry", "View entry", "Update entry", "Cancel")
            
            if x == 1:
                while(True):
                    print("Which Database to do you want to add to: ")
                    p = db.choice_make("Doctor", "Patient", "Staff", "Medical Supplies & Diagnostics", "Room", "Back")
                    
                    if p == 1:
                        while(True):
                            p = db.choice_make("Doctor Information", "Duty Schedule", "Back")
                            
                            if p == 1:
                                dsub.doctor_entry()
                                
                            elif p == 2: 
                                dsub.roomduty_entry()
                                
                            else:
                                break
                    elif p == 2:
                        while(True):
                            p = db.choice_make("Patient Information", "Admission & Emergency Infromation", "Prescription", "Diagnostic Reports", "Back")
                            if p == 1:
                                dsub.patient_entry()
                            elif p == 2:
                                while(True):
                                    p = db.choice_make("Outdoor/Emergency Registry", "Patient Admission", "Back")
                                    if p == 1:
                                        dsub.emergency_patient()
                                    elif p == 2:
                                        dsub.patient_admission()
                                    else:
                                        break
                                
                                
                            elif p == 3:
                                dsub.prescription()
                                
                            elif p == 4:
                                dsub.reports()
                                
                            else:
                                break
                    elif p == 3:
                        while(True):
                            p = db.choice_make("Staff Information", "Duty Schedule", "Back")
                            
                            if p == 1:
                                dsub.staff_entry()
                                
                            elif p == 2:
                                dsub.roomduty_entry_staff()
                            
                            else:
                                break
                    
                    elif p == 4:
                        p = db.choice_make("Medicine", "Medical Equipment", "Diagnostic tests", "Back")
                        
                        if p == 1:
                            dsub.med_entry()
                            
                        elif p == 2:
                            dsub.equip_entry()
                            
                        elif p == 3:
                            dsub.test_entry()
                            
                        else:
                            break
                        
                    elif p == 5:
                        dsub.room_entry()
                    
                    else:
                        break
                            
                        
                            
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
        
    else:
        break
    




#insert_data('doctorsmanagement', name, expertise, degree, position, chamber, time, fee, contactno, ids)





    

    

