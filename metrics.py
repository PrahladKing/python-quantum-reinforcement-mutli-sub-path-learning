import csv
import matplotlib.pyplot as plt

class Metrics:
    def __init__(self):
        self.rewards=[]

    def add_reward(self,r):
        self.rewards.append(r)

    def save(self):
        with open('results/rewards.csv','w',newline='') as f:
            w=csv.writer(f)
            w.writerow(['Episode','Reward'])
            for i,r in enumerate(self.rewards):
                w.writerow([i,r])

    def plot_rewards(self):
        plt.figure(figsize=(8,5))
        plt.plot(self.rewards)
        plt.grid(True)
        plt.xlabel('Episode')
        plt.ylabel('Reward')
        plt.savefig('results/rewards.png')
