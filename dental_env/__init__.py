from gymnasium.envs.registration import register

register(
     id="dental_env/DentalEnv2D-v0",
     entry_point="dental_env.envs:DentalEnv2D",
     max_episode_steps=300,
)
