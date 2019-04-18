#Percentage of nucleotide/nucleotides present in the Gene sequence
nuclSeq = input('Enter nucleotide sequence: ').upper()
count = 0
percent = (input('What to find the percentage in the sequence: ')).upper()
for i in percent:
    for n in nuclSeq:
        if n == i:
            count += 1
        elif n != 'A' and n!='G' and n!='T' and n!='C':
            print('The entered sequence has {0}, which is not acceptable'.format(n))
            exit()
count = count * 100 / len(nuclSeq)
print ('The total GC is {0}%'.format(int(count)))