# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run Instructions](README.md#run-instructions)

# Problem

Historical data for H1B visas are  available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

Therefore, we should analyze the past data and particularly do calculations in two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

We also want the code to be working for all years and producing the required results.

# Approach

Raw data is large and we are only interested in the subset of the raw data which are the cases where case status is **CERTIFIED**. To do that efficiently without storing the whole data in Python namespace(environment), we will filter only the rows of interest as we are reading the file. In addition, we are not interested in all columns of the data so we will also store the columns of interest(job location state and job title) for our problem.

After we read all the data, we will find unique strings of variable of interest and sort them. Then, using these unique strings we will count the number of times each string occurs in the data along with the indexes it appears in the unique strings' list. Finally, we sort again to get the sorted list with highest counts being on the top.

The last step is to write the sorted lists to **txt** files. 

# Run Instructions
Using the command line on a Linux machine, you run the same way as in **run.sh** file except for three arguments you have to specify the location of the data file along with its name and locations for output files along with the names you give to the files.
