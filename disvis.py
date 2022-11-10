import os

from matplotlib import pyplot as plt
import numpy as np

root = input("Please enter the path to the directory to analyze (Don't forget the '/' at the end): ")

sizes = []



def calc_autopct(pct, sizes):
    size = ((pct / 100) * np.sum(sizes)/1000000000)
    return "{:.1f}%\n({:f} GB)".format(pct, size)

def get_dir_size():
    dirlist = [item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item))]    #All directories in root
    
    for d in dirlist:

        size = 0
            
        for dirpath, dirname, files in os.walk(root + d):   #Go through all sub-directories from root
            for f in files:
                try:
                    size += os.path.getsize(os.path.join(dirpath, f))   
                except (FileNotFoundError, OSError):
                    pass
            
        sizes.append(size)
        print("Dir " + d + " analyzed")






    fig = plt.figure(figsize = (10, 7))
    plt.pie(sizes, labels=dirlist, autopct= lambda pct: calc_autopct(pct, sizes))

    plt.show()

get_dir_size()
