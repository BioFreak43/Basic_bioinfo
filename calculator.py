from proteins import molWeight
aaSeq = input('Enter Amino Acid seq: ')
weight = 0
for aa in aaSeq:
    weight = weight + molWeight.prot_weight.get(aa.upper(), 0)
weight = weight - (18 * (len(aaSeq) - 1))
print ("The net weight of the protein is:  ", weight)