from collections import deque
import random
found=False

sites=[{"X":2, "Y":1, "battery_pack":False},
    {"X":3, "Y":1, "battery_pack":False},
    {"X":3, "Y":3, "battery_pack":False}]
sites_queue=deque(sites)

def find_battery_pack(sites_queue):
    visited_sites=set()
    found=False
        
    while not found and sites_queue:
        print("Checking site at X:",sites_queue[0]["X"],"Y:",sites_queue[0]["Y"])
        dequeued=sites_queue.popleft()
        coord=(dequeued["X"],dequeued["Y"])
        if coord in visited_sites:
            continue
        visited_sites.add(coord)
        if dequeued["battery_pack"]==True:
            found=True
            return "Found at",dequeued["X"],dequeued["Y"]
        else:
            enqueued=dequeued
            enqueued["X"]=enqueued["X"]+1
            enqueued["Y"]=enqueued["Y"]+1
            enqueued["battery_pack"]=random.random() < 0.1
            sites_queue.append(enqueued)

print(find_battery_pack(sites_queue))