
"""
create database HANDLES;

CREATE TABLE TWITTER_HANDLES(
	handle_id int auto_increment,
	handle varchar(50) not null,
	primary key (handle_id)
)

this is the database and table created to add handles into
this is using mysql.
"""




import pymysql
import config







def connect():
    conn = pymysql.connect(host='localhost', port=3306 ,database=config.db, user=config.db_user, password=config.db_password)
    print('Connected to MySQL database')
    return conn




def insert_data(connection,handle):
    cursor = connection.cursor()
    sql = "insert into twitter_handles(handle) VALUES('%s')" % (handle)
    cursor.execute(sql)
    connection.commit()
    print("handle added!")
    connection.close()