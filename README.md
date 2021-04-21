Hospital Database System with Python and MySQL

mysqlclient library was used for this project

The project contains 4 files:
1. dbfunctions.py : Contains the necessary basic functions
2. dbsubprograms.py : Contains subprograms for the interface
3. dbconnect.py : Contains and runs the management system interface
4. hospitaldatabase.sql : Contains the database

About:
------
In the database system mainly Create, Retrieve, Update and Delete operations are implemented. A prototype login system where one can log in as either doctor, nurse,
patient and central admin has been implemented. The Central Admin has full control of the database and can perform hard delete. The other logins are restricted to 
parts of the database that concerns their job only. For example: A patient cannot add an entry, can only update his contact infromations and can view necessary doctor
and hospital information. 

As this is a prototype, authentication of accounts were not implemented.


Navigation:
-----------

Users can navigate through the interace by entering the index number of the menu options.
For example:

**** Add new information ****

1. Doctor infromation
2. Patient infromation
3. Medicine and Supplies
4. Back

In order to access "Doctor Infromation", the user has to enter 1 and press return.

Operations:
-----------

CREATE:
User can entry the fields he has access to and can keep a field blank by just pressing the return key. 

RETRIEVE:
Users can view entries they have access to. They can either view all entries in a table or search for entries with a values or ranges for different fields.
Multiple fields can be selected. In case of the range selection one of the fields can be left empty. Some of the options will use table JOIN operation to show
fields from multiple realted entries. For example: Prescription view joins Doctormanagement, Patientmanagement, Prescription, Diagnostictests and Medicine tables and
displays the relevant fields.

UPDATE:
Users will first have to search for entries they want to update, then pick the entry from the search result if there are multiple results. Then they can
update multiple fields of that entry

DELETE:
Users will first search and select the entry they want to delete and then confirm that they want to delete that entry. Only the Central Admin can hard delete an entry.
In case of delete, the operation cascades to all related entries in other tables.





