import sqlite3

def executeQuery(query):
    conn = sqlite3.connect('quizdb.db')   
    curr = conn.execute(query)
    rs = curr.fetchall()
    close(conn, curr)
    return rs

def close(conn, curr):
    curr.close()
    conn.close()
    return True