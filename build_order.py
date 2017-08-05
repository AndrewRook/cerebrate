
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
    

def generate_random_build_order(stuff_to_build):
    """
    takes in a list of the existing build order, a dictionary of available prerequisites/consumables, and a list of stuff remaining to build.
    1. Pick a random index in the stuff remaining list.
    2. Check the dictionary of prerequisites to see if all prerequisites/consumables exist.
    3a. If the answer to 2. is "yes", then append the item in the remaining list to the existing order and remove it from the list of remaining stuff. If it required any consumables, remove them from the prerequisite dictionary.
    3b. If the answer to 2. is "no", then do the following:
      i. choose a random unmet prerequisite/consumable.
      ii. go to 2.
      iii. whenever you find a prereq/consumable you CAN build, after you add it to the build order find it in the "stuff remaining" list and delete it.
    4. When the stuff remaining list has nothing left in it, you're done.
    """
    """
    existing_stuff = NEW ARGUMENT
    build_order = []
    count = 0
    while len(stuff_to_build) > 0 and count < 1000:
        index = np.random.randint(0, len(stuff_to_build))
        item_to_build = stuff_to_build[index]
        prerequisites_consumables = item_to_build.prerequisites + item_to_build.consumed
        if prequisites_consumables in existing_stuff:
            existing_stuff.append(item_to_build)
            if len(item_to_build.consumed) > 0:
                del existing_stuff[indices_consumed]
            build_order.append(item_to_build)
            del stuff_to_build[index]
        else:
            while True:
                index = np.random.randint(0, len(prerequisites_consumables))
                item_to_build = prerequisites_consumables[index]
                prerequisites_consumables = item_to_build.prerequisites + item_to_build.consumed
                if prerequisites_consumables in existing_stuff:
                    existing_stuff.append(item_to_build)
                    if len(item_to_build.consumed) > 0:
                        del existing_stuff[indices_consumed]
                    build_order.append(item_to_build)
                    del stuff_to_build[prerequisite_index]
                    break
                count += 1
                if count > 100:
                    raise RuntimeError("not converging")
            
    """
    pass

# def compute_build_time(build_order):
#     pass

# def create_new_generation(old_generation, old_generation_build_times,
#                           stuff_to_build, mutation_rate):
#     pass
