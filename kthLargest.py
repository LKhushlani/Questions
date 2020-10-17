from collections import Counter

import heapq

class KthMostRepeated:

    def __init__(self):
        self.li = []

    def insertInList(self,s):
        self.li.append(s)

    def calculate_kthMostFrequent(self,k):
        
        print("List is", self.li)
        hashmap = Counter(self.li)
        print(hashmap.most_common(k)[-1][0])



obj = KthMostRepeated()
obj.insertInList("orange")
obj.insertInList("orange")
obj.insertInList("apple")
obj.insertInList("orange")
obj.insertInList("orange")
obj.insertInList("mango")
obj.insertInList("mango")
obj.calculate_kthMostFrequent(1)

        



            




