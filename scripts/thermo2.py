#!/usr/bin/python
import MySQLdb

def insertRow(values):
	#print 'Setting up Database connection'
    	conn = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="root", # your password
                      db="tbl_thermostat") # name of the data base
	# you must create a Cursor object. It will let
	#  you execute all the query you need
	cur = conn.cursor()

    	#insert into DB
    	try:
		 #sql = "INSERT INTO tbl_room_info (device_id, temperature,humidity,light,occupancy)values (?,?,?,?,?);"
            	#cur.execute(sql,(5,90.0,10.0,2,1))
            	cur.execute("INSERT INTO tbl_room_info (device_id, temperature, humidity, light, occupancy) values ( %s, %s, %s, %s, %s)", 
            	(values[0], values[1], values[2], values[3], values[4]))
            	conn.commit()
            	#print 'successfully added to Database'
    	except MySQLdb.Error, e:
            	conn.rollback()
            	#print 'failed: %s' %e
    
    	conn.close()
    	return

def getWebFlag():
	conn = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="root", # your password
                      db="tbl_thermostat") # name of the data base
        # you must create a Cursor object. It will let
        #  you execute all the query you need
        cur = conn.cursor()
	cur.execute("SELECT heating FROM tbl_heating ORDER BY unique_id DESC LIMIT 1")
	for row in cur.fetchall():
		if(row[0]==0):
			return False
		elif(row[0]==1):
			return True
		else:
			raise Exception("Error with WebFlag result:Flag is neither 0 or 1")

def setWebFlag(heating, agent):
	#print 'Setting up Database connection'
        conn = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="root", # your password
                      db="tbl_thermostat") # name of the data base
        # you must create a Cursor object. It will let
        #  you execute all the query you need
        cur = conn.cursor()

        #insert into DB
        try:
                 #sql = "INSERT INTO tbl_room_info (device_id, temperature,humidity,light,occupancy)values (?,?,?,?,?);"
                #cur.execute(sql,(5,90.0,10.0,2,1))
                cur.execute("INSERT INTO tbl_heating (heating, agent) values ( %s, %s)", (heating, agent))
                conn.commit()
                #print 'successfully added to Database'
        except MySQLdb.Error, e:
                conn.rollback()
                #print 'failed: %s' %e

        conn.close()
        return

