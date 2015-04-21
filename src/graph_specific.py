'''
Created on Apr 20, 2015

@author: gmccabe
'''
'''
Created on Apr 20, 2015

@author: gmccabe
'''
#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt
import single_drug_all

specific_demo = single_drug_all.zipped

all_demo = single_drug_all.query_drug(single_drug_all.drug_name, 11)
               


N = 5
specific_bayes_init = []
side_effect_init = []

count = 0
for line in specific_demo:
    if count < 5:
        print line[1]
        specific_bayes_init.append(abs(line[1]))
        side_effect_init.append(line[0])
    count = count + 1    
#lprint menMeans

specific_bayes = np.array(specific_bayes_init)
side_effect = np.array(side_effect_init)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, specific_bayes, width, color='r') #, yerr=menStd)

#womenMeans = (25, 32, 34, 20, 25)
#womenStd =   (3, 5, 2, 3, 3)
#rects2 = ax.bar(ind+width, womenMeans, width, color='y', yerr=womenStd)

# add some text for labels, title and axes ticks
ax.set_ylabel('Absolute Value of Naive Bayes Score( the lower the score the more likely it is)', fontsize= 8)
ax.set_title('Side-effect Naive Bayes')
#ax.set_xlabel('Side Effect', 12)
ax.set_xticks(ind+width)
#ax.set_xticklabels( ('G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11') )
ax.set_xticklabels(side_effect, fontsize= 6)
ax.legend( (rects1[0], 'Men'))

def autolabel(rects):
    #attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

#autolabel(rects1)
#autolabel(rects2)

plt.show()