from item import create_item

fps = 15 #~normal, see http://www.starcraftai.com/wiki/Frame_Rate

#Buildings
nexus = create_item(400, 0, 120, 0, [], population_generated=9)
pylon = create_item(100, 0, 30, 0, [], population_generated=8)
assimilator = create_item(100, 0, 40, 0, [])
gateway = create_item(150, 0, 60, 0, [nexus, pylon])
forge = create_item(150, 0, 40, 0, [nexus, pylon])
photon_cannon = create_item(150, 0, 50, 0, [forge, pylon])
shield_battery = create_item(100, 0, 30, 0, [gateway, pylon])
cybernetics_core = create_item(200, 0, 60, 0, [gateway, pylon])
robotics_facility = create_item(200, 200, 80, 0, [cybernetics_core, pylon])
robotics_support_bay = create_item(150, 100, 30, 0, [robotics_facility, pylon])
observatory = create_item(50, 100, 30, 0, [robotics_facility, pylon])
citadel_of_adun = create_item(150, 100, 60, 0, [cybernetics_core, pylon])
templar_archives = create_item(150, 200, 60, 0, [citadel_of_adun, pylon])
stargate = create_item(150, 150, 70, 0, [cybernetics_core, pylon])
fleet_beacon = create_item(300, 200, 60, 0, [stargate, pylon])
arbiter_tribunal = create_item(200, 150, 60, 0, [stargate, templar_archives, pylon])
 

#Designating special buildings:
population_generator = pylon
vespene_generator = assimilator

#Units

#production rates from Churchill & Buro 2011
#(http://ai.cs.unibas.ch/research/reading_group/churchill-buro-aiide2011.pdf)
probe = create_item(50, 0, 20, 1, [nexus],
                    mineral_production_rate=0.045 * fps,
                    gas_production_rate=0.07 * fps)
zealot = create_item(100, 0, 40, 1, [gateway])
dragoon = create_item(125, 50, 50, 2, [gateway, cybernetics_core])
high_templar = create_item(50, 150, 50, 2, [gateway, templar_archives])
dark_templar = create_item(125, 100, 50, 2, [gateway, templar_archives])
reaver = create_item(200, 100, 70, 4, [robotics_facility, robotics_support_bay])
observer
shuttle
scout
carrier
arbiter
corsair
archon
dark_archon
