'''

@Author: Kolapati Mani deepak Chandu

@Date: 2024-01-18 3:30:00

@Last Modified by: Kolapati Mani deepak Chandu

@Last Modified time: 2024-01-18 3:30:00

@Title : creating a stop watch

'''


import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self):
        return self.end_time - self.start_time

# Example usage
stopwatch = Stopwatch()
stopwatch.start()
# Perform some task
stopwatch.stop()
print(f"Elapsed time: {stopwatch.elapsed_time()} seconds")
