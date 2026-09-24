class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        #time is the moment the chef finishes cooking the previous meal
        total_waiting_time = 0
        time = 0
        for c in customers:
            if c[0] > time:
                waiting_time = 0
                time = c[0]
            else: 
                waiting_time = time - c[0]
            waiting_time += c[1]
            time += c[1]
            total_waiting_time += waiting_time
        return total_waiting_time / len(customers)



        