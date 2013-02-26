#!/usr/bin/python
import MySQLdb

values = [5, 90, 10, 2, 1]

conn = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="root", # your password
                      db="tbl_thermostat") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the query you need
cur = conn.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM tbl_room_info")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0],"|", row[1], "|", row[2],"|", row[3],"|", row[4]

#insert into DB
try:
	#sql = "INSERT INTO tbl_room_info (device_id, temperature,humidity,light,occupancy)values (?,?,?,?,?);"
	#cur.execute(sql,(5,90.0,10.0,2,1))
	cur.execute("INSERT INTO tbl_room_info (device_id, temperature, humidity, light, occupancy) values ( %s, %s, %s, %s, %s)", (values[0], values[1], values[2], values[3], values[4]))
	conn.commit()
	print 'success'
except MySQLdb.Error, e:
	conn.rollback()
	print 'failed: %s' %e

conn.close()

print "Finished"
