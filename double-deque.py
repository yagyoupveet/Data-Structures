class Demo:
    def __init__(self):
        self.myData = []

    def queueFront(self, elements):
        self.myData.append(elements)

    def queueRear(self, elements):
        self.myData.insert(0, elements)

    def is_empty(self):
        return self.len() == 0

    def dequeueFront(self):
        del self.myData[-1]

    def dequeueRear(self):
        del self.myData[0]

    def len(self):
        return len(self.myData)

    def Rear(self):
        return self.myData[0]

    def Front(self):
        return self.myData[-1]

    def data_display(self):
        return self.myData

func = Demo()
func.queueFront(55)
func.queueRear(77)
print(func.data_display())