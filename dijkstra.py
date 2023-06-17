import heapq  # 우선순위 큐 구현을 위함
from db import dbSelect
from db import hubSelect, hubUpdate 

# 물류 하나 당 가중치
WEIGHT = 5

def dijkstra(graph, final, conn):
    distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
    distances['A'] = 0  # 시작 값은 0이어야 함
    queue = []
    routes = {'A': [], 'B': [], 'C': [], 'D': [],
              'E': [], 'F': [], 'G': [], 'H': [], 'I': []}  # 최적 루트 경로 저장
    heapq.heappush(queue, [distances['A'], 'A'])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝

        # 탐색 할 노드, 거리를 가져옴.
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            
            hub = hubSelect(conn, current_destination, new_destination)
            
            if len(hub) > 3:
                distance += len(hub) * 2
            else:
                distance += len(hub) * 5
            
            # for hub in hubs:
            #     if hub.check(current_destination, new_destination):
            #         distance += hub.weight() # 해당 노드를 거쳐 갈 때 거리

            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance

                # 경로 저장
                routes[new_destination] = []
                for route in routes[current_destination]:
                    routes[new_destination].append(route)
                routes[new_destination].append(new_destination)

                # 다음 인접 거리를 계산 하기 위해 큐에 삽입
                heapq.heappush(queue, [distance, new_destination])

    result = list()
    result.append(distances[final])
    result.append(routes[final])

    return result

def full(arr, dest, id, conn):
    print(f"arr:{arr}, dest:{dest}")
    # for h in hubs:
    #     if h.check(arr, dest):
    #         hub = h  # 현재 물류가 위치한 허브의 큐
    # print(f'{current} Hubs Queue : {queue}')
    
    que = hubSelect(conn, arr, dest)
    
    que.append(id)
    
    s=''
    for q in que:
        print('q')
        print(q)
        s += str(q)
        s += '-' 
    s = s[:-1]
    print(s)
    
    hubUpdate(conn, arr, dest, s)

    if len(que) == 5:  # 허브 큐가 가득찼을때

        for q in que:  # 허브 큐에 차있는 개수만큼 반복
            # pop = hub.que.popleft()  # 허브 큐에 차있는 물류 꺼내기

            print(f'POP : {q}')
            
            # select pop's routes
            sql = f"SELECT root FROM PACKAGES WHERE id={q}"
            cur = dbSelect(sql, conn)
            route = cur.fetchone()[0].split('-')
            
            # print(f'pop routes  :{route}')
            # print(f'dest"{dest} route[-1]:{route[-1]}')
            if dest == route[-1]:
                continue
            
            index = route.index(dest) + 1  # 꺼낸 물류의 경로 중 다음 경로 인덱스
            
            # print(f'next : {route[index]}')

            full(dest, route[index], q, conn)

            print("------------")
            
        hubUpdate(conn, arr, dest, '')