from collections import deque
import time

def next_ticket(q):
    if not q:
        print("No more tickets.")
    else:
        print('Next ticket:', q[0])
        return q[0]
    
#--------LIST VERSION--------
list_queue = []
for i in range(101, 106):
    list_queue.append(i)

print("List Queue:", list_queue)
start=time.perf_counter()
while list_queue:
    next_ticket(list_queue)
    list_queue.pop(0)
end=time.perf_counter()
print(f"List finished in {end-start:.5f}s\n")

#--------DEQUE VERSION--------
deque_queue = deque()
for i in range(101, 106):
    deque_queue.append(i)   
print("Deque Queue:", deque_queue)
start=time.perf_counter()   
while deque_queue:
    next_ticket(deque_queue)
    deque_queue.popleft()
end=time.perf_counter()
print(f"Deque finished in {end-start:.5f}s\n")
