
import numpy as np



# def compute_build_order(current_minerals, current_gas,
#                         existing_stuff, in_progress_stuff, required_stuff):
#     paid_for_stuff = combine_stuff(existing_stuff, in_progress_stuff)
#     stuff_to_build = determine_missing_stuff(paid_for_stuff, required_stuff)
#     build_order, build_order_time = optimize_build_order(current_minerals, current_gas,
#                                                          existing_stuff, in_progress_stuff,
#                                                          stuff_to_build)
#     return build_order, build_order_time

# def combine_stuff(*args):
#     """
#     Take multiple groupings of buildings/upgrades/units and combine them
#     into a single grouping.
#     """

# def determine_missing_stuff(paid_for_stuff, required_stuff):
#     explicit_requirements = difference_stuff(paid_for_stuff, required_stuff)
#     prerequisites = determine_prerequisites(required_stuff)
#     implicit_requirements = difference_stuff(explicit_requirements, prerequisites)
#     return combine_stuff(explicit_requirements, implicit_requirements)

# def difference_stuff(group_1, group_2):
#     """
#     compute all items in group_2 that are not in group_1, then return them as
#     a group.
#     """

# def determine_prerequisites(group):
#     """
#     Find the set of all prerequisites required to build the buildings/upgrades/units in
#     the group.
#     """

# def optimize_build_order(current_minerals, current_gas,
#                          existing_stuff, in_progress_stuff, stuff_to_build,
#                          n_generations=50, n_population=100, mutation_rate=0.01):
#     best_build_order = None
#     best_build_order_time = None
#     new_generation = [generate_random_build_order(stuff_to_build) for i in range n_population]
#     new_generation_build_times = [compute_build_time(build_order) for build_order in new_generation]
#     for n in range(n_generations):
#         old_generation = new_generation.copy()
#         old_generation_build_times = old_generation_build_times.copy()
#         new_generation = create_new_generation(old_generation, old_generation_build_times,
#                                                stuff_to_build, mutation_rate)
#         new_generation_build_times = [compute_build_time(build_order) for build_order in new_generation]
#     best_build_order_index = np.argmin(new_generation_build_times)
#     return new_generation[best_build_order_index], new_generation_build_times[best_build_order_index]
    

# def generate_random_build_order(stuff_to_build):
#     pass

# def compute_build_time(build_order):
#     pass

# def create_new_generation(old_generation, old_generation_build_times,
#                           stuff_to_build, mutation_rate):
#     pass
