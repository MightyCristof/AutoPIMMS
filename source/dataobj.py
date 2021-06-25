import pandas as pd


## load data frame and return number of columns
class DataObj:
    def load_data(self, filein):
        self.data = pd.read_csv(filein,header=None)
        self.ncol = len(self.data.columns)

    ## save output to new file
    def save_data(self, fetched_data, fileout):
        ## assign new column to input data and save as .CSV
        output_data = self.data.assign(output_flux=pd.Series(fetched_data,dtype='float64').values)
        output_data.to_csv(fileout, index=False, sep=",")

## add output and save to file
#save_data(data,output_flux,args.fileout)


## object class for data
class Params: 
    def __init__(self):
        ## class parameters should remain blank unless a value passed
        self.conv_from = "Flux"
        self.conv_to = "FLUX"
        self.input_energy = "2-7"
        self.input_unit = "kev"
        self.output_energy = "2-10"
        self.output_unit = "kev"
        self.flux_count_ratio = 1
        self.gal_nh = 2e20
        self.redshift = "none"
        self.intrinsic_nh = "none"
        self.model_src = "Power Law"
        self.phot_ind = 1.8
        self.bb_temp_kev = 1.0
        self.temp_kev = 1.0
        self.solar_abd = "1.0 Solar Abundance"
        self.logt = "6.00 | 0.0862"
