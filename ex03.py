#!/usr/bin/env python3

# encoding: utf8
# author: Anam Ahsan

#Open file with given filepath
my_file = open("/export/home/aahsan4/e_coli_k12_dh10b.faa")

#Create empty dictionary 
residues = {}

#Read open file by line, check whether it is protein line
for entry in my_file:
    if entry.startswith('>'):
        continue
    #For each protein line, residues and counts stored in dictionary 
    else: 
        #Check each residue against amino acid list
        for base in ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z']:
            #If residue not in dictionary, it is added as key with count as value
            if base not in residues:
                count = entry.count(base)
                residues[base] = count 
            #If residue already in dictionary, only count added to value 
            else:                
                count = entry.count(base)
                residues[base] += count
     
#Calculate total number of residues in file
total = float(sum(residues.values())) 

#Sort and print top five most frequently used amino acids and percentage use    
for base, count in sorted(residues.items(), key=lambda b: b[1], reverse=True)[0:5]:
        print("{0}:{1}, ({2:.1%})".format(base,count, count / total))
#Close file
my_file.close()





