# functions to control input and outfile files and data structures

import pandas as pd

# paths are set to demo, but should be an available user argument 
# when user runs code

filepath = '../demo/'
infile = 'example_input.txt'
outfile = 'example_output.txt'

def load_data(path, filename):
    data = pd.read_csv(path+filename, delimiter="\t")
    return data

def save_data(path, filename, data):
    data.to_csv(path+filename, sep="\t", index=False)

data = load_data(filepath,infile)

save_data(filepath,outfile,data)