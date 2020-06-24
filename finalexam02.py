import math
class Point:
    x=0
    y=0
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def distance(self, other):
        return math.sqrt(pow(self.x-other.x,2)+pow(self.y-other.y,2))
    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)

if __name__ == "__main__":
    p1= Point(1,1)
    p2= Point(2,2)
    print(Point.distance(p1,p2))
    p3=p1+p2
    print("("+str(p3.x)+", "+str(p3.y)+")")


