import numpy as np, random
class QLearningAgent:
    def __init__(self,states,actions):
        self.q=np.zeros((states,actions))
        self.alpha=0.1
        self.gamma=0.95
        self.epsilon=1.0
        self.epsilon_decay=0.995
        self.epsilon_min=0.01
        self.actions=actions
    def choose_action(self,s):
        if random.random()<self.epsilon:
            return random.randint(0,self.actions-1)
        return int(np.argmax(self.q[s]))
    def best_action(self,s):
        return int(np.argmax(self.q[s]))
    def learn(self,s,a,r,s2):
        self.q[s,a]+=self.alpha*(r+self.gamma*np.max(self.q[s2])-self.q[s,a])
    def decay(self):
        if self.epsilon>self.epsilon_min:
            self.epsilon*=self.epsilon_decay
