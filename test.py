from MapleEquip import EquipTemplateMatcher
import pprint

pp = pprint.PrettyPrinter(indent=2)
etm = EquipTemplateMatcher()

#default setting values:
etm.verbose = True
etm.outputFiles = True
etm.outputType = 2 #0 = greyscale; 1 = threshold; 2 = template matched

etm.run()

#Print item stats and totals
pp.pprint(etm.itemsLines)
print("TOTALS:")
for l in etm.totalStats:
    print("{}: {} ({} + {} + {})".format(l["stat"], l["total"], l["base"], l["bonus1"], l["bonus2"]))
