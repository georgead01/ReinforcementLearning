import random

class Agent:

    def __init__(self, environment, initial_state = None, learning_rate = 0.1, discount_rate = 0.9, epsilon = 0.5):
        self.env = environment
        
        if initial_state is None:
            self.state = random.choice(environment.states)
        else:
            self.state = initial_state

        self.q_table = {}
        for state in environment.states:
            for action in environment.actions:
                self.q_table[state, action] = 0

        self.learning_rate = learning_rate
        self.discount_rate = discount_rate
        self.epsilon = epsilon

        self.reward = 0

    def step(self, learn = True):
        if random.random() < self.epsilon and learn:
            action = random.choice(self.env.actions)
        else:
            action = max(self.env.actions, key = lambda a: self.q_table[self.state, a])

        new_state = self.env.transition(self.state, action)
        new_action = max(self.env.actions, key = lambda a: self.q_table[new_state, a])
        
        reward = self.env.reward(new_state)
        
        #print(f'action: {action}, new_state: {new_state}, reward: {reward}')

        self.q_table[self.state, action] = self.q_table[self.state, action] + self.learning_rate*(reward + self.discount_rate*self.q_table[new_state, new_action]-self.q_table[self.state, action])

        self.state = new_state
        self.reward += reward

    def train(self, iters = 1000):
        self.reward = 0
        self.state = random.choice(self.env.states)
        for i in range(iters):
            self.step()

    def run(self, stopping_condition = None):
        if not stopping_condition:
            def stopping_condition(agent):
                return False

        self.reward = 0
        while not stopping_condition(self):
            self.step(learn = False)