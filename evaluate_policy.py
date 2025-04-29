import argparse

import gymnasium as gym
from huggingface_sb3 import load_from_hub
from stable_baselines3 import SAC
from stable_baselines3.common.evaluation import evaluate_policy

from make_env import make_env

ENV_ID = "Walker2d"
ALGORITHM = "SAC"
PROFICIENCY = "medium"
EVAL_EPISODES = 1000

eval_env = gym.make(f"{ENV_ID}-v5")
# eval_env = gym.make(f"{ENV_ID}-v5", include_cfrc_ext_in_observation=False)

match ALGORITHM:
    case "SAC":
        # model_checkpoint = load_from_hub(
        # repo_id=f"farama-minari/{ENV_ID}-v5-{ALGORITHM.upper()}-{PROFICIENCY}",
        # filename=f"{ENV_ID.lower()}-v5-{ALGORITHM.lower()}-{PROFICIENCY}.zip",
        # )
        # model = SAC.load(model_checkpoint)
        model = SAC.load(f"./models/{ENV_ID}-{ALGORITHM}-{PROFICIENCY}/run_0/best_model.zip")
    case "TD3":
        None
    case "PPO":
        None
print("MODEL LOADED")


mean_reward, std_reward = evaluate_policy(
    model, eval_env, render=False, n_eval_episodes=EVAL_EPISODES, deterministic=True, warn=False
)
print(f"{ENV_ID}-v5/{PROFICIENCY}/{ALGORITHM}")
print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")
