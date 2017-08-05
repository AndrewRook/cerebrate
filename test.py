import random

from collections import defaultdict

import numpy as np

import protoss

def make_random_build_order(existing_stuff_dict, required_stuff_dict, builder_unit):
    internal_existing_stuff_dict = existing_stuff_dict.copy()
    internal_required_stuff_dict = required_stuff_dict.copy()
    
    build_order = []
    while len(internal_required_stuff_dict) > 0:
        next_build_item = randomly_choose_next_build_item(internal_existing_stuff_dict,
                                                          internal_required_stuff_dict,
                                                          builder_unit)
        build_order.append(next_build_item)
        internal_existing_stuff_dict[next_build_item] += 1
        internal_required_stuff_dict[next_build_item] -= 1
        #If the item being built finishes out a requirement
        #or wasn't in the original requirements (i.e. an implicit prerequisite), delete it:
        if internal_required_stuff_dict[next_build_item] <= 0:
            del internal_required_stuff_dict[next_build_item]
        #TODO (AndrewRook): add code to remove any consumed items

    return build_order

def randomly_choose_next_build_item(existing_stuff_dict, required_stuff_dict, builder_unit):
    chosen_class = random.choice(list(required_stuff_dict))
    chosen_instance = chosen_class()
    prerequisites = chosen_instance.prerequisite_items
    if chosen_instance.item_type == "building" and builder_unit not in prerequisites:
        prerequisites.append(builder_unit)
    #TODO (AndrewRook): Figure out how to include consumed items - need to also bolster loop
    #to count exact number of available units to be consumed
    missing_prerequisites = defaultdict(lambda: 0)
    for prerequisite in prerequisites:
        if prerequisite not in existing_stuff_dict:
            missing_prerequisites[prerequisite] += 1
    if len(missing_prerequisites) == 0:
        return chosen_class
    else:
        return randomly_choose_next_build_item(existing_stuff_dict, missing_prerequisites, builder_unit)
        
    

# def random_build_order(existing_stuff_dict, required_stuff_dict, builder_unit):
#     build_order = []
#     chosen_class = random.choice(list(required_stuff_dict))
#     chosen_instance = chosen_class()
#     prerequisites = chosen_instance.prerequisite_items#Must make instance to set prerequisite_items
#     if chosen_instance.item_type == "building" and builder_unit not in prerequisites:
#         prerequisites.append(builder_unit)
#     #consumables = random.key.items_consumed
#     missing_prerequisites = []
#     for prerequisite in prerequisites:
#         if prerequisite not in existing_stuff_dict:
#             missing_prerequisites.append(prerequisite)
#             print("missing: ", prerequisite().name)
#     if len(missing_prerequisites) == 0:
#         build_order.append(chosen_class)
#         existing_stuff_dict[chosen_class] += 1
#         required_stuff_dict[chosen_class] -= 1
#         if required_stuff_dict[chosen_class] <= 0:
#             del required_stuff_dict[chosen_class]
#         if len(required_stuff_dict) > 0:
#             #Potential problems with mutable structures here:
#             build_order += random_build_order(existing_stuff_dict, required_stuff_dict, builder_unit)
#     #print(chosen_instance.name)
#     #print(required_stuff_dict[chosen_class])
#     return build_order

if __name__ == "__main__":
    existing_stuff = defaultdict(lambda: 0, {protoss.probe: 4, protoss.nexus: 1})
    required_stuff = defaultdict(lambda: 0, {protoss.zealot: 2, protoss.dragoon: 4})
    #existing_stuff = defaultdict(lambda: 0, {protoss.nexus: 1})
    #required_stuff = defaultdict(lambda: 0, {protoss.probe: 3})
    build_order = make_random_build_order(existing_stuff, required_stuff, protoss.builder)
    print([item().name for item in build_order])
    # for item in build_order:
    #     print(item().name)
    
