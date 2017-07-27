
def create_item(mineral_cost, gas_cost, build_time, population_used, prerequisite_items,
                items_consumed=None, population_generated=0, mineral_production_rate=0, gas_production_rate=0):
    class TempClass(object):
        def __init__(self, time_to_ready=0):
            self._mineral_cost = mineral_cost
            self._gas_cost = gas_cost
            self._build_time = build_time
            self._population_used = population_used
            self._prerequisite_items = prerequisite_items
            if items_consumed is not None:
                self._items_consumed = items_consumed
            else:
                self._items_consumed = []
            self._population_generated = population_generated
            self._mineral_production_rate = mineral_production_rate
            self._gas_production_rate = gas_production_rate
            
            self.time_to_ready = time_to_ready

        @property
        def mineral_cost(self):
            return self._mineral_cost
        @property
        def gas_cost(self):
            return self._gas_cost
        @property
        def build_time(self):
            return self._build_time
        @property
        def population_used(self):
            return self._population_used
        @property
        def prerequisite_items(self):
            return self._prerequisite_items
        @property
        def items_consumed(self):
            return self._items_consumed
        @property
        def population_generated(self):
            return self._population_generated
        @property
        def mineral_production_rate(self):
            return self._mineral_production_rate
        @property
        def gas_production_rate(self):
            return self._gas_production_rate
            
    return TempClass

if __name__ == "__main__":
    test = create_item(40, 0, 200, [])
    wooo = test()
    print(wooo.mineral_cost)

