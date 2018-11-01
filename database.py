import pymysql
import config
#PERSONAL NOTE: change "pred" to either "Chances are high" or "Chances are low"


#database connection set up, need to move info to a hidden CONFIG file*******
def connect():
    conn = pymysql.connect(host='localhost', port=3306 ,database=config.db, user=config.db_user, password=config.db_password)
    print('Connected to MySQL database')
    return conn


#return the latest entry in the table and return the pred_val (either 0 or 1)
def get_latest_entry(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM prediction order by pred_id DESC limit 1")
    for row in cursor:
        return (row[1])
    connection.close()


#insert our flood prediction into the table
def insert_data(connection,pred_val,pred,date):
    cursor = connection.cursor()
    sql = "insert into prediction(pred_val, pred, pred_date) VALUES('%d','%s','%s')" % (pred_val, pred, date)
    cursor.execute(sql)
    connection.commit()
    connection.close()