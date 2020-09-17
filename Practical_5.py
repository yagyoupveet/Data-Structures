class search:
    def __init__(self, l, e, type):
        self.l = l
        self.e = e
        self.type = type
        if type == 'l' or 'L':
            if self.linear():
                print('Element Present at ', self.linear())
            else:
                print("Element Not there!")
        elif type == 'B' or 'b':
            if self.binary() != -1: 
                print("Element is present at index", str(self.binary())) 
            else: 
                print("Element is not present in array")
        else:
            print('Enter a valide type of Search')
    
    def linear(self): 
        for i in range(len(self.l)):
            if self.l[i] == self.e:
                return i
        return False

    def binary(self):
        low = 0
        high = len(self.l) - 1
        mid = 0
  
        while low <= high: 
            mid = (high + low) // 2
            if self.l[mid] < self.e: 
                low = mid + 1 
            elif self.l[mid] > self.e: 
                high = mid - 1 
            else: 
                return mid 
        return -1


a = [1,8,3,4,5,9,2,7]
search(a, 8,'b')