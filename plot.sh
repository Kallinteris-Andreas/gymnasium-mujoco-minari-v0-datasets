
for mode in "return" "lenght"; do
	python plot.py --name Pusher --mode $mode --result_directory Pusher-SAC-expert Pusher-TD3-expert Pusher-TQC-expert
	python plot.py --name Reacher --mode $mode --result_directory Reacher-SAC-expert Reacher-TD3-expert Reacher-TQC-expert
	python plot.py --name Hopper --mode $mode --result_directory Hopper-SAC-expert Hopper-PPO-expert Hopper-TD3-expert Hopper-TQC-expert Hopper-TRPO-expert
	python plot.py --name Walker2d --mode $mode --result_directory Walker2d-SAC-expert Walker2d-TD3-expert Walker2d-TQC-expert Walker2d-TRPO-expert
	python plot.py --name HalfCheetah --mode $mode --result_directory HalfCheetah-SAC-expert HalfCheetah-TD3-expert HalfCheetah-TQC-expert
	python plot.py --name HalfCheetah --mode $mode --result_directory HalfCheetah-TQC-simple
	python plot.py --name Ant --mode $mode --result_directory Ant-SAC-medium Ant-TD3-medium
	python plot.py --name Swimmer --mode $mode --result_directory Swimmer-SAC-expert Swimmer-TQC-expert Swimmer-PPO-expert Swimmer-ARS-expert
	python plot.py --name Humanoid --mode $mode --result_directory Humanoid-SAC-expert Humanoid-TD3-expert Humanoid-TQC-expert
	#python plot.py --name HumanoidStandup --mode $mode --result_directory HumanoidStandup-TD3-expert HumanoidStandup-SAC-expert
	python plot.py --name HumanoidStandup --mode $mode --result_directory HumanoidStandup-SAC-expert
done