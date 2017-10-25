#########################################################################################################
#   Program Name : NSWBirthRateDatabasePrep.py                                                          #
#   Program Description:                                                                                #
#   This program prepares a SQLite table concerning birth rates in NSW.                                 #
#                                                                                                       #
#   Comment                                         Date                  Author                        #
#   ================================                ==========            ================              #
#   Initial Version                                 25/10/2017            Engramar Bollas               #
#########################################################################################################
import sqlite3
import sys

#######################################################################
### nswbabies table                                                 ### 
#######################################################################
conn = sqlite3.connect('NSW_BIRTH_RATE.sqlite')
cur = conn.cursor()

cur.executescript('''	
DROP TABLE IF EXISTS NSW_BIRTH_RATE;

CREATE TABLE NSW_BIRTH_RATE (
	YEAR              number(4),            
	LOCALITY          varchar(100),
	SUBURB            varchar(100),  
	STATE             char(3), 
	POSTCODE          number(4),
	COUNT             number(8)
);

''')

fname1 = 'NSWBirthRate.txt'
fhand1 = open(fname1)

#######################################################################
### Populate Old Table                                              ### 
#######################################################################
for line in fhand1:	
	fields = line.split('|')

	YEAR      = fields[0].strip() 
	LOCALITY  = fields[1].strip()  
	SUBURB    = fields[2].strip() 
	STATE     = fields[3].strip() 
	POSTCODE  = fields[4].strip() 
	COUNT     = fields[5].strip() 
	
	if YEAR == "Year" : continue

	cur.execute('''INSERT INTO NSW_BIRTH_RATE
        (
		YEAR,
		LOCALITY,
		SUBURB,
		STATE,
		POSTCODE,
		COUNT
        )  
        VALUES ( ?, ?, ?, ?, ?, ?)''',   
		(
		YEAR,
		LOCALITY,
		SUBURB,
		STATE,
		POSTCODE,
		COUNT
		))
				
conn.commit()

print ('Done')