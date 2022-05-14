import pytest

from pettingzoo.classic import hanabi_v4

def test_pettingzoo():
    env = hanabi_v4.env()
    env.reset()
    for agent in env.agent_iter():
        observation, reward, done, info = env.last()
        if done:
            return
        else:
            action = env.action_space(agent).sample()
            env.step(action)

