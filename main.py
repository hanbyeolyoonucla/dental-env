import dental_env
import gymnasium as gym

if __name__ == "__main__":
    env = gym.make('dental_env/DentalEnv2D-v0', size=10, render_mode="human")
    observation, info = env.reset(seed=42)
    print(observation)
    for _ in range(100):
        action = env.action_space.sample()  # this is where you would insert your policy
        observation, reward, terminated, truncated, info = env.step(action)
        print(observation)

        if terminated or truncated:
            observation, info = env.reset()
    env.close()
