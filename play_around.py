# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:59:09 2019

@author: Asus
"""

        if line[drug_name] in drugs:
            if line[prescriber_id] not in drugs[line[drug_name]][0]:
                drugs[line[drug_name]][0].append(line[prescriber_id])
            drugs[line[drug_name]][1] += int(line[drug_cost])                
        else:
            drugs[line[drug_name]] = [[line[prescriber_id]], line[drug_cost]]
        data.append([line[prescriber_id], line[drug_name], int(line[drug_cost])])
        
        top_cost_
        
        python3 ./src/pharmacy_counting.py ./input/itcont.txt ./output/top_cost_drug.txt
        
        # -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:19:36 2019

@author: Asus
"""
def test_the_variables(test_list):
    
import sys
# filename
input_file = r'C:\Users\Asus\Downloads\trash\de_cc_data.txt'
# reading the rest of the file
drugs = {}
with open(input_file) as file:
    headers = next(file).strip('\n').split(',')
    # variable indices
    prescriber_id = headers.index('id')
    drug_name = headers.index('drug_name')
    drug_cost = headers.index('drug_cost')
    # reading the data
    for line in file:
        line = line.strip('\n').split(',')
        # line = [line[prescriber_id], line[drug_name], line[drug_cost]]
        #prescriber_id = int(line[prescriber_id])
        
        if line[drug_name] in drugs:    
            if line[prescriber_id] not in drugs[line[drug_name]][0]: # isinstance
                drugs[line[drug_name]][0].append(line[prescriber_id])
            try:
                drugs[line[drug_name]][1] += float(line[drug_cost].strip('"'))
            except ValueError:
                drugs[line[drug_name]][1] += float(line[prescriber_id].strip('"'))
      
        else:
            try:
                drugs[line[drug_name]] = [[line[prescriber_id]], float(line[drug_cost].strip('"'))]
            except ValueError:
                drugs[line[drug_name]] = [[line[drug_cost]], float(line[prescriber_id].strip('"'))]

      
output_data = sorted(drugs.items(), key=lambda x: (-x[1][1], x[0]))    
output_file = r'C:\Users\Asus\Downloads\trash\de_cc_data1.txt'
#with open(output_file,"w") as file1:
file1 = open(output_file, "w") #str(sys.argv[2])
output = ["drug_name,num_prescriber,total_cost\n"]
output += [output_line[0] + ',' + str(len(output_line[1][0])) + ',' + 
           str(output_line[1][1]) + '\n' for output_line in output_data]     
file1.writelines(output)
file1.close()

import sys
# filename
input_file = r'C:\Users\Asus\Downloads\trash\de_cc_data.txt'
# reading the rest of the file
drugs = {}
with open(input_file) as file:
    headers = next(file).strip('\n').split(',')
    # variable indices
    prescriber_id_idx = headers.index('id')
    drug_name_idx = -2
    drug_cost_idx = -1
    # reading the data
    for line in file:
        line = line.strip('\n').split(',')
        # line = [line[prescriber_id], line[drug_name], line[drug_cost]]
        #prescriber_id = int(line[prescriber_id])
        drug_name = line[drug_name_idx]
        prescriber_id = line[prescriber_id_idx]
        drug_cost = line[drug_cost_idx]
        if drug_name in drugs:    
            if prescriber_id not in drugs[drug_name][0]: # isinstance
                drugs[drug_name][0].append(prescriber_id)
            try:
                drugs[drug_name][1] += float(drug_cost)
            except ValueError:
                drugs[drug_name][1] += float(drug_name.strip('"'))
      
        else:
            try:
                drugs[drug_name] = [[prescriber_id], float(drug_cost)]
            except ValueError:
                drugs[drug_cost] = [[prescriber_id], float(drug_name.strip('"'))]

      
