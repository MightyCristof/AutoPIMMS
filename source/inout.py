# functions to control input and outfile files and data structures

from os import sep
import pandas as pd

# paths are set to demo, but should be an available user argument 
# when user runs code

filepath = '../demo/'
infile = 'example_input.txt'
outfile = 'example_output.txt'

def load_data(path, filename):
    data = pd.read_csv(path+filename, delim_whitespace=True)
    return data

def save_data(path, filename, data):
    data.to_csv(path+filename, index=False, sep="\t")
    
def save_data_fmtd(path, filein, fileout, flux_list):
    orig_dat = pd.read_csv(path+filein)
    orig_dat['pred_flux'] = pd.Series(flux_list)
    orig_dat.to_csv(path+fileout, index=False, sep="\s\s")

# quick tests
#data = load_data(filepath,infile)

#save_data(filepath,outfile,data)
