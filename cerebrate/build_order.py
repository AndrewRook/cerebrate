import random

def make_random_build_order(existing_stuff_dict, required_stuff_dict, builder_unit):
    internal_existing_stuff_dict = existing_stuff_dict.copy()
    internal_required_stuff_dict = required_stuff_dict.copy()

    #Pruning anything that was input as zero in the requirements defaultdict: 
    for key in internal_required_stuff_dict:
        if internal_required_stuff_dict[key] <= 0:
            del internal_required_stuff_dict[key]
    
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
        if existing_stuff_dict[prerequisite] <= 0:
            missing_prerequisites[prerequisite] += 1
    if len(missing_prerequisites) == 0:
        return chosen_class
    else:
        return randomly_choose_next_build_item(existing_stuff_dict, missing_prerequisites, builder_unit)


if __name__ == "__main__":
    from collections import defaultdict
    import protoss
    existing_stuff = defaultdict(lambda: 0, {protoss.probe: 0, protoss.nexus: 1})
    required_stuff = defaultdict(lambda: 0, {protoss.probe: 3, protoss.zealot: 2, protoss.dragoon: 4})
    #existing_stuff = defaultdict(lambda: 0, {protoss.nexus: 1})
    #required_stuff = defaultdict(lambda: 0, {protoss.probe: 3})
    build_order = make_random_build_order(existing_stuff, required_stuff, protoss.builder)
    print([item().name for item in build_order])
