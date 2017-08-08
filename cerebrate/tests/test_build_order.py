import random

from collections import defaultdict

import pytest

import cerebrate.build_order as bo
import cerebrate.protoss as pt

class TestValidateBuildOrder(object):
    def test_prereqs_met_no_consumables(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.probe: 1})
        order = [pt.zealot, pt.zealot, pt.cybernetics_core]
        assert bo.validate_build_order(existing, order) is True

    def test_prereqs_not_met_no_consumables(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.probe: 1})
        order = [pt.zealot, pt.dragoon, pt.cybernetics_core]
        assert bo.validate_build_order(existing, order) is False

    def test_no_prereqs_consumables_met(self):
        existing = defaultdict(int, {pt.high_templar: 6})
        order = [pt.archon, pt.archon, pt.archon]
        assert bo.validate_build_order(existing, order) is True

    def test_no_prereqs_consumables_not_met(self):
        existing = defaultdict(int, {pt.high_templar: 5})
        order = [pt.archon, pt.archon, pt.archon]
        assert bo.validate_build_order(existing, order) is False

    def test_prereqs_met_consumables_met(self):
        existing = defaultdict(int, {pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.cybernetics_core: 1,
                                     pt.probe: 1})
        order = [pt.zealot, pt.zealot, pt.citadel_of_adun, pt.pylon,
                 pt.templar_archives, pt.high_templar, pt.high_templar, pt.archon]
        assert bo.validate_build_order(existing, order) is True
        
    def test_not_enough_population(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.probe: 1})
        order = [pt.zealot, pt.zealot]
        assert bo.validate_build_order(existing, order) is True
        order *= 5
        assert bo.validate_build_order(existing, order) is False
        order = [pt.pylon] * 3 + order
        assert bo.validate_build_order(existing, order) is True


class TestMakeRandomBuildOrder(object):
    # @staticmethod
    # def make_random_items(num_items, possible_items):
    #     items = defaultdict(int)
    #     for i in range(num_items):
    #         random_item = random.choice(possible_items)
    #         items[random_item] += 1
    #     return items
    
    def test_works_no_requirements(self):
        existing = defaultdict(int)
        required = defaultdict(int)
        assert len(bo.make_random_build_order(existing, required, pt.builder, pt.population_generator)) == 0
    def test_works_some_requirements_zero(self):
        existing = defaultdict(int, {pt.probe: 1, pt.pylon: 1})
        required = defaultdict(int, {pt.nexus: 1,
                                     pt.gateway: 2,
                                     pt.zealot: 0})
        assert (bo.make_random_build_order(existing, required, pt.builder, pt.population_generator) ==
                [pt.nexus, pt.gateway, pt.gateway])
    
    from hypothesis import given
    import hypothesis.strategies as st
    @given(st.random_module(),
           st.lists(elements=st.integers(min_value=0, max_value=len(pt.item_list)-1), min_size=0, max_size=60),
           st.lists(elements=st.integers(min_value=0, max_value=len(pt.item_list)-1), min_size=0, max_size=40))
    def test_build_orders_are_valid_protoss(self, seed, existing_indices_list, required_indices_list):
        existing = defaultdict(int)
        for i in existing_indices_list:
            existing[pt.item_list[i]] += 1
        required = defaultdict(int)
        for i in required_indices_list:
            required[pt.item_list[i]] += 1
        print("Existing:\n-----------")
        for key in existing:
            print(key().name, existing[key])
        print("Required:\n-----------")
        for key in required:
            print(key().name, required[key])
        print("\n\n")
        build_order = bo.make_random_build_order(existing, required, pt.builder, pt.population_generator)
        assert bo.validate_build_order(existing, build_order)
    # def test_build_orders_are_valid(self, existing_list, required_list):
    #     existing = defaultdict(int)
    #     for item in existing_list:
    #         existing[item] += 1
    #     required = defaultdict(int)
    #     for item in required_list:
    #         required[item] += 1
    #     build_order = bo.make_random_build_order(existing, required, pt.builder, pt.population_generator)
    #     assert bo.validate_build_order(build_order)

# from hypothesis import given
# import hypothesis.strategies as st
# @given(st.lists(elements=[1, 2, 3], min_size=0, max_size=5))
# def test_woo(test_list):
#     print(test_list)
#     assert len(test_list) > 0

class TestRandomlyChooseNextBuildItem(object):
    def test_prereqs_met(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.cybernetics_core: 1})
        required = defaultdict(int, {pt.dragoon: 4})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder, pt.population_generator)
        assert choice is pt.dragoon
    def test_prereqs_not_met(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.probe: 1})
        required = defaultdict(int, {pt.dragoon: 4})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder, pt.population_generator)
        assert choice is pt.cybernetics_core
    def test_prereqs_really_not_met(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.probe: 1})
        required = defaultdict(int, {pt.scout: 4})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder, pt.population_generator)
        assert choice is pt.gateway
    def test_consume_met(self):
        existing = defaultdict(int, {pt.high_templar: 3})
        required = defaultdict(int, {pt.archon: 1})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder, pt.population_generator)
        assert choice is pt.archon
    def test_consume_partially_met(self):
        existing = defaultdict(int, {pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.citadel_of_adun: 1,
                                     pt.templar_archives: 1,
                                     pt.high_templar: 1})
        required = defaultdict(int, {pt.archon: 1})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder, pt.population_generator)
        assert choice is pt.high_templar
    def test_consume_not_met(self):
        existing = defaultdict(int, {pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.citadel_of_adun: 1,
                                     pt.templar_archives: 1})
        required = defaultdict(int, {pt.archon: 1})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder, pt.population_generator)
        assert choice is pt.high_templar
    def test_need_more_builders(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.gateway: 1})
        required = defaultdict(int, {pt.dragoon: 4})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder, pt.population_generator)
        assert choice is pt.builder
    def test_need_more_population(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.cybernetics_core: 1,
                                     pt.zealot: 30})
        required = defaultdict(int, {pt.dragoon: 4})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder, pt.population_generator)
        assert choice is pt.population_generator
    def test_existing_prereq_set_to_zero(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.cybernetics_core: 0,
                                     pt.probe: 1})
        required = defaultdict(int, {pt.dragoon: 4})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder, pt.population_generator)
        assert choice is pt.cybernetics_core
    def test_required_prereq_set_to_zero(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.cybernetics_core: 1})
        required = defaultdict(int, {pt.dragoon: 0})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder, pt.population_generator)
        assert choice is None
    
    
    
