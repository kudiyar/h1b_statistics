# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 22:43:57 2018

@author: Asus
"""
import sys
#import os
#import csv
#os.chdir("H:\My Drive\job_updatable\data_insight")
#os.chdir(r"C:\Users\Asus\Desktop\data_insight")
# function that will find the indices of top states or jobs
def calculate_rank(vector):
    a={}
    rank = 1
    v_s = sorted(vector, reverse=True)
    indices = []
    for i, num in enumerate(v_s):
        if num in a:
            a[num] = rank
        else:
            if i == 0:
                a[num] = rank
            else:
                rank = rank + vector.count(v_s[i-1])
                # it will break if the rank of an interest variable is above 10
                if rank > 10:
                    break
                a[num] = rank
    top10_counts = sorted(list(a.keys()), reverse=True)
    # we are interested in the indices of top 10 interest variable
    for j in range(1,len(top10_counts)+1):
        indices += [i for i, x in enumerate(vector) if x == top10_counts[j-1]]
    return indices
# filename
file = str(sys.argv[1]) # "../input/h1b_input.csv" # 
# key variables
status = ['CASE_STATUS', 'STATUS'] # STATUS in 2014, CASE STATUS in 2015,2016
soc_code = ['SOC_NAME', 'LCA_CASE_SOC_NAME']
job_title = 'JOB_TITLE'
employer_state = ['WORKSITE_STATE']#['EMPLOYER_STATE', 'LCA_CASE_EMPLOYER_STATE']
# reading the file
input_file = open(file, 'r')
headers = input_file.readline().split(";")
# getting the indices of key variables
status_ind = [headers.index(c) for c in status if c in headers][0]
#j_ind = headers.index(job_title)    
c_ind = [headers.index(c) for c in soc_code if c in headers][0]
s_ind = [headers.index(c) for c in employer_state if c in headers][0]
# reading the rest of the file
data_list = [[job_title, employer_state[0]]]
for line in input_file: # do I need i
    #print(i)
    currentline = line.split(";")
    # We will filter only applications which was certified 
    if currentline[status_ind] == 'CERTIFIED': 
        currentline = [currentline[c_ind].strip('\"'), currentline[s_ind]]
        data_list.append(currentline)
input_file.close()
# total number of certified h1b's 
l = len(data_list)
# we will work to get top occupations
for k in range(2):
#    if  k == 0:
#        continue
    all_jobs = [data_list[i][k] for i in range(1,l)]
    job_list = sorted(set(all_jobs))
    job_counts = [all_jobs.count(x) for x in job_list]
    top10_indices = calculate_rank(job_counts)
    # write top 10 occupations to a file.
    if k == 0:
        file1 = open(str(sys.argv[2]),"w") # open("../output/top_10_occupations.txt", "w") #
        L = ["TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n"]
    else:
        file1 = open(str(sys.argv[3]),"w") # open("../output/top_10_states.txt", "w") #
        L = ["TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n"]
    for i, idx in enumerate(top10_indices):
        L += [job_list[idx] + ";" + str(job_counts[idx]) + ";" + str(round(job_counts[idx]*100/(l-1), 2))+"%\n"]
    #del all_jobs, job_list, job_counts, top10_indices # not sure
    file1.writelines(L) 
    file1.close() 