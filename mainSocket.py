from db import dbConn, dbSelect, nodeInit, dbDisconnect, dbInsert
from dijkstra import dijkstra, full
from client import sockctConn, client
# from collections import deque
from hubQueue import createQ

# hubs = {
#     'A': deque(maxlen=3),
#     'B': deque(maxlen=3),
#     'C': deque(maxlen=3),
#     'D': deque(maxlen=3),
#     'E': deque(maxlen=3),
#     'F': deque(maxlen=3),
#     'G': deque(maxlen=3),
#     'H': deque(maxlen=3),
#     'I': deque(maxlen=3),
# }

#DB Connect
conn = dbConn()

#Socket Connect
client_socket = sockctConn()

#Init Node(db hubs -> gragh)
sql = "SELECT name, dest, weight FROM HUBS"
cur = dbSelect(sql, conn)
rows = cur.fetchall()
graph = nodeInit(rows)

#Create Hub-Hub Queue
hubs = createQ(rows)

print("waiting to start...")
while True:
    data = client(client_socket)
    
    if data[1] == 'quit':
        print("quit")
        break
    
    print(f"received data : {data}")
    id = data[0]
    pkgName = data[1] #Package Name
    destHub = data[2] #Destination Hub
    
    #dijkstra with received data
    result = dijkstra(graph, destHub, hubs) #[weight, [route]]
    
    print(f'Result : {result}')
    # print(f'Routes : {routes}')
    
    route = '-'.join(result[1])
    
    #save packag information - id, name, dest, route
    sql = f"INSERT INTO PACKAGES (id, name, dest, root) VALUES ({id}, '{pkgName}', '{destHub}', '{route}');"
    dbInsert(sql, conn)
    
    arr = 'A'  # 물류의 현재 허브 위치
    dest = result[1][0]
    full(hubs, arr, dest, id, conn) #check if queue is full
    
    print()
    for hub in hubs:
        hub.prt()
    
    print()
    print('--------------------------------------------')
    
    #STOP while when there's problem
    pass

#DB Disconnect
dbDisconnect(conn)
client_socket.close()