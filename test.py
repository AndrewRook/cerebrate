from collections import defaultdict

from cerebrate import protoss

from cerebrate.build_order import make_random_build_order

if __name__ == "__main__":
    existing_stuff = defaultdict(lambda: 0, {protoss.probe: 0, protoss.nexus: 1})
    required_stuff = defaultdict(lambda: 0, {protoss.probe: 3, protoss.zealot: 2, protoss.dragoon: 4})
    #existing_stuff = defaultdict(lambda: 0, {protoss.nexus: 1})
    #required_stuff = defaultdict(lambda: 0, {protoss.probe: 3})
    build_order = make_random_build_order(existing_stuff, required_stuff, protoss.builder)
    print([item().name for item in build_order])
    
