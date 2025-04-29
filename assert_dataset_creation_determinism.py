import minari


def assert_dataset_equality(dataset_a: minari.dataset, dataset_b: minari.dataset, include_infos=False, include_metadata=True):
    """Checks if the environments `dataset_a` & `dataset_b` are identical.
    Usefull to check if the dataset creation is deterministic.

    Args:
        dataset_a: First dataset to check.
        dataset_b: Second dataset to check.
        include_infos: If `False` it does not check for equivalence of the `info`s.
        include_metadate: If `False` it does not check for equivalence of the `metadata`s. (not implemented)
    """
    assert (
        dataset_a.total_episodes == dataset_b.total_episodes
    ), f"Total episodes differ: {dataset_a.total_episodes} != {dataset_b.total_episodes}"
    assert (
        dataset_a.total_steps == dataset_b.total_steps
    ), f"Total steps differ: {dataset_a.total_steps} != {dataset_b.total_steps}"
    if include_metadata:
        assert dataset_a.env_spec == dataset_b.env_spec, f"Env specs differ: {dataset_a.env_spec} != {dataset_b.env_spec}"
        assert (
            dataset_a.minari_version == dataset_b.minari_version
        ), f"Minari versions differ: {dataset_a.minari_version} != {dataset_b.minari_version}"
        assert (
            dataset_a.action_space == dataset_b.action_space
        ), f"Action spaces differ: {dataset_a.action_space} != {dataset_b.action_space}"
        assert (
            dataset_a.observation_space == dataset_b.observation_space
        ), f"Observation spaces differ: {dataset_a.observation_space} != {dataset_b.observation_space}"
        # Dataset IDs are not guaranteed to be the same
        # Dataset spec is not guaranteed to be the same
        # namaspaces are not guaranteed to be the same
        # dataset names are not guaranteed to be the same
        # dataset versions are not guaranteed to be the same

    for episode_a, episode_b in zip(dataset_a.iterate_episodes(), dataset_b.iterate_episodes()):
        assert episode_a.id == episode_b.id
        assert len(episode_a) == len(episode_b), f"Episode lengths differ: {len(episode_a)} != {len(episode_b)}"

        for step in range(len(episode_a)):
            assert (episode_a.actions[step] == episode_b.actions[step]).all()
            assert (episode_a.observations[step] == episode_b.observations[step]).all()
            assert episode_a.rewards[step] == episode_b.rewards[step]
            assert episode_a.terminations[step] == episode_b.terminations[step]
            assert episode_a.truncations[step] == episode_b.truncations[step]
            assert not include_infos or episode_a.infos[step] == episode_b.infos[step]


dataset_a = minari.load_dataset("mujoco/halfcheetah/expert-v0")
dataset_b = minari.load_dataset("mujoco/halfcheetah/expert-v1")

assert_dataset_equality(dataset_a, dataset_b)
