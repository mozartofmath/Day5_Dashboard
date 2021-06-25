import os
import pandas as pd
import pymysql as mysql
from pymysql import Error

def connect_to_db(dbName=None):

    conn = mysql.connect(host='localhost', user='root', password='root',
                         database=dbName)
    cur = conn.cursor()
    return conn, cur

def create_db(dbName: str) -> None:

    conn, cur = connect_to_db()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()

def create_table(dbName: str) -> None:

    conn, cur = connect_to_db(dbName)
    sqlFile = 'schema.sql'
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()

    return

def insert_to_tweet_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:

    conn, cur = connect_to_db(dbName)

    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (clean_text, polarity, subjectivity)
             VALUES(%s, %s, %s);"""
        data = (row[3], row[1], row[2])

        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            #print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return

def db_execute_fetch(query, tablename='', dbName = None) -> pd.DataFrame:
 
    connection, cursor1 = connect_to_db(dbName = dbName)
    cursor1.execute(query)

    # get column names
    field_names = [i[0] for i in cursor1.description]

    # get column values
    res = cursor1.fetchall()

    # get row count and show info
    nrow = cursor1.rowcount
    if tablename:
        print(f"{nrow} recrods fetched from {tablename} table")

    cursor1.close()
    connection.close()

    # return result
    return pd.DataFrame(res, columns=field_names)
    
if __name__ == "__main__":
    connect_to_db(dbName='tweets')
    create_table(dbName='tweets')
    df = pd.read_csv('processed_tweet_data.csv')
    insert_to_tweet_table(dbName='tweets', df=df, table_name='CleanTweetInfo')
