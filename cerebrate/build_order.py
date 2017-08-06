from collections import defaultdict
import random

def make_random_build_order(existing_stuff_dict, required_stuff_dict, builder_unit):
    #TODO (AndrewRook): Figure out how to factor in population
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
    try:
        chosen_class = random.choice([key for key in required_stuff_dict if required_stuff_dict[key] > 0])
    except IndexError:
        return None
    chosen_instance = chosen_class()
    requirements = defaultdict(int, {})
    for consumed_item in chosen_instance.items_consumed:
        requirements[consumed_item] += 1
    for prerequisite in chosen_instance.prerequisite_items:
        if prerequisite not in requirements:
            requirements[prerequisite] = 1
    if chosen_instance.item_type == "building" and builder_unit not in requirements:
        requirements[builder_unit] = 1
    missing_requirements = defaultdict(int)
    for requirement in requirements:
        if existing_stuff_dict[requirement] < requirements[requirement]:
            missing_requirements[requirement] = requirements[requirement]
    if len(missing_requirements) == 0:
        return chosen_class
    else:
        return randomly_choose_next_build_item(existing_stuff_dict, missing_requirements, builder_unit)