output_data = sorted(drugs.items(), key=lambda x: (-x[1][1], x[0]))    
output_file = r'C:\Users\Asus\Downloads\trash\de_cc_data1.txt'
#with open(output_file,"w") as file1:
file1 = open(output_file, "w") #str(sys.argv[2])
output = ["drug_name,num_prescriber,total_cost\n"]
output += [output_line[0] + ',' + str(len(output_line[1][0])) + ',' + 
           str(output_line[1][1]) + '\n' for output_line in output_data]     
file1.writelines(output)
file1.close()

import sys
# filename
input_file = r'C:\Users\Asus\Downloads\trash\de_cc_data.txt'
#input_file = r'C:\Users\Asus\Documents\GitHub\pharm_count\input\itcont.txt'
# reading the rest of the file
#drugs = {}
with open(input_file) as file:
    headers = next(file).strip('\n').split(',')
    # variable indices
    prescriber_id_idx = headers.index('id')
    drug_name_idx = -2
    drug_cost_idx = -1
    # 
    doctors, drugs = set(), set()
    for line in file:
        line = line.strip('\n').split(',')
        name = (line[1] + ' ' + line[-3]).split(' ')
        doctors.add(name[1] + ' ' + name[-1])
        drugs.add(line[drug_name_idx])
                
dictionary = {}                
with open(input_file) as file:
    next(file)
    for line in file:
        line = line.strip('\n').split(',')
        sample_drug = line[drug_name_idx]
        name = (line[1] + ' ' + line[-3]).split(' ')
        name = name[1] + ' ' + name[-1]
        if sample_drug in dictionary.keys():
            dictionary[sample_drug][1] += float(line[drug_cost_idx])
            dictionary[sample_drug][0].add(name)
        else:
            dictionary[sample_drug] = [{name}, 
                       float(line[drug_cost_idx])]
                
dictionary = {}
doctors = set()              
with open(input_file) as file:
    next(file)
    for line in file:
        line = line.strip('\n').split(',')
        sample_drug = line[drug_name_idx]
        name = (line[1] + ' ' + line[-3]).split(' ')
        name = name[1] + ' ' + name[-1]
        doctors.add(name)
        if sample_drug in dictionary.keys():
            dictionary[sample_drug][1] += float(line[drug_cost_idx])
            if name not in dictionary[sample_drug][0]
            dictionary[sample_drug][0].add(name)
        else:
            dictionary[sample_drug] = [{name: True}, 
                       float(line[drug_cost_idx])]
            

import pandas as pd
data = pd.read_csv(input_file, nrows=100000)
         

    
    
    for line in file:
        
    
    # reading the data
    for line in file:
        line = line.strip('\n').split(',')
        # line = [line[prescriber_id], line[drug_name], line[drug_cost]]
        #prescriber_id = int(line[prescriber_id])
        drug_name = line[drug_name_idx]
        prescriber_id = line[prescriber_id_idx]
        drug_cost = line[drug_cost_idx]
        if drug_name in drugs:    
            if prescriber_id not in drugs[drug_name][0]: # isinstance
                drugs[drug_name][0].append(prescriber_id)
            try:
                drugs[drug_name][1] += float(drug_cost)
            except ValueError:
                drugs[drug_name][1] += float(drug_name.strip('"'))
      
        else:
            try:
                drugs[drug_name] = [[prescriber_id], float(drug_cost)]
            except ValueError:
                drugs[drug_cost] = [[prescriber_id], float(drug_name.strip('"'))]

      
output_data = sorted(drugs.items(), key=lambda x: (-x[1][1], x[0]))    
output_file = r'C:\Users\Asus\Downloads\trash\de_cc_data1.txt'
#with open(output_file,"w") as file1:
file1 = open(output_file, "w") #str(sys.argv[2])
output = ["drug_name,num_prescriber,total_cost\n"]
output += [output_line[0] + ',' + str(len(output_line[1][0])) + ',' + 
           str(output_line[1][1]) + '\n' for output_line in output_data]     
file1.writelines(output)
file1.close()