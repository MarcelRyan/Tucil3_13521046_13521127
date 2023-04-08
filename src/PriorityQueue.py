from datatype.Graph import *

class PriorityQueue:
    # CONSTRUCTOR 
    def __init__(self):
        self.queue = []
    
    # GETTER
    def getQueue(self):
        return self.queue
    
    def isEmpty(self):
        return len(self.queue) == 0

    # Oke w coba jelasin dlu ini prio queue w gimana. Jadi ini prioqueue tu elemennya tuple yang isinya {location, weight, path}
    # jadi itu tu ada lokasi yang harus dicek selanjutnya sama ada weightnya (jarak dari lokasi sebelumnya sm lokasi ini) 
    # sama ada path nah path ini isinya dia tu udah ngelewatin lokasi mana aja buat sampe lokasi sekarang
    
    # Sama sistem prioqueue yg w kepikir ini jdi kayak dia dequeue headnya dulu yg weightnya terkecil nah nanti
    # langsung jadiin elemen yang di dequeue tadi buat jadi parameter di enqueue. Karena prioqueue pny w
    # dia tu enqueue semua tetangga-tetangganya bukan node itu sendiri
    # jadi misal dia jadiin tuple ini {itb, 264, "tubis-djuanda-itb"} di parameter enqueue. Ini dia bakal enqueue semua tetangganya itb 
    # jadi ntar tetangga itb nya yang masuk ke queue berdasarkan jarak dia ke itb sama pathnya bakal berubah ditambah nama lokasi tetangganya
    # misal sabuga tetangga itb ntar bakal dimasukin ke queue tuplenya gini {sabuga, 115, "tubis-djuanda-itb-sabuga"} gitu
    # nah tapi w belum testing samsek baru tulis apa yang kepikir aja jadi kalau misal ngerasa terlalu ribet mw ganti aja gapapa si AKWKAKKWAKAW

    # FUNCTION TO ADD ELEMENT TO THE QUEUE BASED ON WEIGHT
    def enqueue(self, head):
        if (not self.isEmpty()):
            for neighbor, weight in head[0].getWeight():

                index = len(self.queue)
                for i in range(len(self.queue)):

                    # IF ELEMENT WITH HIGHER WEIGHT IS FOUND IN THE QUEUE
                    if (self.queue[i][1] > weight):

                        # LOOPING TO MOVE ELEMENT AT QUEUE SO THAT THERE IS AN EMPTY SPACE FOR NEW ELEMENT
                        for j in range(len(self.queue), i):
                            self.queue[j] = self.queue[j-1]
                        index = i
                        break
                
                self.queue.insert(index, {neighbor, weight, head[2] + "-" + neighbor.getName()})
        else:
            self.queue.append(head)

    # FUNCTION TO REMOVE THE FIRST ELEMENT FROM QUEUE TO BE CHECKED
    def dequeue(self):
        return self.queue.pop(0)
    