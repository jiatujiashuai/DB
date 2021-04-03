from db_table import db_table
from sys import argv
import os.path
import pandas as pd
import xlrd

def Parseexcel(fname):
    df = pd.read_excel(
        fname,
        #sheet_name= "Agenda Database",
        header = 14,
        names=['Date', 'Time_Start', 'Time_End', 'Session', 'Session_Title', 'Room_Location', 'Description', 'Speakers'])
    df.head()
    print(df.columns)

    users = db_table("Agenda", {"id": "integer PRIMARY KEY",
                                "Date": "text NOT NULL",
                                "Time_Start": "text NOT NULL",
                                "Time_End": "text NOT NULL",
                                "Session": "text NOT NULL",
                                "Session_Title": "text NOT NULL",
                                "Room_Location": "text",
                                "Description": "text",
                                "Speakers": "text"})

    df.to_sql('Agenda', users.db_conn, if_exists='append', index=False)
    users.close()


if __name__ == "__main__":
    filename = None
    try:
        filename = argv[1]
        print("The name of the agenda excel file is", filename)
        if (not os.path.isfile(filename)):
            raise ValueError("The file does not exist.")
        pass
    except Exception:
        print("Please double check the input.")
        raise

Parseexcel(filename)


