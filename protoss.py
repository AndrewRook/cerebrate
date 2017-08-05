from item import create_item

fps = 15 #~normal, see http://www.starcraftai.com/wiki/Frame_Rate

#Buildings
nexus = create_item("nexus", 400, 0, 120, 0, [], "building", population_generated=9)
pylon = create_item("pylon", 100, 0, 30, 0, [], "building", population_generated=8)
assimilator = create_item("assimilator", 100, 0, 40, 0, [], "building")
gateway = create_item("gateway", 150, 0, 60, 0, [nexus, pylon], "building")
forge = create_item("forge", 150, 0, 40, 0, [nexus, pylon], "building")
photon_cannon = create_item("photon_cannon", 150, 0, 50, 0, [forge, pylon], "building")
shield_battery = create_item("shield_battery", 100, 0, 30, 0, [gateway, pylon], "building")
cybernetics_core = create_item("cybernetics_core", 200, 0, 60, 0, [gateway, pylon], "building")
robotics_facility = create_item("robotics_facility", 200, 200, 80, 0, [cybernetics_core, pylon], "building")
robotics_support_bay = create_item("robotics_support_bay", 150, 100, 30, 0, [robotics_facility, pylon], "building")
observatory = create_item("observatory", 50, 100, 30, 0, [robotics_facility, pylon], "building")
citadel_of_adun = create_item("citadel_of_adun", 150, 100, 60, 0, [cybernetics_core, pylon], "building")
templar_archives = create_item("templar_archives", 150, 200, 60, 0, [citadel_of_adun, pylon], "building")
stargate = create_item("stargate", 150, 150, 70, 0, [cybernetics_core, pylon], "building")
fleet_beacon = create_item("fleet_beacon", 300, 200, 60, 0, [stargate, pylon], "building")
arbiter_tribunal = create_item("arbiter_tribunal", 200, 150, 60, 0, [stargate, templar_archives, pylon], "building")
 

#Designating special buildings:
population_generator = pylon
vespene_generator = assimilator

#Units

#production rates from Churchill & Buro 2011
#(http://ai.cs.unibas.ch/research/reading_group/churchill-buro-aiide2011.pdf)
probe = create_item("probe", 50, 0, 20, 1, [nexus], "unit",
                    mineral_production_rate=0.045 * fps,
                    gas_production_rate=0.07 * fps)
zealot = create_item("zealot", 100, 0, 40, 1, [gateway, pylon], "unit")
dragoon = create_item("dragoon", 125, 50, 50, 2, [gateway, cybernetics_core, pylon], "unit")
high_templar = create_item("high_templar", 50, 150, 50, 2, [gateway, templar_archives, pylon], "unit")
dark_templar = create_item("dark_templar", 125, 100, 50, 2, [gateway, templar_archives, pylon], "unit")
reaver = create_item("reaver", 200, 100, 70, 4, [robotics_facility, robotics_support_bay, pylon], "unit")
observer = create_item("observer", 25, 75, 40, 1, [robotics_facility, observatory, pylon], "unit")
shuttle = create_item("shuttle", 200, 0, 60, 2, [robotics_facility, pylon], "unit")
scout = create_item("scout", 275, 125, 80, 3, [stargate, pylon], "unit")
carrier = create_item("carrier", 350, 250, 140, 6, [stargate, fleet_beacon, pylon], "unit")
arbiter = create_item("arbiter", 100, 350, 160, 4, [stargate, arbiter_tribunal, pylon], "unit")
corsair = create_item("corsair", 150, 100, 40, 2, [stargate, pylon], "unit")
#archon = create_item(0, 0, 20, 4, [
#dark_archon

#Designating special units:
builder = probe
