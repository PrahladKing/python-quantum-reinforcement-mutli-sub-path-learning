from environment import GridWorld
from classical_agent import QLearningAgent
from trainer import Trainer
from config import *

env=GridWorld()
agent=QLearningAgent(env.rows*env.cols,4)
trainer=Trainer(env,agent)
trainer.train(EPISODES)
trainer.metrics.save()
trainer.metrics.plot_rewards()
path,done=trainer.evaluate()
print("Goal reached:",done)
print(path)
