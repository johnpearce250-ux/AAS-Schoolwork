from collections import deque

arrivals = ['S1', 'S2']
items = {'S1': ['shoes', 'shirt', 'toothbrush'],
         'S2': ['snacks', 'charger']}

def process_bags(arrivals):
    bag_queue = deque(arrivals)
    while bag_queue:
        current_bag = bag_queue.popleft()

        while items[current_bag]:
            current_item = items[current_bag].pop(0)
            print(f"Processing {current_bag}: popped {current_item}")

process_bags(arrivals)