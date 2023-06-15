import pymysql
from ignore import user, password, db


def dbConn():
    connect = pymysql.connect(
        host='localhost', 
        user=user, 
        password=password, 
        db=db, 
        charset='utf8mb4',
        )
    return connect
    
def dbInsert(sql, conn):

    #Insert Query
    # sql = f"INSERT INTO PACKAGES (id, name, dest, root) VALUES ({id}, {name}, {dest}, {root});"

    conn.cursor().execute(sql)
    conn.commit()

def dbSelect(sql, conn):
    # Select Query
    # cur.execute("SELECT id, name, arrive, dest, root FROM PACKAGES")
    cur = conn.cursor()
    cur.execute(sql)
    
    return cur

def hubSelect(conn, name, dest):
    sql = f"SELECT que FROM HUBS WHERE name='{name}' AND dest='{dest}';"
    cur = conn.cursor()
    cur.execute(sql)

    if cur.rowcount == 0:
        return []

    que = cur.fetchone()[0]
    
    if not que:
        return []
    
    que = que.split('-')
    hq = list()
    for q in que:
        hq.append(int(q))
        
    return hq

# def hubInsert(conn, name, dest, que):
#     sql = f"INSERT INTO FROM HUBS (que) VALUES ({que}) WHERE name='{name}' AND dest='{dest}'"
#     cur = conn.cursor()
#     cur.execute(sql)
#     conn.commit()
    
def hubUpdate(conn, name, dest, que):
    sql = f"UPDATE HUBS SET que = '{que}' WHERE name='{name}' AND dest='{dest}';"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    

def dbDisconnect(conn):
    conn.close()

def resultPrt(cur):
    row = cur.fetchone()
    #cur.fetchall()
    
    while row:
        print(row)
        row = cur.fetchone()
        
def nodeInit(rows):
    dic = dict()
    for row in rows:
        if not row[0] in dic:
            dic[row[0]] = dict()
            
        if not row[1] in dic:
            dic[row[1]] = dict()
            
        dic[row[0]][row[1]] = row[2]
        dic[row[1]][row[0]] = row[2]
    
    print("===========gragh===========")
    for k in dic.keys():
        print(f"{k} : {dic[k]}")
    print("===========================")
        
    return dic
    