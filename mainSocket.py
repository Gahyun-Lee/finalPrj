from db import dbConn, dbSelect, nodeInit, dbDisconnect, dbInsert, resultPrt
from dijkstra import dijkstra, full
from client import sockctConn, client
# from collections import deque
# from hubQueue import createQ
from servo import servo1, servo2, servo3, servo4, servoClean, servoSet

#DB Connect
conn = dbConn()

#Socket Connect
client_socket = sockctConn()

#Servo Connect
servo = servoSet()

#Init Node(db hubs -> gragh)
sql = "SELECT name, dest, weight FROM HUBS"
cur = dbSelect(sql, conn)
rows = cur.fetchall()
graph = nodeInit(rows)

#Create Hub-Hub Queue
# hubs = createQ(rows)

print("waiting to start...")
while True:
    data = client(client_socket)
    
    sql = "SELECT id FROM PACKAGES"
    cur = dbSelect(sql, conn)
    rows = cur.fetchall()
    
    same = False
    for row in rows:
        print(row[0])
        if int(data[0]) == row[0]:
            print("There's same package!!")
            same = True
    
    if same:
        continue 
    
    if data[3] == 1:
        print("servo4")
        servo4(servo[3])
        continue
    
    print(f"received data : {data}")
    id = data[0]
    pkgName = data[1] #Package Name
    destHub = data[2] #Destination Hub
    
    #dijkstra with received data
    result = dijkstra(graph, destHub, conn) #[weight, [route]]
    
    print(f'Result : {result}')
    # print(f'Routes : {routes}')
    
    route = '-'.join(result[1])
    
    if result[1][0] == 'B':
        print("servo1")
        servo1(servo[0])
    elif result[1][0] == 'C':
        print("servo2")
        servo2(servo[1])
    elif result[1][0] == 'D':
        print("servo3")
        servo3(servo[2])
    
    #save packag information - id, name, dest, route
    sql = f"INSERT INTO PACKAGES (id, name, dest, root) VALUES ({id}, '{pkgName}', '{destHub}', '{route}');"
    dbInsert(sql, conn)
    
    arr = 'A'  # 물류의 현재 허브 위치
    dest = result[1][0]
    full(arr, dest, id, conn) #check if queue is full
    
    print()
    
    sql = 'SELECT que FROM HUBS'
    cur = dbSelect(sql, conn)
    resultPrt(cur)
    
    print()
    print('--------------------------------------------')
    
    #STOP while when there's problem
    pass

#DB Disconnect
dbDisconnect(conn)
client_socket.close()
servoClean()