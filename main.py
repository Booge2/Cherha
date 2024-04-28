import queue
import time
import random


#
#
# class Server:
#     def __init__(self):
#         self.request_queue = queue.PriorityQueue()
#         self.request_statistics = []
#
#     def add_request(self, user, priority):
#         request = (user, time.time())
#         self.request_queue.put((priority, request))
#         self.request_statistics.append(request)
#
#     def show_statistics(self):
#         print("Request Statistics:")
#         for i, (user, time_) in enumerate(self.request_statistics):
#             print(f"{i + 1}. User: {user}, Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_))}")
#
#     def process_requests(self):
#         while not self.request_queue.empty():
#             priority, (user, time_) = self.request_queue.get()
#             print(f"Processing request from {user} with priority {priority}...")
#             time.sleep(1)  # Simulate request processing
#             print(f"Request from {user} processed.")
#
#
# server = Server()
#
# users = ["Client1", "Client2", "Client3"]
# for user in users:
#     priority = random.randint(1, 10)
#     server.add_request(user, priority)
#
# server.process_requests()
#
# server.show_statistics()
# Завдання 2
class MarinaBerth:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.passenger_queue = queue.Queue()
        self.boat_queue = queue.Queue()

    def arrival_of_passengers(self):
        time.sleep(random.uniform(1, 5))
        self.passenger_queue.put("Passenger")
        print("Пасажир прибув до пристані.")

    def arrival_of_boats(self):
        time.sleep(random.uniform(10, 30))
        available_seats = random.randint(1, self.max_capacity)
        self.boat_queue.put(available_seats)
        print(f"Катер прибув до пристані є {available_seats} вільних місць.")

    def board_passengers(self):
        while not self.passenger_queue.empty() and not self.boat_queue.empty():
            passengers = min(self.passenger_queue.qsize(), self.boat_queue.get())
            print(f"Сіли в човен {passengers} пасажирів.")
            for _ in range(passengers):
                self.passenger_queue.get()

    def simulate(self):
        while True:
            event = random.choice(["пасажир", "човен"])
            if event == "пасажир":
                self.arrival_of_passengers()
            elif event == "човен":
                self.arrival_of_boats()
                self.board_passengers()

max_capacity = 10

marina = MarinaBerth(max_capacity)

marina.simulate()