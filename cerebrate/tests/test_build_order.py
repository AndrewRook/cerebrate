from collections import defaultdict

import pytest

import cerebrate.build_order as bo
import cerebrate.protoss as pt

class TestRandomlyChooseNextBuildItem(object):
    def test_prereqs_met(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.cybernetics_core: 1})
        required = defaultdict(int, {pt.dragoon: 4})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder)
        assert choice is pt.dragoon
    def test_prereqs_not_met(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.probe: 1})
        required = defaultdict(int, {pt.dragoon: 4})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder)
        assert choice is pt.cybernetics_core
    def test_prereqs_really_not_met(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.probe: 1})
        required = defaultdict(int, {pt.scout: 4})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder)
        assert choice is pt.gateway
    def test_consume_met(self):
        existing = defaultdict(int, {pt.high_templar: 3})
        required = defaultdict(int, {pt.archon: 1})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder)
        assert choice is pt.archon
    def test_consume_partially_met(self):
        existing = defaultdict(int, {pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.citadel_of_adun: 1,
                                     pt.templar_archives: 1,
                                     pt.high_templar: 1})
        required = defaultdict(int, {pt.archon: 1})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder)
        assert choice is pt.high_templar
    def test_consume_not_met(self):
        existing = defaultdict(int, {pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.citadel_of_adun: 1,
                                     pt.templar_archives: 1})
        required = defaultdict(int, {pt.archon: 1})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder)
        assert choice is pt.high_templar
    def test_existing_prereq_set_to_zero(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.cybernetics_core: 0,
                                     pt.probe: 1})
        required = defaultdict(int, {pt.dragoon: 4})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder)
        assert choice is pt.cybernetics_core
    def test_required_prereq_set_to_zero(self):
        existing = defaultdict(int, {pt.nexus: 1,
                                     pt.pylon: 1,
                                     pt.gateway: 1,
                                     pt.cybernetics_core: 1})
        required = defaultdict(int, {pt.dragoon: 0})
        choice = bo.randomly_choose_next_build_item(existing, required, pt.builder)
        assert choice is None
    
    
    
