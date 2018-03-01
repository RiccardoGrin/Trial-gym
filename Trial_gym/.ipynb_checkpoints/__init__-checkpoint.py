from gym.envs.registration import register

register(
    id='trial_gym-v0',
    entry_point='Trial_gym.envs:FrozenLakeEnv',
)
