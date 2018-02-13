

import os, sys
import numpy as np
import glob, shutil
import pandas as pd

flower_path = 'flowers'

flower_type = os.listdir(flower_path)
print("Types of flowers found: ", len(flower_type))
print("Categories of flowers: ", flower_type)

flowers = []

for species in flower_type:
    #get all file names
    all_flowers = os.listdir(flower_path + '/' + species)
    #add to list
    for flower in all_flowers:
        flowers.append((species, flower_path + '/' + species + '/' + flower))

flowers = pd.DataFrame(data=flowers, columns=['category', 'image'], index=None)
flowers.head()

