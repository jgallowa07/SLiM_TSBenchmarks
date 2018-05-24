import sys as os
from pathlib import Path


import matplotlib.pyplot as plt
'''
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
'''

'''
rootdir = Path('/Users/jared/Documents/SLiM_TSBenchmarks/Bench/ComparisonTimes/RealTimes')
# Return a list of regular files only, not directories
file_list = [f for f in rootdir.glob('**/*') if f.is_file()]

print(file_list)
'''

import sys
import re
files = []

P = [1000,10000]

timing_data = {}
memory_data = {}

'''
Keys

neut_timing_N1000
neut_timing_N10000
pedNM_timing_N1000
pedNM_timing_N10000
ped_timing_N1000
ped_timing_N10000
rel_timing_N1000
rel_timing_N10000
'''
for i in sys.argv[1:]:
    OK = True
    for line in open(i, 'r'):
        if re.search('non-zero', line):
            OK = False
            break
    if OK is True:
        files.append(i)

for i in files:
    
    sep_value = i.split(".")
        
    #print(sep_value)
    N = sep_value[2][1:]
    Rho = sep_value[3][4:]
    trace_key = sep_value[1][1:] + "_" + sep_value[2]
    fp = open(i,'r')
    data = fp.readline().split('/')
    runtime = float(data[2]) / 60 / 60
    memory = float(data[3])
    #print(runtime,memory)

    if (trace_key in timing_data):
        timing_data[trace_key].append(runtime)
        memory_data[trace_key].append(memory)
    else:
        timing_data[trace_key] = [runtime]
        memory_data[trace_key] = [memory]

#print(timing_data)

PopSizes = ['N = 1e+03','N = 1e+04']

f, axarr = plt.subplots(1,2,sharey=True,sharex=True)
axarr[0].plot(P,timing_data['neut_timimg_N1000'],'go-',label=PopSizes[0])
axarr[0].plot(P,timing_data['neut_timimg_N10000'],'b^-',label=PopSizes[1])
axarr[0].legend(loc='upper left',frameon=False)
axarr[0].set_xscale('log')
axarr[0].set_ylabel('Run time (hours)',fontsize='small')
axarr[0].set_xlabel('Scaled recombination rate (' + r'$\rho = 4Nr$)',fontsize='small')
axarr[0].set_title('With Neutral Mutations',fontsize='medium')

axarr[1].plot(P,timing_data['ped_timimg_N1000'],'go-',label=PopSizes[0])
axarr[1].plot(P,timing_data['ped_timimg_N10000'],'b^-',label=PopSizes[1])
axarr[1].legend(loc='upper left',frameon=False)
axarr[1].set_xlabel('Scaled recombination rate (' + r'$\rho = 4Nr$)',fontsize='small')
axarr[1].set_title('With Pedigree Recording',fontsize='medium')
plt.show()


'''
f, axarrr = plt.subplots(1,2,sharey=True,sharex=True)
axarr[0].plot(P,timing_data['rel_timimg_N1000'],'go-',label=PopSizes[0])
axarr[0].plot(P,timing_data['rel_timimg_N10000'],'b^-',label=PopSizes[1])
axarr[0].legend(loc='upper left',frameon=False)
axarr[0].set_xscale('log')


axarr[1].plot(P,timing_data['rel_timimg_N1000'],'go-',label=PopSizes[0])
axarr[1].plot(P,timing_data['rel_timimg_N10000'],'b^-',label=PopSizes[1])
'''     

   




