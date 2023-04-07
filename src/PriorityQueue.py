class PriorityQueue:
    # CONSTRUCTOR 
    def __init__(self):
        self.queue = []
    
    # GETTER
    def getQueue(self):
        return self.queue
    
    def isEmpty(self):
        return len(self.queue) == 0

    # FUNCTION TO ADD ELEMENT TO THE QUEUE BASED ON PRIORITY
    def enqueue(self, number):
        if (not self.isEmpty()):
            index = len(self.queue)
            for i in range(len(self.queue)):

                # IF ELEMENT WITH HIGHER PRIORITY IS FOUND IN THE QUEUE
                if (self.queue[i] > number):

                    # LOOPING TO MOVE ELEMENT AT QUEUE SO THAT THERE IS AN EMPTY SPACE FOR NEW ELEMENT
                    for j in range(len(self.queue), i):
                        self.queue[j] = self.queue[j-1]
                    index = i
                    break
            
            self.queue.insert(index, number)
        else:
            self.queue.append(number)

    # FUNCTION TO REMOVE THE FIRST ELEMENT FROM QUEUE
    def dequeue(self):
        self.queue.pop(0)