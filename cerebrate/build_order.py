from collections import defaultdict
import random

def validate_build_order(existing_items, build_order):
    existing_items = existing_items.copy()
    available_population = sum([existing_items[item] * (item().population_generated - item().population_used)
                                for item in existing_items])
    for item in build_order:
        item_instance = item()
        if available_population < item_instance.population_required and item_instance.population_required > 0:
            return False
        for prereq in item_instance.prerequisite_items:
            if prereq not in existing_items:
                return False
        for consumable in item_instance.items_consumed:
            if existing_items[consumable] <= 0:
                return False
            existing_items[consumable] -= 1
            available_population += consumable().population_used
        available_population += item_instance.population_generated
        available_population -= item_instance.population_used
        existing_items[item] += 1
    return True

def make_random_build_order(existing_stuff_dict, required_stuff_dict, builder_unit, population_item):
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
                                                          builder_unit, population_item)
        build_order.append(next_build_item)
        internal_existing_stuff_dict[next_build_item] += 1
        internal_required_stuff_dict[next_build_item] -= 1
        #If the item being built finishes out a requirement
        #or wasn't in the original requirements (i.e. an implicit prerequisite), delete it:
        if internal_required_stuff_dict[next_build_item] <= 0:
            del internal_required_stuff_dict[next_build_item]
        for item in next_build_item().items_consumed:
            internal_existing_stuff_dict[item] -= 1

    return build_order

def randomly_choose_next_build_item(existing_stuff_dict, required_stuff_dict, builder_unit, population_item):
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
        #Now check population:
        if chosen_instance.population_required > 0:
            available_population = sum([existing_stuff_dict[item] * (item().population_generated - item().population_used)
                                      for item in existing_stuff_dict])
            if chosen_instance.population_required <= available_population:
                return chosen_class
            else:
                return population_item
        else:
            return chosen_class
    else:
        return randomly_choose_next_build_item(existing_stuff_dict, missing_requirements, builder_unit, population_item)
