import sqlite3

def executeQuery(query):
    conn = sqlite3.connect('quizdb.db')   
    curr = conn.execute(query)
    rs = curr.fetchall()
    close(conn, curr)
    return rs

def executeDMLQuery(query):
    conn = sqlite3.connect('quizdb.db')   
    curr = conn.execute(query)
    conn.commit()
    close(conn, curr)
    return True

def close(conn, curr):
    curr.close()
    conn.close()
    return True