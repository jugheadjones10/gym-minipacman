# Gym MiniPacman

A minimal version (19x15 pixels) of Pacman implemented as a Gymnasium environment. The smaller size makes it easier to learn compared to the full-size Atari Pacman environments.

A Gymnasium port of the original MiniPacman environment from [mltrain-nips-2017](https://github.com/vasiloglou/mltrain-nips-2017/blob/master/sebastien_racaniere/I2A%20-%20NIPS%20workshop.ipynb) was written [here](https://github.com/FlorianKlemt/gym-minipacman), but it has become outdated with new versions of Gymnasium. This repository adds slight modifications to make it compatible with the latest version of Gymnasium.

## Installation

```bash
git clone https://github.com/yourusername/gym-minipacman.git
cd gym-minipacman
pip install -e .
```

## Quick Start

```python
import gymnasium as gym
import gym_minipacman

env = gym.make("RegularMiniPacmanNoFrameskip-v0", render_mode="human")
env.reset()

for _ in range(1000):
    # Make random action (0-4)
    action = env.action_space.sample()

    # Take step in environment
    observation, reward, terminated, truncated, info = env.step(action)

    # Check if episode is done
    if terminated or truncated:
        print("Episode finished")
        env.reset()

env.close()
```

## Environment Details

- **Observation Space**: RGB image (19x15x3)
- **Action Space**: Discrete(5) - [NOOP, RIGHT, UP, LEFT, DOWN]
- **Render Modes**: "human" (window display) or "rgb_array" (numpy array)

## Available Environments

The package includes 5 different Pacman environments, each with unique rewards and objectives:

1. `RegularMiniPacmanNoFrameskip-v0`: Standard Pacman gameplay
2. `AvoidMiniPacmanNoFrameskip-v0`: Focus on avoiding ghosts
3. `HuntMiniPacmanNoFrameskip-v0`: Focus on hunting ghosts
4. `AmbushMiniPacmanNoFrameskip-v0`: Focus on strategic ghost hunting
5. `RushMiniPacmanNoFrameskip-v0`: Focus on collecting power pills

## Environment Configurations

| Environment        | Regular | Avoid | Hunt | Ambush | Rush |
| ------------------ | ------- | ----- | ---- | ------ | ---- |
| Step Reward        | 0       | 0.1   | 0    | 0      | 0    |
| Food Reward        | 1       | -0.1  | 0    | -0.1   | -0.1 |
| Power Pill Reward  | 2       | -5    | 1    | 0      | 10   |
| Kill Ghost Reward  | 5       | -10   | 10   | 10     | 0    |
| Death Reward       | 0       | -20   | -20  | -20    | 0    |
| Complete on Pills  | No      | No    | No   | No     | Yes  |
| Complete on Ghosts | No      | No    | Yes  | Yes    | No   |
| Complete on Food   | Yes     | Yes   | No   | No     | No   |
| Time Limit         | ∞       | 128   | 80   | 80     | ∞    |
