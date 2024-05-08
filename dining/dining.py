import threading

class Philosopher(threading.Thread):
    def __init__(self, name, fork_on_left, fork_on_right):
        threading.Thread.__init__(self)
        self.name = name
        self.fork_on_left = fork_on_left
        self.fork_on_right = fork_on_right

    def run(self):
        self.dine()

    def dine(self):
        while True:
            self.think()
            self.eat()

    def think(self):
        print(f'{self.name} is thinking.')

    def eat(self):
        fork1, fork2 = self.fork_on_left, self.fork_on_right

        while True:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()

        print(f'{self.name} is eating.')
        fork2.release()
        fork1.release()

def dining_philosophers():
    forks = [threading.Semaphore() for n in range(5)]
    philosophers = [Philosopher(f'Philosopher {i}', forks[i%5], forks[(i+1)%5]) for i in range(5)]

    for p in philosophers:
        p.start()

dining_philosophers()