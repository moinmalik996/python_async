import sys
import threading
from queue import Queue
from cutlery_class import Cutlery


kitchen = Cutlery(knives=100, forks=100)


class ThreadBot(threading.Thread):
    def __init__(self):
        super().__init__(target=self.manage_table)
        self.cutlery = Cutlery(knives=0, forks=0)
        self.tasks = Queue()
        
    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == 'prepare table':
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == 'clear table':
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == 'shutdown':
                return
        


bots = [ThreadBot() for i in range(10)]

for bot in bots:
    for i in range(int(sys.argv[1])):
        bot.tasks.put('prepare table')
        bot.tasks.put('clear table')
    bot.tasks.put('shutdown')
    
print('Kitchen inventory before service:', kitchen)
for bot in bots:
    bot.start()
    
for bot in bots:
    bot.join()
    
print('Kitchen inventory after service:', kitchen)
