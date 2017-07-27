from item import create_item

fps = 24 #~fastest, see http://www.starcraftai.com/wiki/Frame_Rate

#Buildings
nexus = create_item(400, 0, 120, 0, [], population_generated=9)
pylon = create_item(100, 0, 30, 0, [], population_generated=8)
assimilator = create_item(100, 0, 40, 0, [])
gateway = create_item(150, 0, 0, [pylon])

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
