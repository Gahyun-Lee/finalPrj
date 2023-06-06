from collections import deque

class hQu:
    
    def __init__(self, arr, dest):
        self.arr = arr
        self.dest = dest
        self.que = deque(maxlen=3)
        
    def weight(self):
        size = len(self.que)
        if size > 3:
            return 0
        w = size * 5
        return w
    
    def check(self, arr, dest):
        if (self.arr == arr) and (self.dest == dest):
            return True
        return False
    
    def prt(self):
        print(self.arr, self.dest, self.que)

def createQ(rows):
    queue = list()
    for row in rows:
        q = hQu(row[0], row[1])
        q.prt()
        queue.append(q)
    return queue
            
# gragh = {
#     'A': {'B': 4, 'C': 5},
#     'B': {'C': 7, 'D': 10}
# }

# tu = (
#     ('A', 'B', 4),
#     ('A', 'C', 5),
#     ('B', 'D', 10),
#     ('D', 'F', 7)
# )
# q = createQ(tu)
# for qq in q:
# #     qq.prt()
#     if qq.check('A', 'C'):
#         que = qq.que
        
# que.append('a')
# que.append('b')
# que.append('c')

# for gg in q:
#     gg.prt()

# while que:
#     print(que.popleft())