"""Upload trained model to Hugging Face Hub."""


from huggingface_sb3 import package_to_hub
from stable_baselines3 import PPO, SAC, TD3
from stable_baselines3.common.env_util import make_vec_env


HF_REPO = "farama-minari"
ALGORITHM = "sac"
PROFICIENCY = "simple"
# PROFICIENCY = "medium"
# PROFICIENCY = "expert"
ENV_LIST = [
    "Reacher",
]
seed = 0

EVAL_ENVS = 1000

if __name__ == "__main__":
    for env_id in ENV_LIST:
        if env_id == "HumandoidStandup":
            eval_env = make_vec_env(
                f"{env_id}-v5",
                n_envs=1,
                env_kwargs={
                    "include_cinert_in_observation": False,
                    "include_cvel_in_observation": False,
                    "include_qfrc_actuator_in_observation": False,
                    "include_cfrc_ext_in_observation": False,
                },
            )
        else:
            eval_env = make_vec_env(f"{env_id}-v5", n_envs=1)

        if ALGORITHM == "sac":
            model = SAC.load(
                f"models/{env_id}-{ALGORITHM.upper()}-{PROFICIENCY}-{seed}/best_model.zip",
            )
        elif ALGORITHM == "td3":
            model = TD3.load(
                f"models/{env_id}-{ALGORITHM.upper()}-{PROFICIENCY}-{seed}/best_model.zip",
            )
        elif ALGORITHM == "ppo":
            model = PPO.load(
                f"models/{env_id}-{ALGORITHM.upper()}-{PROFICIENCY}-{seed}/best_model.zip",
            )

        package_to_hub(
            model=model,
            model_name=f"{env_id.lower()}-v5-{ALGORITHM}-{PROFICIENCY}",
            model_architecture=ALGORITHM.upper(),
            env_id=f"{env_id}-v5",
            eval_env=eval_env,
            # repo_id=f"{HF_REPO}/{env_id}-v5-{ALGORITHM.upper()}-{PROFICIENCY}",
            repo_id=f"{HF_REPO}/TEST",
            commit_message="model",
            is_deterministic=True,
            n_eval_episodes=EVAL_ENVS,
        )

    print("FINISHED UPLOADING TO HF")
