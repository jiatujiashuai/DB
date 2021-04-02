from db_table import db_table
from sys import argv
import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("interview_test.db")
    except Exception:
        print("The database does not exist.")

    return conn

def lookup_database(conn, column, data):
    cur = conn.cursor()
    #query = "SELECT * FROM Agenda WHERE %s=%s" %(column, data)
    query = "SELECT * FROM Agenda WHERE %s=?" %column
    cur.execute(query,(data,))
    print(data)
    #cur.execute(query)
    for row in cur:
        print(row)


if __name__ == "__main__":
    try:
        column_name = argv[1]
        data_name = ''
        for i in range(2, len(argv)):
            data_name += argv[i]
            data_name += ' '
        #data_name = argv[2]
        data_name = data_name[0:-1]
        print(data_name)
        if column_name in ['Date', 'Time_Start', 'Time_End', 'Session', 'Session_Title', 'Room_Location', 'Description', 'Speakers']:
            lookup_database(create_connection(), column_name, data_name)
        else:
            raise ValueError("The column does not exist.")
        pass
    except Exception:
        print("Please double check the input.")
        raise


