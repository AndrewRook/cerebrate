
def create_item(name, mineral_cost, gas_cost, build_time, population_used, prerequisite_items,
                item_type, items_consumed=None, population_required=None, population_generated=0,
                mineral_production_rate=0, gas_production_rate=0):
    """
    Create a simple class to store information about a unit, building, or upgrade.

    Parameters
    ----------
    name : string
        The prose name of the item.
    mineral_cost : integer
        The mineral cost of the item.
    gas_cost : integer
        The gas cost of the item.
    build_time : number
        How long it takes to build/research the item, in whatever unit is appropriate (frames, seconds, etc).
    population_used : integer
        The number of population used by the item. For buildings and upgrades this is usually 0.
    prerequisite_items : list of Item classes
        The units/buildings/upgrades required in order to be able to produce the unit.
    item_type : string
        The type of item, either "building", "unit", or "upgrade". 
    items_consumed : list of Item classes, or ``None`` (default: ``None``)
        If the unit/building/upgrade requires the sacrifice of one or more units
        or buildings (e.g. Protoss Archons, Zerg buildings) list each of them. (Example:
        For Archons this would be [high_templar, high_templar].)
    population_required : integer or ``None`` (default: ``None``)
        If the required population to construct the unit is different than the population used by the
        created unit, enter it here. (Example: Archons use 4 population, but require zero available population
        to create because the High Templar units already exist.)
    population_generated : integer or 0 (default: 0)
        If the unit/building generates population, how many units of population it generates.
    mineral_production_rate : integer or 0 (default: 0)
        If the unit/building is capable of proucing minerals, how many minerals it produces per time-step (must be in the
        same time units as ``build_time``).
    gas_production_rate : integer or 0 (default: 0)
        Same as ``mineral_production_rate``, but for gas.
    
    """
    class Item(object):
        def __init__(self, time_to_ready=0):
            self._name = name
            self._mineral_cost = mineral_cost
            self._gas_cost = gas_cost
            self._build_time = build_time
            self._population_used = population_used
            self._prerequisite_items = prerequisite_items
            self.item_type = item_type
            if items_consumed is not None:
                self._items_consumed = items_consumed
            else:
                self._items_consumed = []
            if population_required is None:
                self._population_required = population_used
            else:
                self._population_required = population_required
            self._population_generated = population_generated
            self._mineral_production_rate = mineral_production_rate
            self._gas_production_rate = gas_production_rate
            
            self.time_to_ready = time_to_ready

        @property
        def name(self):
            return self._name
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
        def item_type(self):
            return self._item_type
        @item_type.setter
        def item_type(self, value):
            if value.lower() not in ["unit", "building", "upgrade"]:
                raise ValueError("item_type must be one of unit, building, or upgrade")
            self._item_type = value
        @property
        def items_consumed(self):
            return self._items_consumed
        @property
        def population_required(self):
            return self._population_required
        @property
        def population_generated(self):
            return self._population_generated
        @property
        def mineral_production_rate(self):
            return self._mineral_production_rate
        @property
        def gas_production_rate(self):
            return self._gas_production_rate
            
    return Item

if __name__ == "__main__":
    test = create_item(40, 0, 200, [])
    wooo = test()
    print(wooo.mineral_cost)

