import gymnasium as gym

import gym_minipacman  # noqa

env = gym.make("RegularMiniPacmanNoFrameskip-v0", render_mode="human")
env.reset()

# Run for 1000 steps or until game is done
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
