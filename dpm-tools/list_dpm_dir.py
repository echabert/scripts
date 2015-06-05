#############################################################
##
## Listing of dpm subdirectories than contain root files
##
#############################################################


import os
import subprocess


def check_dir_content(base_dir, final_list):
    list = subprocess.check_output("/usr/bin/rfdir " + base_dir, shell=True)

    #print base_dir
    #print list
    subdir = []
    #for i in list.split("\n")[5:len(list)]:
    for i in list.split("\n"):
        sp = i.split()
        if len(sp) > 8:
	    subdir.append(base_dir+"/"+sp[8])

    #print subdir
    #print len(subdir)
    #if len(subdir) == 1:
    if len([i for i in subdir if i.find(".root") != -1 ])!=0: 
    	#print "here"
	final_list.append(base_dir)
    else:
        for i in range(len(subdir)):
            check_dir_content(subdir[i], final_list)
    #return subdir


base_dir="/dpm/in2p3.fr/home/cms/phedex/store/user//echabert/FlatTrees/v20150314-WildBeast-v3"

#call of a recursive function
dir_content = []
check_dir_content(base_dir, dir_content)

#print the output
for i in range(len(dir_content)):
    print dir_content[i]


