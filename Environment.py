from Agent import *
import random
import matplotlib.pyplot as plt
import turtle
import time


class Environment:

    def __init__(self, states, actions, transition, reward, agents = None):
        self.states = states.copy()
        self.actions = actions.copy()
        self.transition = transition
        self.reward = reward

        if agents:
            self.agents = agents.copy()
        else:
            self.agents = []

    def add_agent(self, initial_state = None, learning_rate = 0.1, discount_rate = 0.9, epsilon = 0.5):
        new_agent = Agent(self, initial_state, learning_rate, discount_rate, epsilon)
        self.agents.append(new_agent)
        return new_agent

if __name__ == '__main__':

    board_size = 6
    reward_state = (board_size-1, board_size-1)
    cell_size = 50
    x_shift = (board_size/2)*cell_size
    y_shift = -(board_size/2)*cell_size
    margin = cell_size

    states = [(i,j) for i in range(board_size) for j in range(board_size)] #board
    actions = [0, 1, 2, 3] # 0: left, 1: up, 2: right, 3: down
    
    def transition(state, action):
        x = state[0]
        y = state[1]

        if action == 0:
            x = max(0, x-1)
        elif action == 1:
            y = max(0, y-1)
        elif action == 2:
            x = min(board_size-1, x+1)
        elif action == 3:
            y = min(board_size-1, y+1)

        return (x,y)

    def reward(state):
        if state == reward_state:
            return 1
        return -1

    env = Environment(states, actions, transition, reward)
    agent1 = env.add_agent()

    for _ in range(100):
        agent1.train()

    turtle.setup(board_size*cell_size+margin, board_size*cell_size+margin)
    turtle.tracer(1000)
    turtle.hideturtle()
    turtle.pu()
    
    for x in range(board_size+1):
        turtle.goto((x-board_size)*cell_size+x_shift, board_size*cell_size+y_shift)
        turtle.pd()
        turtle.goto((x-board_size)*cell_size+x_shift, y_shift)
        turtle.pu()

    for y in range(board_size+1):
        turtle.goto(-board_size*cell_size+x_shift, (board_size-y)*cell_size+y_shift)
        turtle.pd()
        turtle.goto(x_shift, (board_size-y)*cell_size+y_shift)
        turtle.pu()

    def goto_state(turtle, state):
        x, y = state
        turtle.goto((x-board_size+0.5)*cell_size+x_shift, (board_size-y-0.5)*cell_size+y_shift)
        time.sleep(0.5)


    turtle1 = turtle.Turtle()
    turtle1.pu()
    turtle1.shape('circle')
    turtle1.color('red')

    agent1.state = (0,0)
    goto_state(turtle1, agent1.state)
    turtle.tracer(1)

    steps1 = 0
    print(f'starting in state: {agent1.state}')
    while agent1.state != reward_state:
        agent1.step(learn = False)
        goto_state(turtle1, agent1.state)
        steps1 += 1
        print(f'agent1 in state:{agent1.state}')
    turtle1.hideturtle()
    turtle.bye()

    print(f'it took the agent1 {steps1} steps to get to the target')

    graph_array = [[0 for _ in range(board_size)].copy() for _ in range(board_size)]

    for state in states:
        optimal_action = max(actions, key = lambda a: agent1.q_table[state, a])
        graph_array[state[0]][state[1]] = agent1.q_table[state, optimal_action]


    plt.style.use('_mpl-gallery-nogrid')
    fig, ax = plt.subplots()
    ax.imshow(graph_array)
    plt.show()