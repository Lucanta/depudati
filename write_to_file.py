import sqlite3
import pandas as pd
import numpy as np
from os import path

def write_poll_to_csv(poll_id,question_no,poll_results,filename,no_of_parties):
    
    if(path.exists(filename)):
        # Load dataframe
        dataframe = pd.read_csv(filename,header=None,delimiter=';',error_bad_lines=False)
        # Check if poll_id is already present in csv file
        is_poll_in_file = poll_id in dataframe[0].unique()
        # Check if question is already present in csv file
        subdf = dataframe.loc[dataframe[0]==poll_id]
        is_question_in_poll = question_no in subdf[1].unique()

        # Write data if at least one of the two conditions applies
        if ((not is_poll_in_file) or (not is_question_in_poll)):
            row_to_add = pd.Series(np.append([poll_id,question_no],poll_results))
            print(row_to_add)
            dataframe = dataframe.append(row_to_add,ignore_index=True)
            dataframe.to_csv(filename,header=None,index=False,index_label=False,sep=';',line_terminator='\n')
            
    else:
        print(poll_results)
        row_to_add = pd.DataFrame([np.append([poll_id,question_no],poll_results)],index=None,columns=range(no_of_parties+2))
        print(row_to_add)
        row_to_add.to_csv(filename,header=None,index=False,index_label=False,columns=range(no_of_parties+2),sep=';',line_terminator='\n')
        
def write_metadata_to_SQL(db_path,table_name,poll_id,pollster_name,start_date_fw,end_date_fw,sample_size,method):
    
    # Insert poll metadata on a SQL database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # SQL statement that adds values to the table
    insert_stmt = ("INSERT INTO "+table_name+" VALUES (?, ?, ?, ?, ?, ?);")
    data = (poll_id,pollster_name,start_date_fw,end_date_fw,sample_size,method)
    try:
        c.execute(insert_stmt,data)
    except sqlite3.Error as e:
        print(e)
        print("Metadata about this poll are already present in the SQL database")
    finally:
        conn.commit()
        conn.close()
        
def write_question_to_SQL(db_path,table_name,poll_id,question_no,question_text):
    
    # Insert poll questions on a SQL database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # SQL statement that adds the question to the table
    insert_stmt = ("INSERT INTO "+table_name+" VALUES (?, ?, ?);")
    data = (poll_id,question_no,question_text)
    try:
        c.execute(insert_stmt,data)
    except sqlite3.Error as e:
        print(e)
        print("This poll's question is already present in the SQL database")
    finally:
        conn.commit()
        conn.close()   
        
def write_poll_to_SQL(db_path,table_name,poll_id,question_no,no_of_parties,poll_results):
    
    # Insert poll results on a SQL database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # Count the number of columns
    #ncols = c.execute("SELECT Count(*) FROM INFORMATION_SCHEMA.Columns where TABLE_NAME ="+table_name+";")
    columnsQuery = "PRAGMA table_info(%s)" % table_name
    c.execute(columnsQuery)
    ncols = len(c.fetchall())
    if(ncols<(no_of_parties+2)):
        # Add column(s) to database
        for j in range(no_of_parties+2-ncols):
            col_name = 'party'+str(ncols-2+j)
            c.execute("ALTER TABLE "+table_name+" ADD "+col_name+" REAL;")
    # SQL statement that inserts poll data
    insert_stmt = ("INSERT INTO "+table_name+" VALUES (?"+",?"*(no_of_parties+1)+");")
    data = (poll_id,question_no)+tuple(poll_results)
    try:
        c.execute(insert_stmt,data)
    except sqlite3.Error as e:
        print(e)
        print("This poll's question is already present in the SQL database")
    finally:
        conn.commit()
        conn.close()  