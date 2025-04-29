import argparse
import time

from sb3_contrib import ARS, TQC, TRPO
from stable_baselines3 import A2C, DDPG, DQN, PPO, SAC, TD3
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.logger import configure
from stable_baselines3.common.vec_env import VecVideoRecorder

from make_env import make_env

parser = argparse.ArgumentParser()
parser.add_argument("--mode", default="render", type=str)
parser.add_argument("--env", type=str)
parser.add_argument("--algo", type=str)
parser.add_argument("--model_name", type=str)
# parser.add_argument("--model_path", type=str)
# parser.add_argument("--video", default=False, type=bool)
parser.add_argument("--run", default=0, type=int)
args = parser.parse_args()


match args.mode:
    case "render":
        RENDER_MODE = "human"
    case "info":
        RENDER_MODE = "rgb_array"
    case "eval":
        RENDER_MODE = "rgb_array"
    case "video":
        RENDER_MODE = "rgb_array"
    case _:
        raise ValueError(f"unsupported mode: {args.mode}")


eval_env = make_env(args.env, render_mode=RENDER_MODE)
# gymnasium.make(f"{args.env}", render_mode=RENDER_MODE)


# make model
model_path = f"./models/{args.env}-{args.algo}-{args.model_name}/run_{args.run}/best_model"
match args.algo:
    case "SAC":
        model = SAC.load(path=model_path, env=eval_env, device="cpu")
    case "HER-SAC":
        model = SAC.load(path=model_path, env=eval_env, device="cpu")
    case "TD3":
        model = TD3.load(path=model_path, env=eval_env, device="cpu")
    case "DDPG":
        model = DDPG.load(path=model_path, env=eval_env, device="cpu")
    case "DQN":
        model = DQN.load(path=model_path, env=eval_env, device="cpu")
    case "PPO":
        model = PPO.load(path=model_path, env=eval_env, device="cpu")
    case "A2C":
        model = A2C.load(path=model_path, env=eval_env, device="cpu")
    case _:
        raise ValueError(f"Unsupported algorithm: {args.algo}")


#
# RECORD VIDEO
#
if args.mode == "video":
    video_folder = "videos/"
    video_length = 1000
    VIDEO_NAME = f"{args.env}_{args.algo}_run_{args.run}"
    vec_env = VecVideoRecorder(
        model.get_env(),
        video_folder,
        record_video_trigger=lambda x: x == 0,
        video_length=video_length,
        name_prefix=f"{VIDEO_NAME}",
    )
    obs = vec_env.reset()
    for _ in range(video_length + 1):
        action, _state = model.predict(obs, deterministic=True)
        obs, _, _, _ = vec_env.step(action)
    # Save the video
    vec_env.close()


#
# Evaluate Policy
if args.mode == "eval":
    avg_return, std_return = evaluate_policy(model, eval_env, n_eval_episodes=1000)
    print(f"the average return is {avg_return}")


#
# Render Human
#
STEPS = 10000
if args.mode in ["render", "info"]:
    vec_env = model.get_env()
    obs = vec_env.reset()
    infos = []
    for step in range(STEPS):
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, info = vec_env.step(action)
        # print(action)
        # print(info)
        infos.append(info)
        # if args.mode == "render":
        # time.sleep(0.1)

    # print(f"reward_foward = {sum([info[0]['reward_forward']for info in infos])/STEPS}")
    # print(f"reward_ctrl = {sum([info[0]['reward_ctrl']for info in infos])/STEPS}")
    # print(f"reward_contact = {sum([info[0]['reward_contact']for info in infos])/STEPS}")
    # print(f"reward_survive = {sum([info[0]['reward_survive']for info in infos])/STEPS}")
    vec_env.close()
