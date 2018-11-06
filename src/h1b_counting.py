# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 22:43:57 2018

@author: Asus
"""
import sys
# filename
file = str(sys.argv[1])
# key variable lists
status = ['CASE_STATUS', 'STATUS']
soc_name = ['SOC_NAME', 'LCA_CASE_SOC_NAME']
job_title = 'JOB_TITLE'
job_state = ['WORKSITE_STATE','LCA_CASE_WORKLOC1_STATE']
# reading the file
input_file = open(file, 'r')
headers = input_file.readline().split(";")
# getting the indices of key variables
status_ind = [headers.index(c) for c in status if c in headers][0] # Status index     
j_ind = [headers.index(c) for c in soc_name if c in headers][0] # Job index
state_ind = [headers.index(c) for c in job_state if c in headers][0] # State index
# reading the rest of the file
data_list = []# [[job_title, job_state[0]]]
for line in input_file:
    currentline = line.split(";")
    # We will filter only applications which was certified 
    if currentline[status_ind] == 'CERTIFIED': 
        currentline = [currentline[j_ind].strip('\"'), currentline[state_ind]]
        data_list.append(currentline)
input_file.close()
# total number of certified h1b's 
l = len(data_list)
# we will work to get top occupations
for k in range(2):
    variable_list = [data_list[i][k] for i in range(l)]
    unique_list = sorted(set(variable_list), reverse=True) # list(set(variable_list)) from last letter to first
    counts_type = [[variable_list.count(x), unique_list.index(x)] for x in unique_list]
    ranks = sorted(counts_type, reverse=True) # x3 = [[2,4], [2,3], [2,8], [9,2]] sorted(x3, reverse=True)
    r = 10
    if len(ranks) > r:
        ranks_top10 = ranks[0:r]
        # add if there multiple 10th rank
        while ranks[r][0] == ranks_top10[r-1][0]:
            ranks_top10.append(ranks[r])
            r += 1
    else:
        ranks_top10 = ranks
    # write top 10 occupations to a file.
    if k == 0:
        file1 = open(str(sys.argv[2]),"w") # open("./output/top_10_2016t_occupations.txt", "w")
        L = ["TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n"]
    else:
        file1 = open(str(sys.argv[3]),"w") # open("./output/top_10_2016t_states.txt", "w") 
        L = ["TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n"]
    L += [unique_list[i[1]] + ";" + str(i[0]) + ";" + str(round(i[0]*100/(l), 2))+"%\n" for i in ranks_top10]
    file1.writelines(L) 
    file1.close()