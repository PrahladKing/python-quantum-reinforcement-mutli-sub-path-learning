class Trainer:
    def __init__(self, env, agent):
        self.env=env
        self.agent=agent
        from metrics import Metrics
        self.metrics=Metrics()

    def train(self, episodes):
        for ep in range(episodes):
            state=self.env.reset()
            done=False
            total=0
            while not done:
                s=self.env.state_index(state)
                a=self.agent.choose_action(s)
                ns,r,done=self.env.step(a)
                s2=self.env.state_index(ns)
                self.agent.learn(s,a,r,s2)
                state=ns
                total+=r
            self.agent.decay()
            self.metrics.add_reward(total)

    def evaluate(self,max_steps=100):
        state=self.env.reset()
        path=[state]
        done=False
        steps=0
        while not done and steps<max_steps:
            s=self.env.state_index(state)
            a=self.agent.best_action(s)
            state,_,done=self.env.step(a)
            path.append(state)
            steps+=1
        return path,done
