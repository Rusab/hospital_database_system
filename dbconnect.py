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
    
    print("\nWelcome to Alpha Hospital Database".upper())
    print("To Navigate in the menu, Please enter the Index number of the option you want to select")
    
    
    print("\nLogin As:")
      
    login = db.choice_make("Doctor", "Patient", "Nurse/Medical Staff", "Central Admin", "Cancel")
    
    
    if login == 1:
         while(True):
            print("\n**** LOGGED IN AS DOCTOR ****\n")
            x = db.choice_make("Add New Information","View Information", "Update Information", "Delete Information", "Cancel")
            
            if x == 1:
                while(True):
                    print("\n**** Add New Information ****\n")
                    print("Which Database to do you want to add to: ")
                    p = db.choice_make("Doctor Information", "Patient Information", "Staff Information", "Medical Supplies", "Back")
                    
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
                        p = db.choice_make("Medicine", "Medical Equipment", "Back")
                        
                        if p == 1:
                            dsub.med_entry()
                            
                        elif p == 2:
                            dsub.equip_entry()
                            
                            
                        else:
                            break

                    else:
                        break
                            
                    

            elif x == 2:
                while(True):
                    print("\n**** View Infromation ****\n")
                    p = db.choice_make("Doctor Infromation", "Patient information", "Staff Infromation", "Medical Supplies & Diagnostics", "Room", "Back")
                    if p == 1:
                        p = db.choice_make("Doctor Infromation", "Duty Schedule", "Back")
                        if p == 1:
                            p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                            if p == 1:
                                dsub.doctor_view_admin()
                            elif p == 2:
                                dsub.doctor_range_admin()
                            elif p == 3:
                                db.view_all(['doctorsmanagement'], dsub.view_ports['dview:doctorsmanagement'], dsub.table_fields['doctorsmanagement'])
                                
                        elif p == 2:
                            p = db.choice_make("Search with value", "Search with range", "View all", "Back")
                            delete_check = ['roomduty', 'doctorsmanagement', 'room']
                            combo = [ ["roomduty", 'doctorsmanagement', "docid"], ["roomduty", "room", "roomid"]]
                            if p == 1:
                                dsub.generic_view_value(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], delete_check, combo, "date", "date") 
                            elif p == 2:
                                table = 'roomduty'
                                dsub.generic_range_singletable(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], table)
                            elif p == 3:
                                db.view_all(delete_check, dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], combo)
                            
                    elif p == 2:
                        while(True):
                            p = db.choice_make("Patient Information", "Admission & Emergency Infromation", "Prescription", "Diagnostic Reports", "Back")
                            if p == 1:
                                p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                if p == 1:      
                                    dsub.patient_view_admin()
                                elif p == 2:
                                    dsub.patient_range_admin()
                                elif p == 3:
                                    db.view_all(['patientmanagement'], dsub.view_ports['admin:patientmanagement'], dsub.table_fields['patientmanagement'])
                        
                            
                            elif p == 2:
                                p = db.choice_make("Patient: Outdoor", "Patient: Emergency", "Patient : Admission", "Back")
                                if p == 1:
                                    p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                    delete_check = ['outdoor', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["outdoor", 'patientmanagement', "patientid"], ["outdoor", "doctorsmanagement", "docid"]]
                                    
                                    if p == 1:
                                        dsub.generic_view_value(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date", "date")
                                        
                                    elif p == 2:
                                        dsub.generic_view_range(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date", "date")
                                        
                                    elif p == 3:
                                        db.view_all(delete_check, dsub.view_ports['outdoor:admin'], dsub.table_fields['outdoor:admin'], combo)
                                
                                elif p == 2:
                                    p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                    delete_check = ['emergency', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["emergency", 'patientmanagement', "patientid"], ["emergency", "doctorsmanagement", "docid"]]
                                    
                                    if p == 1:
                                        dsub.generic_view_value(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date")
                                        
                                    elif p == 2:
                                        dsub.generic_view_range(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date")
                                    elif p == 3:
                                        db.view_all(delete_check, dsub.view_ports['emergency:admin'], dsub.table_fields['emergency:admin'], combo)
                                
                                elif p == 3:
                                    p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                    delete_check = ['admission', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["admission", 'patientmanagement', "patientid"], ["admission", "doctorsmanagement", "docid"], ["admission", "room", "roomid"]]
                                    if p == 1:
                                        
                                        dsub.generic_view_value(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate")
                                    elif p == 2:
                                        dsub.generic_view_range(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate")
                                    elif p == 3:
                                        db.view_all(delete_check, dsub.view_ports['admission:admin'], dsub.table_fields['admission:admin'], combo)
                                    
                            elif p == 3:
                                p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                delete_check = ['prescription', 'patientmanagement', 'doctorsmanagement']
                                combo = [ ["prescription", 'patientmanagement', "patientid"], ["prescription", "doctorsmanagement", "docid"], ["prescription", "medicine", "medid"], ["prescription", "diagnostictests", "testid"]]
                               
                                if p == 1:
                                    dsub.generic_view_value(dsub.select_ports['admin:prescription'], dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], delete_check, combo, "date", "date") 
                                
                                elif p == 2:
                                    dsub.generic_view_range(dsub.select_ports['admin:prescription'], dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], delete_check, combo, "date", "date")
                                elif p == 3:
                                    db.view_all(delete_check, dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], combo)
                            
                            elif p == 4:
                                p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                delete_check = ['prescription', 'patientmanagement', 'diagnosticreport']
                                combo =  [ ["prescription", "diagnosticreport", "presid"], ["prescription", 'patientmanagement', "patientid"],  ["prescription", "diagnostictests", "testid"], ["diagnosticreport", "doctorsmanagement", "docid"]]
                               
                                if p == 1:
                                    dsub.generic_view_value(dsub.select_ports['admin:report'], dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], delete_check, combo, "date", "date") 
                                
                                elif p == 2:
                                    dsub.generic_view_range(dsub.select_ports['admin:report'], dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], delete_check, combo, "date", "date")   
                                
                                elif p == 3:
                                    db.view_all(delete_check, dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], combo)

                            else:
                                break
                            
                    elif p == 3:
                        while(True):
                             p = db.choice_make("Staff Information", "Duty Schedule", "Back")
                             if p == 1:
                                 p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                 if p == 1:
                                     table = 'staffmanagement'
                                     dsub.generic_view_singletable(dsub.select_ports['admin:staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'], table)
                                 elif p == 2:
                                     table = 'staffmanagement'
                                     dsub.generic_range_singletable(dsub.select_ports['admin:staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'], table)
                                 elif p == 3:
                                     db.view_all(['staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'])
                                     
                                     
                             elif p == 2:
                                 p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                 delete_check = ['roomduty', 'staffmanagement', 'room']
                                 combo = [ ["roomduty", 'staffmanagement', "staffid"], ["roomduty", "room", "roomid"]]
                                 if p == 1:
                                     dsub.generic_view_value(dsub.select_ports['admin:staffduty'], dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], delete_check, combo, "date", "date") 
                                 elif p == 2:
                                     dsub.generic_view_range(dsub.select_ports['admin:staffduty'], dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], delete_check, combo, "date", "date") 
                                 elif p == 3:
                                     db.view_all(delete_check, dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], combo)
                            
                             else:
                                break
                             
                    elif p == 4:
                       p = db.choice_make("Medicines", "Medical Equipments", "Diagnostic Tests", "Back")
                       if p == 1:
                           p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                           table = 'medicine'
                           if p == 1:  
                                dsub.generic_view_singletable(dsub.select_ports['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'], table)
                           elif p == 2:
                                dsub.generic_range_singletable(dsub.select_ports['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'], table)
                           elif p == 3:
                                db.view_all(['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'])
                                
                       elif p == 2:
                           p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                           table = 'medequipment'
                           if p == 1:  
                                dsub.generic_view_singletable(dsub.select_ports['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'], table)
                           elif p == 2:
                                dsub.generic_range_singletable(dsub.select_ports['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'], table)
                           elif p == 3:
                                db.view_all(['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'])
                        
                       elif p == 3:
                           p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                           table = 'diagnostictests'
                           if p == 1:  
                                dsub.generic_view_singletable(dsub.select_ports['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'], table)
                           elif p == 2:
                                dsub.generic_range_singletable(dsub.select_ports['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'], table)
                           elif p == 3:
                                db.view_all(['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'])
                                
                    elif p == 5:
                       p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                       table = 'room'
                       if p == 1:  
                            dsub.generic_view_singletable(dsub.select_ports['room'], dsub.view_ports['room'], dsub.table_fields['room'], table)
                       elif p == 2:
                            dsub.generic_range_singletable(dsub.select_ports['room'], dsub.view_ports['room'], dsub.table_fields['room'], table)
                       elif p == 3:
                            db.view_all(['room'], dsub.view_ports['room'], dsub.table_fields['room'])
                            
                    else:
                        break
                        
                                
                            
                    
            #UPDATE                
            elif x == 3:
                while(True):
                    print("\n**** Update Infromation ****\n")
                    p = db.choice_make("Doctor Infromation", "Patient information", "Staff Infromation", "Medical Supplies", "Back")
                    if p == 1:
                        p = db.choice_make("Doctor Infromation", "Duty Schedule", "Back")
                        if p == 1:
                            table = 'doctorsmanagement'
                            dsub.generic_update_singletable(dsub.select_ports['dview:doctorsmanagement'], dsub.view_ports['dview:doctorsmanagement'], dsub.table_fields['doctorsmanagement'], table)
                                
                        elif p == 2:
                            delete_check = ['roomduty', 'doctorsmanagement', 'room']
                            combo = [ ["roomduty", 'doctorsmanagement', "docid"], ["roomduty", "room", "roomid"]]
                            dsub.generic_update_value(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], delete_check, combo, "date", "date") 

                            
                    elif p == 2:
                        while(True):
                            p = db.choice_make("Patient Information", "Admission & Emergency Infromation", "Prescription", "Diagnostic Reports", "Back")
                            if p == 1:
                                table = 'patientmanagement'
                                dsub.generic_update_singletable(dsub.select_ports['admin:patientmanagement'], dsub.view_ports['admin:patientmanagement'], dsub.table_fields['patientmanagement'], table)
                                                       
                            elif p == 2:
                                p = db.choice_make("Patient: Outdoor", "Patient: Emergency", "Patient : Admission", "Back")
                                if p == 1:
                                    delete_check = ['outdoor', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["outdoor", 'patientmanagement', "patientid"], ["outdoor", "doctorsmanagement", "docid"]]
                                    
                                    dsub.generic_update_value(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date", "date")
                                        
                                elif p == 2:
                                    delete_check = ['emergency', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["emergency", 'patientmanagement', "patientid"], ["emergency", "doctorsmanagement", "docid"]]
                                   
                                    dsub.generic_update_value(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date")
                                        
                                elif p == 3:
                                    delete_check = ['admission', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["admission", 'patientmanagement', "patientid"], ["admission", "doctorsmanagement", "docid"], ["admission", "room", "roomid"]]
                                    
                                    dsub.generic_update_value(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate")
                                    
                            elif p == 3:
                                delete_check = ['prescription', 'patientmanagement', 'doctorsmanagement']
                                combo = [ ["prescription", 'patientmanagement', "patientid"], ["prescription", "doctorsmanagement", "docid"], ["prescription", "medicine", "medid"], ["prescription", "diagnostictests", "testid"]]
                               
                                dsub.generic_update_value(dsub.select_ports['admin:prescription'], dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], delete_check, combo, "date", "date") 
                                
                            elif p == 4:
                                delete_check = ['diagnosticreport', 'patientmanagement', 'prescription']
                                combo =  [ ["prescription", "diagnosticreport", "presid"], ["prescription", 'patientmanagement', "patientid"],  ["prescription", "diagnostictests", "testid"], ["diagnosticreport", "doctorsmanagement", "docid"]]
                               
                                dsub.generic_update_value(dsub.select_ports['admin:report'], dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], delete_check, combo, "date", "date") 

                            else:
                                break
                            
                    elif p == 3:
                        while(True):
                             p = db.choice_make("Staff Information", "Duty Schedule", "Back")
                             if p == 1:
                                 table = 'staffmanagement'
                                 dsub.generic_update_singletable(dsub.select_ports['admin:staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'], table)
                                     
                             elif p == 2:
                                 delete_check = ['roomduty', 'staffmanagement', 'room']
                                 combo = [ ["roomduty", 'staffmanagement', "staffid"], ["roomduty", "room", "roomid"]]
                                 dsub.generic_update_value(dsub.select_ports['admin:staffduty'], dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], delete_check, combo, "date", "date") 
                            
                             else:
                                break
                            
                    elif p == 4:
                       while(True):
                            p = db.choice_make("Medicines", "Medical Equipments", "Diagnostic Tests", "Back")
                            if p == 1:
                                table = 'medicine'
                                dsub.generic_update_singletable(dsub.select_ports['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'], table)
                                     
                            elif p == 2:
                                table = 'medequipment'
                                dsub.generic_update_singletable(dsub.select_ports['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'], table)
                             
                            else:
                                break
                    
                    else:
                        break
            # DELETE
            elif x == 4:
                while(True):
                    print("\n**** Delete Infromation ****\n")
                    p = db.choice_make("Doctor Infromation", "Patient information", "Staff Infromation", "Medical Supplies",  "Back")
                    if p == 1:
                        p = db.choice_make("Doctor Infromation", "Duty Schedule", "Back")
                        if p == 1:
                            table = 'doctorsmanagement'
                            dsub.generic_delete_singletable(dsub.select_ports['dview:doctorsmanagement'], dsub.view_ports['dview:doctorsmanagement'], dsub.table_fields['doctorsmanagement'], table )
                                
                        elif p == 2:
                            delete_check = ['roomduty', 'doctorsmanagement', 'room']
                            combo = [ ["roomduty", 'doctorsmanagement', "docid"], ["roomduty", "room", "roomid"]]
                            dsub.generic_delete_value(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], delete_check, combo, "date", "date" ) 

                            
                    elif p == 2:
                        while(True):
                            p = db.choice_make("Patient Information", "Admission & Emergency Infromation", "Prescription", "Diagnostic Reports", "Back")
                            if p == 1:
                                table = 'patientmanagement'
                                dsub.generic_delete_singletable(dsub.select_ports['admin:patientmanagement'], dsub.view_ports['admin:patientmanagement'], dsub.table_fields['patientmanagement'], table )
                                                       
                            elif p == 2:
                                p = db.choice_make("Patient: Outdoor", "Patient: Emergency", "Patient : Admission", "Back")
                                if p == 1:
                                    delete_check = ['outdoor', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["outdoor", 'patientmanagement', "patientid"], ["outdoor", "doctorsmanagement", "docid"]]
                                    
                                    dsub.generic_delete_value(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date", "date" )
                                        
                                elif p == 2:
                                    delete_check = ['emergency', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["emergency", 'patientmanagement', "patientid"], ["emergency", "doctorsmanagement", "docid"]]
                                   
                                    dsub.generic_delete_value(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date" )
                                        
                                elif p == 3:
                                    delete_check = ['admission', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["admission", 'patientmanagement', "patientid"], ["admission", "doctorsmanagement", "docid"], ["admission", "room", "roomid"]]
                                    
                                    dsub.generic_delete_value(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate" )
                                    
                            elif p == 3:
                                delete_check = ['prescription', 'patientmanagement', 'doctorsmanagement']
                                combo = [ ["prescription", 'patientmanagement', "patientid"], ["prescription", "doctorsmanagement", "docid"], ["prescription", "medicine", "medid"], ["prescription", "diagnostictests", "testid"]]
                               
                                dsub.generic_delete_value(dsub.select_ports['admin:prescription'], dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], delete_check, combo, "date", "date" ) 
                                
                            elif p == 4:
                                delete_check = ['diagnosticreport', 'patientmanagement', 'prescription']
                                combo =  [ ["prescription", "diagnosticreport", "presid"], ["prescription", 'patientmanagement', "patientid"],  ["prescription", "diagnostictests", "testid"], ["diagnosticreport", "doctorsmanagement", "docid"]]
                               
                                dsub.generic_delete_value(dsub.select_ports['admin:report'], dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], delete_check, combo, "date", "date" ) 

                            else:
                                break
                            
                    elif p == 3:
                        while(True):
                             p = db.choice_make("Staff Information", "Duty Schedule", "Back")
                             if p == 1:
                                 table = 'staffmanagement'
                                 dsub.generic_delete_singletable(dsub.select_ports['admin:staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'], table )
                                     
                             elif p == 2:
                                 delete_check = ['roomduty', 'staffmanagement', 'room']
                                 combo = [ ["roomduty", 'staffmanagement', "staffid"], ["roomduty", "room", "roomid"]]
                                 dsub.generic_delete_value(dsub.select_ports['admin:staffduty'], dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], delete_check, combo, "date", "date" ) 
                            
                             else:
                                break
                            
                    elif p == 4:
                       while(True):
                            p = db.choice_make("Medicines", "Medical Equipments", "Diagnostic Tests", "Back" )
                            if p == 1:
                                table = 'medicine'
                                dsub.generic_delete_singletable(dsub.select_ports['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'], table )
                                     
                            elif p == 2:
                                table = 'medequipment'
                                dsub.generic_delete_singletable(dsub.select_ports['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'], table )
                             
                            else:
                                break
                           

                    
                    else:
                        break                
            
            else: 
                break
    elif login == 2:
        while(True):
            print("\n**** LOGGED IN AS PATIENT ****\n")
            x = db.choice_make("View Information", "Update Information", "Cancel")
            
           
                    
            if x == 1:
                while(True):
                    print("\n**** View Infromation ****\n")
                    p = db.choice_make("Doctor Infromation", "Patient information", "Medical Supplies & Diagnostics", "Room", "Back")
                    if p == 1:
                        p = db.choice_make("Doctor Infromation", "Duty Schedule", "Back")
                        if p == 1:
                            p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                            if p == 1:
                                dsub.doctor_view_admin()
                            elif p == 2:
                                dsub.doctor_range_admin()
                            elif p == 3:
                                db.view_all(['doctorsmanagement'], dsub.view_ports['dview:doctorsmanagement'], dsub.table_fields['doctorsmanagement'])
                                
                        elif p == 2:
                            p = db.choice_make("Search with value", "Search with range", "View all", "Back")
                            delete_check = ['roomduty', 'doctorsmanagement', 'room']
                            combo = [ ["roomduty", 'doctorsmanagement', "docid"], ["roomduty", "room", "roomid"]]
                            if p == 1:
                                dsub.generic_view_value(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], delete_check, combo, "date", "date") 
                            elif p == 2:
                                table = 'roomduty'
                                dsub.generic_range_singletable(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], table)
                            elif p == 3:
                                db.view_all(delete_check, dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], combo)
                            
                    elif p == 2:
                        while(True):
                            p = db.choice_make("Patient Information", "Admission & Emergency Infromation", "Prescription", "Diagnostic Reports", "Back")
                            if p == 1:
                                p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                if p == 1:      
                                    dsub.patient_view_admin()
                                elif p == 2:
                                    dsub.patient_range_admin()
                                elif p == 3:
                                    db.view_all(['patientmanagement'], dsub.view_ports['admin:patientmanagement'], dsub.table_fields['patientmanagement'])
                        
                            
                            elif p == 2:
                                p = db.choice_make("Patient: Outdoor", "Patient: Emergency", "Patient : Admission", "Back")
                                if p == 1:
                                    p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                    delete_check = ['outdoor', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["outdoor", 'patientmanagement', "patientid"], ["outdoor", "doctorsmanagement", "docid"]]
                                    
                                    if p == 1:
                                        dsub.generic_view_value(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date", "date")
                                        
                                    elif p == 2:
                                        dsub.generic_view_range(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date", "date")
                                        
                                    elif p == 3:
                                        db.view_all(delete_check, dsub.view_ports['outdoor:admin'], dsub.table_fields['outdoor:admin'], combo)
                                
                                elif p == 2:
                                    p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                    delete_check = ['emergency', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["emergency", 'patientmanagement', "patientid"], ["emergency", "doctorsmanagement", "docid"]]
                                    
                                    if p == 1:
                                        dsub.generic_view_value(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date")
                                        
                                    elif p == 2:
                                        dsub.generic_view_range(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date")
                                    elif p == 3:
                                        db.view_all(delete_check, dsub.view_ports['emergency:admin'], dsub.table_fields['emergency:admin'], combo)
                                
                                elif p == 3:
                                    p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                    delete_check = ['admission', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["admission", 'patientmanagement', "patientid"], ["admission", "doctorsmanagement", "docid"], ["admission", "room", "roomid"]]
                                    if p == 1:
                                        
                                        dsub.generic_view_value(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate")
                                    elif p == 2:
                                        dsub.generic_view_range(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate")
                                    elif p == 3:
                                        db.view_all(delete_check, dsub.view_ports['admission:admin'], dsub.table_fields['admission:admin'], combo)
                                    
                            elif p == 3:
                                p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                delete_check = ['prescription', 'patientmanagement', 'doctorsmanagement']
                                combo = [ ["prescription", 'patientmanagement', "patientid"], ["prescription", "doctorsmanagement", "docid"], ["prescription", "medicine", "medid"], ["prescription", "diagnostictests", "testid"]]
                               
                                if p == 1:
                                    dsub.generic_view_value(dsub.select_ports['admin:prescription'], dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], delete_check, combo, "date", "date") 
                                
                                elif p == 2:
                                    dsub.generic_view_range(dsub.select_ports['admin:prescription'], dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], delete_check, combo, "date", "date")
                                elif p == 3:
                                    db.view_all(delete_check, dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], combo)
                            
                            elif p == 4:
                                p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                delete_check = ['prescription', 'patientmanagement', 'diagnosticreport']
                                combo =  [ ["prescription", "diagnosticreport", "presid"], ["prescription", 'patientmanagement', "patientid"],  ["prescription", "diagnostictests", "testid"], ["diagnosticreport", "doctorsmanagement", "docid"]]
                               
                                if p == 1:
                                    dsub.generic_view_value(dsub.select_ports['admin:report'], dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], delete_check, combo, "date", "date") 
                                
                                elif p == 2:
                                    dsub.generic_view_range(dsub.select_ports['admin:report'], dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], delete_check, combo, "date", "date")   
                                
                                elif p == 3:
                                    db.view_all(delete_check, dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], combo)

                            else:
                                break
                                                      
                    elif p == 3:
                       p = db.choice_make("Medicines", "Medical Equipments", "Diagnostic Tests", "Back")
                       if p == 1:
                           p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                           table = 'medicine'
                           if p == 1:  
                                dsub.generic_view_singletable(dsub.select_ports['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'], table)
                           elif p == 2:
                                dsub.generic_range_singletable(dsub.select_ports['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'], table)
                           elif p == 3:
                                db.view_all(['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'])
                                
                       elif p == 2:
                           p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                           table = 'medequipment'
                           if p == 1:  
                                dsub.generic_view_singletable(dsub.select_ports['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'], table)
                           elif p == 2:
                                dsub.generic_range_singletable(dsub.select_ports['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'], table)
                           elif p == 3:
                                db.view_all(['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'])
                        
                       elif p == 3:
                           p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                           table = 'diagnostictests'
                           if p == 1:  
                                dsub.generic_view_singletable(dsub.select_ports['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'], table)
                           elif p == 2:
                                dsub.generic_range_singletable(dsub.select_ports['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'], table)
                           elif p == 3:
                                db.view_all(['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'])
                                
                    elif p == 4:
                       p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                       table = 'room'
                       if p == 1:  
                            dsub.generic_view_singletable(dsub.select_ports['room'], dsub.view_ports['room'], dsub.table_fields['room'], table)
                       elif p == 2:
                            dsub.generic_range_singletable(dsub.select_ports['room'], dsub.view_ports['room'], dsub.table_fields['room'], table)
                       elif p == 3:
                            db.view_all(['room'], dsub.view_ports['room'], dsub.table_fields['room'])
                            
                    else:
                        break
                        
                                
                            
                    
            #UPDATE                
            elif x == 2:
                while(True):
                    print("\n**** Update Infromation ****\n")
                    p = db.choice_make("Patient information", "Back")
                   
                            
                    if p == 1:

                        table = 'patientmanagement'
                        dsub.generic_update_singletable(dsub.select_ports['admin:patientmanagement'], dsub.view_ports['admin:patientmanagement'], dsub.table_fields['patientmanagement'], table, update_ports = dsub.update_ports['patsel:patientmanagement'])
                                                       

                    else:
                        break
                            
                            
            else:
                break
                  
          
        
    elif login == 3:
        while(True):
            print("\n**** LOGGED IN AS STAFF ****\n")
            x = db.choice_make("Add New Information","View Information", "Update Information", "Delete Information", "Cancel")
            
            if x == 1:
                while(True):
                    print("\n**** Add New Information ****\n")
                    print("Which Database to do you want to add to: ")
                    p = db.choice_make("Doctor Information", "Patient Information", "Staff Information", "Back")
                    
                    if p == 1:
                        while(True):
                            p = db.choice_make("Doctor Duty Schedule", "Back")

                            if p == 1: 
                                dsub.roomduty_entry()
                                
                            else:
                                break
                    elif p == 2:
                        while(True):
                            p = db.choice_make("Patient Information", "Admission & Emergency Infromation", "Back")
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
                    
                    
                    else:
                        break
                            
                    
            elif x == 2:
                while(True):
                    print("\n**** View Infromation ****\n")
                    p = db.choice_make("Doctor Infromation", "Patient information", "Staff Infromation", "Medical Supplies & Diagnostics", "Room", "Back")
                    if p == 1:
                        p = db.choice_make("Doctor Infromation", "Duty Schedule", "Back")
                        if p == 1:
                            p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                            if p == 1:
                                dsub.doctor_view_admin()
                            elif p == 2:
                                dsub.doctor_range_admin()
                            elif p == 3:
                                db.view_all(['doctorsmanagement'], dsub.view_ports['dview:doctorsmanagement'], dsub.table_fields['doctorsmanagement'])
                                
                        elif p == 2:
                            p = db.choice_make("Search with value", "Search with range", "View all", "Back")
                            delete_check = ['roomduty', 'doctorsmanagement', 'room']
                            combo = [ ["roomduty", 'doctorsmanagement', "docid"], ["roomduty", "room", "roomid"]]
                            if p == 1:
                                dsub.generic_view_value(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], delete_check, combo, "date", "date") 
                            elif p == 2:
                                table = 'roomduty'
                                dsub.generic_range_singletable(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], table)
                            elif p == 3:
                                db.view_all(delete_check, dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], combo)
                            
                    elif p == 2:
                        while(True):
                            p = db.choice_make("Patient Information", "Admission & Emergency Infromation", "Prescription", "Diagnostic Reports", "Back")
                            if p == 1:
                                p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                if p == 1:      
                                    dsub.patient_view_admin()
                                elif p == 2:
                                    dsub.patient_range_admin()
                                elif p == 3:
                                    db.view_all(['patientmanagement'], dsub.view_ports['admin:patientmanagement'], dsub.table_fields['patientmanagement'])
                        
                            
                            elif p == 2:
                                p = db.choice_make("Patient: Outdoor", "Patient: Emergency", "Patient : Admission", "Back")
                                if p == 1:
                                    p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                    delete_check = ['outdoor', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["outdoor", 'patientmanagement', "patientid"], ["outdoor", "doctorsmanagement", "docid"]]
                                    
                                    if p == 1:
                                        dsub.generic_view_value(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date", "date")
                                        
                                    elif p == 2:
                                        dsub.generic_view_range(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date", "date")
                                        
                                    elif p == 3:
                                        db.view_all(delete_check, dsub.view_ports['outdoor:admin'], dsub.table_fields['outdoor:admin'], combo)
                                
                                elif p == 2:
                                    p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                    delete_check = ['emergency', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["emergency", 'patientmanagement', "patientid"], ["emergency", "doctorsmanagement", "docid"]]
                                    
                                    if p == 1:
                                        dsub.generic_view_value(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date")
                                        
                                    elif p == 2:
                                        dsub.generic_view_range(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date")
                                    elif p == 3:
                                        db.view_all(delete_check, dsub.view_ports['emergency:admin'], dsub.table_fields['emergency:admin'], combo)
                                
                                elif p == 3:
                                    p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                    delete_check = ['admission', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["admission", 'patientmanagement', "patientid"], ["admission", "doctorsmanagement", "docid"], ["admission", "room", "roomid"]]
                                    if p == 1:
                                        
                                        dsub.generic_view_value(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate")
                                    elif p == 2:
                                        dsub.generic_view_range(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate")
                                    elif p == 3:
                                        db.view_all(delete_check, dsub.view_ports['admission:admin'], dsub.table_fields['admission:admin'], combo)
                                    
                            elif p == 3:
                                p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                delete_check = ['prescription', 'patientmanagement', 'doctorsmanagement']
                                combo = [ ["prescription", 'patientmanagement', "patientid"], ["prescription", "doctorsmanagement", "docid"], ["prescription", "medicine", "medid"], ["prescription", "diagnostictests", "testid"]]
                               
                                if p == 1:
                                    dsub.generic_view_value(dsub.select_ports['admin:prescription'], dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], delete_check, combo, "date", "date") 
                                
                                elif p == 2:
                                    dsub.generic_view_range(dsub.select_ports['admin:prescription'], dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], delete_check, combo, "date", "date")
                                elif p == 3:
                                    db.view_all(delete_check, dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], combo)
                            
                            elif p == 4:
                                p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                delete_check = ['prescription', 'patientmanagement', 'diagnosticreport']
                                combo =  [ ["prescription", "diagnosticreport", "presid"], ["prescription", 'patientmanagement', "patientid"],  ["prescription", "diagnostictests", "testid"], ["diagnosticreport", "doctorsmanagement", "docid"]]
                               
                                if p == 1:
                                    dsub.generic_view_value(dsub.select_ports['admin:report'], dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], delete_check, combo, "date", "date") 
                                
                                elif p == 2:
                                    dsub.generic_view_range(dsub.select_ports['admin:report'], dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], delete_check, combo, "date", "date")   
                                
                                elif p == 3:
                                    db.view_all(delete_check, dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], combo)

                            else:
                                break
                            
                    elif p == 3:
                        while(True):
                             p = db.choice_make("Staff Information", "Duty Schedule", "Back")
                             if p == 1:
                                 p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                 if p == 1:
                                     table = 'staffmanagement'
                                     dsub.generic_view_singletable(dsub.select_ports['admin:staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'], table)
                                 elif p == 2:
                                     table = 'staffmanagement'
                                     dsub.generic_range_singletable(dsub.select_ports['admin:staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'], table)
                                 elif p == 3:
                                     db.view_all(['staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'])
                                     
                                     
                             elif p == 2:
                                 p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                 delete_check = ['roomduty', 'staffmanagement', 'room']
                                 combo = [ ["roomduty", 'staffmanagement', "staffid"], ["roomduty", "room", "roomid"]]
                                 if p == 1:
                                     dsub.generic_view_value(dsub.select_ports['admin:staffduty'], dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], delete_check, combo, "date", "date") 
                                 elif p == 2:
                                     dsub.generic_view_range(dsub.select_ports['admin:staffduty'], dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], delete_check, combo, "date", "date") 
                                 elif p == 3:
                                     db.view_all(delete_check, dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], combo)
                            
                             else:
                                break
                             
                    elif p == 4:
                       p = db.choice_make("Medicines", "Medical Equipments", "Diagnostic Tests", "Back")
                       if p == 1:
                           p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                           table = 'medicine'
                           if p == 1:  
                                dsub.generic_view_singletable(dsub.select_ports['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'], table)
                           elif p == 2:
                                dsub.generic_range_singletable(dsub.select_ports['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'], table)
                           elif p == 3:
                                db.view_all(['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'])
                                
                       elif p == 2:
                           p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                           table = 'medequipment'
                           if p == 1:  
                                dsub.generic_view_singletable(dsub.select_ports['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'], table)
                           elif p == 2:
                                dsub.generic_range_singletable(dsub.select_ports['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'], table)
                           elif p == 3:
                                db.view_all(['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'])
                        
                       elif p == 3:
                           p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                           table = 'diagnostictests'
                           if p == 1:  
                                dsub.generic_view_singletable(dsub.select_ports['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'], table)
                           elif p == 2:
                                dsub.generic_range_singletable(dsub.select_ports['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'], table)
                           elif p == 3:
                                db.view_all(['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'])
                                
                    elif p == 5:
                       p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                       table = 'room'
                       if p == 1:  
                            dsub.generic_view_singletable(dsub.select_ports['room'], dsub.view_ports['room'], dsub.table_fields['room'], table)
                       elif p == 2:
                            dsub.generic_range_singletable(dsub.select_ports['room'], dsub.view_ports['room'], dsub.table_fields['room'], table)
                       elif p == 3:
                            db.view_all(['room'], dsub.view_ports['room'], dsub.table_fields['room'])
                            
                    else:
                        break
                        
                                
                            
                    
            #UPDATE                
            elif x == 3:
                while(True):
                    print("\n**** Update Infromation ****\n")
                    p = db.choice_make("Doctor Infromation", "Patient information", "Staff Infromation", "Medical Supplies", "Back")
                    if p == 1:
                        p = db.choice_make("Doctor Infromation", "Duty Schedule", "Back")
                        if p == 1:
                            table = 'doctorsmanagement'
                            dsub.generic_update_singletable(dsub.select_ports['dview:doctorsmanagement'], dsub.view_ports['dview:doctorsmanagement'], dsub.table_fields['doctorsmanagement'], table, update_ports = dsub.update_ports['staffsel:doctorsmanagement'])
                                
                        elif p == 2:
                            delete_check = ['roomduty', 'doctorsmanagement', 'room']
                            combo = [ ["roomduty", 'doctorsmanagement', "docid"], ["roomduty", "room", "roomid"]]
                            dsub.generic_update_value(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], delete_check, combo, "date", "date") 

                            
                    elif p == 2:
                        while(True):
                            p = db.choice_make("Patient Information", "Admission & Emergency Infromation", "Back")
                            if p == 1:
                                table = 'patientmanagement'
                                dsub.generic_update_singletable(dsub.select_ports['admin:patientmanagement'], dsub.view_ports['admin:patientmanagement'], dsub.table_fields['patientmanagement'], table)
                                                       
                            elif p == 2:
                                p = db.choice_make("Patient: Outdoor", "Patient: Emergency", "Patient : Admission", "Back")
                                if p == 1:
                                    delete_check = ['outdoor', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["outdoor", 'patientmanagement', "patientid"], ["outdoor", "doctorsmanagement", "docid"]]
                                    
                                    dsub.generic_update_value(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date", "date")
                                        
                                elif p == 2:
                                    delete_check = ['emergency', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["emergency", 'patientmanagement', "patientid"], ["emergency", "doctorsmanagement", "docid"]]
                                   
                                    dsub.generic_update_value(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date")
                                        
                                elif p == 3:
                                    delete_check = ['admission', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["admission", 'patientmanagement', "patientid"], ["admission", "doctorsmanagement", "docid"], ["admission", "room", "roomid"]]
                                    
                                    dsub.generic_update_value(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate")
                                    
                                

                            else:
                                break
                            
                    elif p == 3:
                        while(True):
                             p = db.choice_make("Staff Information", "Duty Schedule", "Back")
                             if p == 1:
                                 table = 'staffmanagement'
                                 dsub.generic_update_singletable(dsub.select_ports['admin:staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'], table)
                                     
                             elif p == 2:
                                 delete_check = ['roomduty', 'staffmanagement', 'room']
                                 combo = [ ["roomduty", 'staffmanagement', "staffid"], ["roomduty", "room", "roomid"]]
                                 dsub.generic_update_value(dsub.select_ports['admin:staffduty'], dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], delete_check, combo, "date", "date") 
                            
                             else:
                                break
                            
                    elif p == 4:
                       while(True):
                            p = db.choice_make("Medicines", "Medical Equipments", "Back")
                            if p == 1:
                                table = 'medicine'
                                dsub.generic_update_singletable(dsub.select_ports['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'], table, update_ports = dsub.update_ports['staffsel:medicine']  )
                                     
                            elif p == 2:
                                table = 'medequipment'
                                dsub.generic_update_singletable(dsub.select_ports['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'], table, update_ports = dsub.update_ports['staffsel:medequipment'])               

                            else:
                                break
                           

                    
                    else:
                        break
            # DELETE
            elif x == 4:
                while(True):
                    print("\n**** Delete Infromation ****\n")
                    p = db.choice_make("Doctor Infromation", "Patient information", "Staff Infromation",  "Back")
                    if p == 1:
                        p = db.choice_make("Doctor Duty Schedule", "Back")
                                
                        if p == 1:
                            delete_check = ['roomduty', 'doctorsmanagement', 'room']
                            combo = [ ["roomduty", 'doctorsmanagement', "docid"], ["roomduty", "room", "roomid"]]
                            dsub.generic_delete_value(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], delete_check, combo, "date", "date") 

                            
                    elif p == 2:
                        while(True):
                            p = db.choice_make("Patient Information", "Admission & Emergency Infromation", "Back")
                            if p == 1:
                                table = 'patientmanagement'
                                dsub.generic_delete_singletable(dsub.select_ports['admin:patientmanagement'], dsub.view_ports['admin:patientmanagement'], dsub.table_fields['patientmanagement'], table)
                                                       
                            elif p == 2:
                                p = db.choice_make("Patient: Outdoor", "Patient: Emergency", "Patient : Admission", "Back")
                                if p == 1:
                                    delete_check = ['outdoor', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["outdoor", 'patientmanagement', "patientid"], ["outdoor", "doctorsmanagement", "docid"]]
                                    
                                    dsub.generic_delete_value(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date")
                                        
                                elif p == 2:
                                    delete_check = ['emergency', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["emergency", 'patientmanagement', "patientid"], ["emergency", "doctorsmanagement", "docid"]]
                                   
                                    dsub.generic_delete_value(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date")
                                        
                                elif p == 3:
                                    delete_check = ['admission', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["admission", 'patientmanagement', "patientid"], ["admission", "doctorsmanagement", "docid"], ["admission", "room", "roomid"]]
                                    
                                    dsub.generic_delete_value(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate")


                            else:
                                break
                            
                    elif p == 3:
                        while(True):
                             p = db.choice_make("Staff Information", "Duty Schedule", "Back")
                             if p == 1:
                                 table = 'staffmanagement'
                                 dsub.generic_delete_singletable(dsub.select_ports['admin:staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'], table)
                                     
                             elif p == 2:
                                 delete_check = ['roomduty', 'staffmanagement', 'room']
                                 combo = [ ["roomduty", 'staffmanagement', "staffid"], ["roomduty", "room", "roomid"]]
                                 dsub.generic_delete_value(dsub.select_ports['admin:staffduty'], dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], delete_check, combo, "date") 
                            
                             else:
                                break
                            
    
                    else:
                        break                
            
            else: 
                break
    # ADMIN    
    elif login == 4:     
        while(True):
            print("\n**** LOGGED IN AS CENTRAL ADMIN ****\n")
            x = db.choice_make("CREATE entry","RETRIEVE entry", "UPDATE entry", "DELETE entry", "Cancel")
            
            if x == 1:
                while(True):
                    print("\n**** CREATE ENTRY ****\n")
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
                while(True):
                    print("\n**** VIEW ENTRIES ****\n")
                    p = db.choice_make("Doctor Infromation", "Patient information", "Staff Infromation", "Medical Supplies & Diagnostics", "Room", "Back")
                    if p == 1:
                        p = db.choice_make("Doctor Infromation", "Duty Schedule", "Back")
                        if p == 1:
                            p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                            if p == 1:
                                dsub.doctor_view_admin()
                            elif p == 2:
                                dsub.doctor_range_admin()
                            elif p == 3:
                                db.view_all(['doctorsmanagement'], dsub.view_ports['dview:doctorsmanagement'], dsub.table_fields['doctorsmanagement'])
                                
                        elif p == 2:
                            p = db.choice_make("Search with value", "Search with range", "View all", "Back")
                            delete_check = ['roomduty', 'doctorsmanagement', 'room']
                            combo = [ ["roomduty", 'doctorsmanagement', "docid"], ["roomduty", "room", "roomid"]]
                            if p == 1:
                                dsub.generic_view_value(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], delete_check, combo, "date", "date") 
                            elif p == 2:
                                table = 'roomduty'
                                dsub.generic_range_singletable(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], table)
                            elif p == 3:
                                db.view_all(delete_check, dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], combo)
                            
                    elif p == 2:
                        while(True):
                            p = db.choice_make("Patient Information", "Admission & Emergency Infromation", "Prescription", "Diagnostic Reports", "Back")
                            if p == 1:
                                p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                if p == 1:      
                                    dsub.patient_view_admin()
                                elif p == 2:
                                    dsub.patient_range_admin()
                                elif p == 3:
                                    db.view_all(['patientmanagement'], dsub.view_ports['admin:patientmanagement'], dsub.table_fields['patientmanagement'])
                        
                            
                            elif p == 2:
                                p = db.choice_make("Patient: Outdoor", "Patient: Emergency", "Patient : Admission", "Back")
                                if p == 1:
                                    p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                    delete_check = ['outdoor', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["outdoor", 'patientmanagement', "patientid"], ["outdoor", "doctorsmanagement", "docid"]]
                                    
                                    if p == 1:
                                        dsub.generic_view_value(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date", "date")
                                        
                                    elif p == 2:
                                        dsub.generic_view_range(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date", "date")
                                        
                                    elif p == 3:
                                        db.view_all(delete_check, dsub.view_ports['outdoor:admin'], dsub.table_fields['outdoor:admin'], combo)
                                
                                elif p == 2:
                                    p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                    delete_check = ['emergency', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["emergency", 'patientmanagement', "patientid"], ["emergency", "doctorsmanagement", "docid"]]
                                    
                                    if p == 1:
                                        dsub.generic_view_value(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date")
                                        
                                    elif p == 2:
                                        dsub.generic_view_range(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date")
                                    elif p == 3:
                                        db.view_all(delete_check, dsub.view_ports['emergency:admin'], dsub.table_fields['emergency:admin'], combo)
                                
                                elif p == 3:
                                    p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                    delete_check = ['admission', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["admission", 'patientmanagement', "patientid"], ["admission", "doctorsmanagement", "docid"], ["admission", "room", "roomid"]]
                                    if p == 1:
                                        
                                        dsub.generic_view_value(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate")
                                    elif p == 2:
                                        dsub.generic_view_range(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate")
                                    elif p == 3:
                                        db.view_all(delete_check, dsub.view_ports['admission:admin'], dsub.table_fields['admission:admin'], combo)
                                    
                            elif p == 3:
                                p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                delete_check = ['prescription', 'patientmanagement', 'doctorsmanagement']
                                combo = [ ["prescription", 'patientmanagement', "patientid"], ["prescription", "doctorsmanagement", "docid"], ["prescription", "medicine", "medid"], ["prescription", "diagnostictests", "testid"]]
                               
                                if p == 1:
                                    dsub.generic_view_value(dsub.select_ports['admin:prescription'], dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], delete_check, combo, "date", "date") 
                                
                                elif p == 2:
                                    dsub.generic_view_range(dsub.select_ports['admin:prescription'], dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], delete_check, combo, "date", "date")
                                elif p == 3:
                                    db.view_all(delete_check, dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], combo)
                            
                            elif p == 4:
                                p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                delete_check = ['prescription', 'patientmanagement', 'diagnosticreport']
                                combo =  [ ["prescription", "diagnosticreport", "presid"], ["prescription", 'patientmanagement', "patientid"],  ["prescription", "diagnostictests", "testid"], ["diagnosticreport", "doctorsmanagement", "docid"]]
                               
                                if p == 1:
                                    dsub.generic_view_value(dsub.select_ports['admin:report'], dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], delete_check, combo, "date", "date") 
                                
                                elif p == 2:
                                    dsub.generic_view_range(dsub.select_ports['admin:report'], dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], delete_check, combo, "date", "date")   
                                
                                elif p == 3:
                                    db.view_all(delete_check, dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], combo)

                            else:
                                break
                            
                    elif p == 3:
                        while(True):
                             p = db.choice_make("Staff Information", "Duty Schedule", "Back")
                             if p == 1:
                                 p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                 if p == 1:
                                     table = 'staffmanagement'
                                     dsub.generic_view_singletable(dsub.select_ports['admin:staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'], table)
                                 elif p == 2:
                                     table = 'staffmanagement'
                                     dsub.generic_range_singletable(dsub.select_ports['admin:staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'], table)
                                 elif p == 3:
                                     db.view_all(['staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'])
                                     
                                     
                             elif p == 2:
                                 p = db.choice_make("Search with value", "Search with range", "View All", "Back")
                                 delete_check = ['roomduty', 'staffmanagement', 'room']
                                 combo = [ ["roomduty", 'staffmanagement', "staffid"], ["roomduty", "room", "roomid"]]
                                 if p == 1:
                                     dsub.generic_view_value(dsub.select_ports['admin:staffduty'], dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], delete_check, combo, "date", "date") 
                                 elif p == 2:
                                     dsub.generic_view_range(dsub.select_ports['admin:staffduty'], dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], delete_check, combo, "date", "date") 
                                 elif p == 3:
                                     db.view_all(delete_check, dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], combo)
                            
                             else:
                                break
                             
                    elif p == 4:
                       p = db.choice_make("Medicines", "Medical Equipments", "Diagnostic Tests", "Back")
                       if p == 1:
                           p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                           table = 'medicine'
                           if p == 1:  
                                dsub.generic_view_singletable(dsub.select_ports['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'], table)
                           elif p == 2:
                                dsub.generic_range_singletable(dsub.select_ports['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'], table)
                           elif p == 3:
                                db.view_all(['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'])
                                
                       elif p == 2:
                           p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                           table = 'medequipment'
                           if p == 1:  
                                dsub.generic_view_singletable(dsub.select_ports['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'], table)
                           elif p == 2:
                                dsub.generic_range_singletable(dsub.select_ports['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'], table)
                           elif p == 3:
                                db.view_all(['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'])
                        
                       elif p == 3:
                           p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                           table = 'diagnostictests'
                           if p == 1:  
                                dsub.generic_view_singletable(dsub.select_ports['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'], table)
                           elif p == 2:
                                dsub.generic_range_singletable(dsub.select_ports['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'], table)
                           elif p == 3:
                                db.view_all(['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'])
                                
                    elif p == 5:
                       p = db.choice_make("Search with value", "Search with range", "View All", "Back")  
                       table = 'room'
                       if p == 1:  
                            dsub.generic_view_singletable(dsub.select_ports['room'], dsub.view_ports['room'], dsub.table_fields['room'], table)
                       elif p == 2:
                            dsub.generic_range_singletable(dsub.select_ports['room'], dsub.view_ports['room'], dsub.table_fields['room'], table)
                       elif p == 3:
                            db.view_all(['room'], dsub.view_ports['room'], dsub.table_fields['room'])
                            
                    else:
                        break
                        
                                
                            
                    
            #UPDATE                
            elif x == 3:
                while(True):
                    print("\n**** UPDATE ENTRY ****\n")
                    p = db.choice_make("Doctor Infromation", "Patient information", "Staff Infromation", "Medical Supplies & Diagnostics", "Room", "Back")
                    if p == 1:
                        p = db.choice_make("Doctor Infromation", "Duty Schedule", "Back")
                        if p == 1:
                            table = 'doctorsmanagement'
                            dsub.generic_update_singletable(dsub.select_ports['dview:doctorsmanagement'], dsub.view_ports['dview:doctorsmanagement'], dsub.table_fields['doctorsmanagement'], table)
                                
                        elif p == 2:
                            delete_check = ['roomduty', 'doctorsmanagement', 'room']
                            combo = [ ["roomduty", 'doctorsmanagement', "docid"], ["roomduty", "room", "roomid"]]
                            dsub.generic_update_value(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], delete_check, combo, "date", "date") 

                            
                    elif p == 2:
                        while(True):
                            p = db.choice_make("Patient Information", "Admission & Emergency Infromation", "Prescription", "Diagnostic Reports", "Back")
                            if p == 1:
                                table = 'patientmanagement'
                                dsub.generic_update_singletable(dsub.select_ports['admin:patientmanagement'], dsub.view_ports['admin:patientmanagement'], dsub.table_fields['patientmanagement'], table)
                                                       
                            elif p == 2:
                                p = db.choice_make("Patient: Outdoor", "Patient: Emergency", "Patient : Admission", "Back")
                                if p == 1:
                                    delete_check = ['outdoor', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["outdoor", 'patientmanagement', "patientid"], ["outdoor", "doctorsmanagement", "docid"]]
                                    
                                    dsub.generic_update_value(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date", "date")
                                        
                                elif p == 2:
                                    delete_check = ['emergency', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["emergency", 'patientmanagement', "patientid"], ["emergency", "doctorsmanagement", "docid"]]
                                   
                                    dsub.generic_update_value(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date")
                                        
                                elif p == 3:
                                    delete_check = ['admission', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["admission", 'patientmanagement', "patientid"], ["admission", "doctorsmanagement", "docid"], ["admission", "room", "roomid"]]
                                    
                                    dsub.generic_update_value(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate")
                                    
                            elif p == 3:
                                delete_check = ['prescription', 'patientmanagement', 'doctorsmanagement']
                                combo = [ ["prescription", 'patientmanagement', "patientid"], ["prescription", "doctorsmanagement", "docid"], ["prescription", "medicine", "medid"], ["prescription", "diagnostictests", "testid"]]
                               
                                dsub.generic_update_value(dsub.select_ports['admin:prescription'], dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], delete_check, combo, "date", "date") 
                                
                            elif p == 4:
                                delete_check = ['diagnosticreport', 'patientmanagement', 'prescription']
                                combo =  [ ["prescription", "diagnosticreport", "presid"], ["prescription", 'patientmanagement', "patientid"],  ["prescription", "diagnostictests", "testid"], ["diagnosticreport", "doctorsmanagement", "docid"]]
                               
                                dsub.generic_update_value(dsub.select_ports['admin:report'], dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], delete_check, combo, "date", "date") 

                            else:
                                break
                            
                    elif p == 3:
                        while(True):
                             p = db.choice_make("Staff Information", "Duty Schedule", "Back")
                             if p == 1:
                                 table = 'staffmanagement'
                                 dsub.generic_update_singletable(dsub.select_ports['admin:staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'], table)
                                     
                             elif p == 2:
                                 delete_check = ['roomduty', 'staffmanagement', 'room']
                                 combo = [ ["roomduty", 'staffmanagement', "staffid"], ["roomduty", "room", "roomid"]]
                                 dsub.generic_update_value(dsub.select_ports['admin:staffduty'], dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], delete_check, combo, "date", "date") 
                            
                             else:
                                break
                            
                    elif p == 4:
                       while(True):
                            p = db.choice_make("Medicines", "Medical Equipments", "Diagnostic Tests", "Back")
                            if p == 1:
                                table = 'medicine'
                                dsub.generic_update_singletable(dsub.select_ports['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'], table)
                                     
                            elif p == 2:
                                table = 'medequipment'
                                dsub.generic_update_singletable(dsub.select_ports['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'], table)
                             
                            elif p == 3:
                                table = 'diagnostictests'
                                dsub.generic_update_singletable(dsub.select_ports['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'], table)
                            else:
                                break
                           
                    elif p == 5:
                       table = 'room'
                       dsub.generic_update_singletable(dsub.select_ports['room'], dsub.view_ports['room'], dsub.table_fields['room'], table)
                    
                    else:
                        break
            # DELETE
            elif x == 4:
                while(True):
                    print("\n**** DELETE ENTRY ****\n")
                    p = db.choice_make("Doctor Infromation", "Patient information", "Staff Infromation", "Medical Supplies & Diagnostics", "Room", "Back")
                    if p == 1:
                        p = db.choice_make("Doctor Infromation", "Duty Schedule", "Back")
                        if p == 1:
                            table = 'doctorsmanagement'
                            dsub.generic_delete_singletable(dsub.select_ports['dview:doctorsmanagement'], dsub.view_ports['dview:doctorsmanagement'], dsub.table_fields['doctorsmanagement'], table, deletetype = "admin")
                                
                        elif p == 2:
                            delete_check = ['roomduty', 'doctorsmanagement', 'room']
                            combo = [ ["roomduty", 'doctorsmanagement', "docid"], ["roomduty", "room", "roomid"]]
                            dsub.generic_delete_value(dsub.select_ports['admin:docduty'], dsub.view_ports['admin:docduty'], dsub.table_fields['admin:docduty'], delete_check, combo, "date", "date", deletetype = "admin") 

                            
                    elif p == 2:
                        while(True):
                            p = db.choice_make("Patient Information", "Admission & Emergency Infromation", "Prescription", "Diagnostic Reports", "Back")
                            if p == 1:
                                table = 'patientmanagement'
                                dsub.generic_delete_singletable(dsub.select_ports['admin:patientmanagement'], dsub.view_ports['admin:patientmanagement'], dsub.table_fields['patientmanagement'], table, deletetype = "admin")
                                                       
                            elif p == 2:
                                p = db.choice_make("Patient: Outdoor", "Patient: Emergency", "Patient : Admission", "Back")
                                if p == 1:
                                    delete_check = ['outdoor', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["outdoor", 'patientmanagement', "patientid"], ["outdoor", "doctorsmanagement", "docid"]]
                                    
                                    dsub.generic_delete_value(dsub.select_ports['outdoor:admin'], dsub.view_ports['admin:outdoor'], dsub.table_fields['admin:outdoor'], delete_check, combo, "date", "date", deletetype = "admin")
                                        
                                elif p == 2:
                                    delete_check = ['emergency', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["emergency", 'patientmanagement', "patientid"], ["emergency", "doctorsmanagement", "docid"]]
                                   
                                    dsub.generic_delete_value(dsub.select_ports['emergency:admin'], dsub.view_ports['admin:emergency'], dsub.table_fields['admin:emergency'], delete_check, combo, "date", "date", deletetype = "admin")
                                        
                                elif p == 3:
                                    delete_check = ['admission', 'patientmanagement', 'doctorsmanagement']
                                    combo = [ ["admission", 'patientmanagement', "patientid"], ["admission", "doctorsmanagement", "docid"], ["admission", "room", "roomid"]]
                                    
                                    dsub.generic_delete_value(dsub.select_ports['admission:admin'], dsub.view_ports['admin:admission'], dsub.table_fields['admin:admission'], delete_check, combo, "admissiondate", "releasedate", deletetype = "admin")
                                    
                            elif p == 3:
                                delete_check = ['prescription', 'patientmanagement', 'doctorsmanagement']
                                combo = [ ["prescription", 'patientmanagement', "patientid"], ["prescription", "doctorsmanagement", "docid"], ["prescription", "medicine", "medid"], ["prescription", "diagnostictests", "testid"]]
                               
                                dsub.generic_delete_value(dsub.select_ports['admin:prescription'], dsub.view_ports['admin:prescription'], dsub.table_fields['admin:prescription'], delete_check, combo, "date", "date", deletetype = "admin") 
                                
                            elif p == 4:
                                delete_check = ['diagnosticreport', 'patientmanagement', 'prescription']
                                combo =  [ ["prescription", "diagnosticreport", "presid"], ["prescription", 'patientmanagement', "patientid"],  ["prescription", "diagnostictests", "testid"], ["diagnosticreport", "doctorsmanagement", "docid"]]
                               
                                dsub.generic_delete_value(dsub.select_ports['admin:report'], dsub.view_ports['admin:report'], dsub.table_fields['admin:report'], delete_check, combo, "date", "date", deletetype = "admin") 

                            else:
                                break
                            
                    elif p == 3:
                        while(True):
                             p = db.choice_make("Staff Information", "Duty Schedule", "Back")
                             if p == 1:
                                 table = 'staffmanagement'
                                 dsub.generic_delete_singletable(dsub.select_ports['admin:staffmanagement'], dsub.view_ports['admin:staffmanagement'], dsub.table_fields['admin:staffmanagement'], table, deletetype = "admin")
                                     
                             elif p == 2:
                                 delete_check = ['roomduty', 'staffmanagement', 'room']
                                 combo = [ ["roomduty", 'staffmanagement', "staffid"], ["roomduty", "room", "roomid"]]
                                 dsub.generic_delete_value(dsub.select_ports['admin:staffduty'], dsub.view_ports['admin:staffduty'], dsub.table_fields['admin:staffduty'], delete_check, combo, "date", "date", deletetype = "admin") 
                            
                             else:
                                break
                            
                    elif p == 4:
                       while(True):
                            p = db.choice_make("Medicines", "Medical Equipments", "Diagnostic Tests", "Back", deletetype = "admin")
                            if p == 1:
                                table = 'medicine'
                                dsub.generic_delete_singletable(dsub.select_ports['medicine'], dsub.view_ports['medicine'], dsub.table_fields['medicine'], table, deletetype = "admin")
                                     
                            elif p == 2:
                                table = 'medequipment'
                                dsub.generic_delete_singletable(dsub.select_ports['medequipment'], dsub.view_ports['medequipment'], dsub.table_fields['medequipment'], table, deletetype = "admin")
                             
                            elif p == 3:
                                table = 'diagnostictests'
                                dsub.generic_delete_singletable(dsub.select_ports['diagnostictests'], dsub.view_ports['diagnostictests'], dsub.table_fields['diagnostictests'], table, deletetype = "admin")
                            else:
                                break
                           
                    elif p == 5:
                       table = 'room'
                       dsub.generic_delete_singletable(dsub.select_ports['room'], dsub.view_ports['room'], dsub.table_fields['room'], table, deletetype = "admin")
                    
                    else:
                        break                
            
            else: 
                break
        
    else:
        break
    




#insert_data('doctorsmanagement', name, expertise, degree, position, chamber, time, fee, contactno, ids)





    

    

