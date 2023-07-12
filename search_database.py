import mysql.connector as mysql

# connect to MySQL server


#CREATE USER 'tmp_root'@'10.3.0.165' IDENTIFIED BY 'Elfx61gt56t';
#GRANT SELECT ON tbccharacters.* TO 'tmp_root'@'10.3.0.165' WITH GRANT OPTION;
#FLUSH PRIVILEGES;

db_connection = mysql.connect(host='10.3.0.175', database="tbccharacters",user="tmp_root", password='Elfx61gt56t')

# Get a cursor
database_cursor = db_connection.cursor()


database_cursor.execute("select * from information_schema.tables;") #################  WE GET ALL TABLES

returned_data = database_cursor.fetchall()


for table in returned_data:
    #table[2] # here we get the table name and append it to list
    # do another MYSQL query here for "string" in all returned data

    try:
        database_cursor.execute("select * from " + table[2] + " ;") #################  WE GET ALL TABLES
        table_data = database_cursor.fetchall()
        #print(table_data)
        if "Warglaive of Azzinoth" in table_data:
            print(table_data)
    except Exception as e:
        #print("failed to connect to - " , table[2] , "// ERROR - " , e)
        pass



