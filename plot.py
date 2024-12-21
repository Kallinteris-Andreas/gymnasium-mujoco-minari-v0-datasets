import numpy as np
import matplotlib.pyplot as plt
import argparse
from matplotlib.ticker import EngFormatter

parser = argparse.ArgumentParser()
parser.add_argument("--runs", default=1, type=int)  # Number of statistical runs
parser.add_argument("--name", type=str)
parser.add_argument("--result_directory", nargs='+', type=str)
parser.add_argument("--mode", type=str, default="return")
args = parser.parse_args()

steps = np.load(f'models/{args.result_directory[0]}/run_0/evaluations.npz')['timesteps']

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

for algorithm in args.result_directory:
    returns = np.average(np.array([np.load(f'models/{algorithm}/run_{run}/evaluations.npz')['results'][:steps.size] for run in range(args.runs)]), axis=2)
    returns_len = np.average(np.array([np.load(f'models/{algorithm}/run_{run}/evaluations.npz')['ep_lengths'][:steps.size] for run in range(args.runs)]), axis=2)

    #if 'ahr' in algorithm:
        #options = "--"
    #else:
        #options = "-"
    options = ""
    ax.set_xlim(left=0, right=steps[-1])
    ax.xaxis.set_major_formatter(EngFormatter())
    ax.xaxis.set_major_locator(plt.MaxNLocator(25))
    for x in ax.get_xticks():
        ax.axvline(x=x, color='gray', linestyle='--', linewidth=0.5)

    if args.mode == "return":
        ax.plot(steps, np.average(returns, axis=0), options, linewidth=1, label=f'{algorithm}')
        ax.fill_between(steps, np.min(returns, axis=0), np.max(returns, axis=0), alpha=0.2)
    elif args.mode == "lenght":
        ax.plot(steps, np.average(returns_len, axis=0), options, linewidth=1, label=f'{algorithm}')
        ax.fill_between(steps, np.min(returns_len, axis=0), np.max(returns_len, axis=0), alpha=0.2)

    if args.mode == "return":
        print(f"{algorithm} --- max return: {returns.max()}, --- on run: {returns.max(axis=1).argmax()}")


if args.mode == "return":
    ax.set_title(f'SB3 on Gymnasium/MuJoCo/{args.name}, for {args.runs} Runs, episodic return')
    ax.set_ylabel("Episode Return")
elif args.mode == "lenght":
    ax.set_title(f'SB3 on Gymnasium/MuJoCo/{args.name}, for {args.runs} Runs, episodic lenght')
    ax.set_ylabel("Episode Steps")

ax.legend(loc="upper left")

fig.set_figwidth(16)
fig.set_figheight(9)

for file_extenion in ["png", "pdf"]:
    fig.savefig(f"figures/{args.name}_{args.mode}.{file_extenion}", bbox_inches="tight")
