# ReinforcementLearning
Simple agent/environment classes for RL.

# Agent.py

This file contains the agent class.

## attributes
- `env` (Environment): the environment in which the agent is operating.
- `state`: current state of the agent.
- `q_table` (dict): the q-values of each (state, action) pair.
- `learning_rate` (number): the learning rate of the agent.
- `discount_rate` (number): the discount rate of the agent.
- `epsilon` (number): probability of exploration (vs. optimization) in learning mode.
- `reward` (number): the reward collected by the agent.

## methods
The agent class has the following methods:

### init

Class constructor.
**args:**
- `environment` (Environment): the environment in which the agents lives/operates.
- `initial_state`: The state (if provided) at which the agent starts. If `None`, initial state is chosen randomly from the states in the environment. Default value `None`.
- `learning_rate` (number): the learning rate of the agent. Default value 0.1.
- `discount_rate` (number): the discount rate of the agent. Default value 0.9.
- `epsilon` (number): the probability of exploration (vs. optimization) in learning mode. Default value 0.5.

### step

Takes an action in the environment based on current state, q_table, and learning mode.
**args:**
- `learn` (bool): if `True`, takes optimal action (according to current values of q_table) with probability `1-epsilon`. Otherwise, takes optimal action with probability 1. Default value `True`.

### train

Trains agent `iters` time.
**args:**
- `iters` (int): the number of training iterations.

### run

Runs the agent, taking learned optimal actions, until stopping condition is `True`.
**args:**
- `stopping_condition` (Agent -> bool): function to check if stopping condition is met.

# Environment.py

This file contains the environment class as well as an application using the agent/environment classes.

## attributes
- `states` (iter): the states in the environment.
- `actions` (iter): the actions available to the agents in the environment.
- `transition` (state + action -> state): the transition function.
- `reward` (state -> number): the reward function.
- `agents` (iter<Agent>): the agents living/operating in the environment.

## methods
The environment class has the following methods:

### init

Class constructor.
**args:**
- `states` (iter): the states in the environment.
- `actions` (iter): the actions available to the agents in the environment.
- `transition` (state + action -> state): the transition function.
- `reward` (state -> number): the reward function.
- `agents` (iter<Agent> |`None`): the agents living/operating in the environment (if provided). If `None`, it's set to an empty list. Default value `None`.

### add_agent

Creates a new agent in the environment.
**args:**
- `initial_state`: The state (if provided) at which the agent starts. If `None`, initial state is chosen randomly from the states in the environment. Default value `None`.
- `learning_rate` (number): the learning rate of the agent. Default value 0.1.
- `discount_rate` (number): the discount rate of the agent. Default value 0.9.
- `epsilon` (number): the probability of exploration (vs. optimization) in learning mode. Default value 0.5.
