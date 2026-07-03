class GridWorld:
    def __init__(self):
        self.rows=10; self.cols=10
        self.start=(0,0); self.goal=(9,9)
        self.obstacles={(1,1),(1,2),(2,4),(4,3),(4,4),(6,1),(8,2)}
        self.reset()
    def reset(self):
        self.agent=self.start
        return self.agent
    def state_index(self,s):
        return s[0]*self.cols+s[1]
    def valid(self,p):
        r,c=p
        return 0<=r<self.rows and 0<=c<self.cols and p not in self.obstacles
    def step(self,a):
        r,c=self.agent
        d={0:(-1,0),1:(1,0),2:(0,-1),3:(0,1)}[a]
        n=(r+d[0],c+d[1])
        if not self.valid(n):
            return self.agent,-10,False
        self.agent=n
        if n==self.goal:
            return n,100,True
        return n,-1,False
