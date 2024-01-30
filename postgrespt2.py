"""
TOPIC POSTGRES PART 2

"""
#Import the module - psycopg2
import psycopg2

#Define and initialize all the important variables
conn = None #This variable for database connection
cur = None #Cursor -> It is a temporary data structure to handle rows/tuples fetched from a database
hostname = 'localhost'
databasename = 'postgres'
username ='postgres'
mypassword = 'postgres'
portnumber = 5432

try:
    conn = psycopg2.connect(host = hostname,
                            dbname = databasename,
                            user = username,
                            password = mypassword,
                            port = portnumber)
    
    print("1:your database has been connected successfully...")
    cur = conn.cursor()
    # print('conn', conn)
    # print('cur', cur)
    
except Exception as db_connect_error:
    print(db_connect_error)

finally:
    if cur is not None:
        cur.close()
    #if conn is not None:
     #   conn.close()
    
#Drop table
try:
    cur = conn.cursor()
    drop_table_script = """DROP TABLE IF EXISTS STUDENT_T;"""
    cur.execute(drop_table_script)
    conn.commit()
    print('2:The database table STUDENT_T has been permanently deleted from the database...')
except Exception as db_delete_table_error:
    print(db_delete_table_error)
# finally:
#     if cur is not None:
#         cur.close()
    
 
#Create table STUDENT_T
create_table_script = """CREATE TABLE IF NOT EXISTS STUDENT_T
                             (stud_id CHAR(5) PRIMARY KEY NOT NULL,
                              stud_name VARCHAR(40) NOT NULL,
                              stud_age INT NOT NULL,
                              stud_salary REAL NULL,
                              stud_email_id VARCHAR(40) NULL,
                              stud_gender CHAR(1) NOT NULL);"""
try:
    if cur is not None:
        cur.execute(create_table_script)
        conn.commit() #Each transaction (writing, deletion) must be commited
        print('3:The STUDENT_T - database table has been created successfully...')
    else:
        print('The cursor has been closed...')
        
except Exception as db_create_error:
    print(db_create_error)
finally:
    if cur is not None:
        cur.close()
    
#Insert tuple into table
insert_tuple_script = """INSERT INTO STUDENT_T(stud_id,stud_name,stud_age,stud_salary,stud_email_id,stud_gender)
                         VALUES ('S0001','ZAILAN',39,500.00,'zaila@gmail.com','M'),
                                ('S0002','MARIE',12,500.00,'marie@gmail.com','F');"""

try:
    cur = conn.cursor()
    cur.execute(insert_tuple_script)
    conn.commit()
    print('4:The new row has been added into the system successfully...')

except Exception as insert_error:
    print(insert_error)
finally:
    if cur is not None:
        cur.close()
    
#Display the students' data found
select_script = """SELECT * FROM STUDENT_T WHERE (stud_age BETWEEN 10 AND 20);"""
try:
    cur = conn.cursor()
    cur.execute(select_script)
    rows = cur.fetchall()
    for data in rows:
        print('ID: ', data[0])
        print('Name: ', data[1])
        print('Age: ', data[2])
        print('Salary: ', data[3])
        print('Email ID: ', data[4])
        print('Gender:', data[5])

except Exception as select_error:
    print(select_error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    
    
    
    
    
    
    