INFO_KEYS = {
    "HalfCheetah": {
        "x_position",
        "x_velocity",
        "reward_forward",
        "reward_ctrl",
    },
    "Hopper": {
        "x_position",
        "x_velocity",
        "z_distance_from_origin",
        "reward_forward",
        "reward_ctrl",
        "reward_survive",
    },
    "Ant": {
        "x_position",
        "y_position",
        "distance_from_origin",
        "x_velocity",
        "y_velocity",
        "reward_forward",
        "reward_ctrl",
        "reward_survive",
        "reward_contact",
    },
    "Walker2d": {
        "x_position",
        "x_velocity",
        "z_distance_from_origin",
        "reward_forward",
        "reward_ctrl",
        "reward_survive",
    },
    "InvertedPendulum": {
        "reward_survive",
    },
    "InvertedDoublePendulum": {
        "reward_survive",
        "distance_penalty",
        "velocity_penalty",
    },
    "Pusher": {
        "reward_dist",
        "reward_ctrl",
        "reward_near",
    },
    "Reacher": {
        "reward_dist",
        "reward_ctrl",
    },
    "Swimmer": {
        "x_position",
        "y_position",
        "distance_from_origin",
        "x_velocity",
        "y_velocity",
        "reward_forward",
        "reward_ctrl",
    },
    "Humanoid": {
        "x_position",
        "y_position",
        "tendon_length",  # Tendons are not kept in info for compatability
        "tendon_velocity",  # Tendons are not kept in info for compatability
        "distance_from_origin",
        "x_velocity",
        "y_velocity",
        "reward_survive",
        "reward_forward",
        "reward_ctrl",
        "reward_contact",
    },
    "HumanoidStandup": {
        "x_position",
        "y_position",
        "z_distance_from_origin",
        "tendon_length",  # Tendons are not kept in info for compatability
        "tendon_velocity",  # Tendons are not kept in info for compatability
        "distance_from_origin",
        "reward_linup",
        "reward_quadctrl",
        "reward_impact",
    },
}
