from os import sep
import argparse as arg
import pandas as pd
import mechanicalsoup


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

## load data frame and return number of columns
class DataObj:
    def load_data(self, filename):
        self.data = pd.read_csv(filename)
        self.ncol = len(self.data.columns)

## ping web form
def fetch(input):
    ## pull the URL and select the form
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://heasarc.gsfc.nasa.gov/cgi-bin/Tools/w3pimms/w3pimms.pl")
    #browser.page.find_all('select')
    browser.select_form('form[action="/cgi-bin/Tools/w3pimms/w3pimms.pl"]')
    #browser.form.print_summary()

    ## required form fields    
    browser.form.set_select({"from": input.conv_from+"\n"})
    browser.form.set_select({"sat": input.conv_to+"\n"})
    browser["range"] = input.input_energy
    browser["etype"] = input.input_unit
    browser["orange"] = input.output_energy
    browser["otype"] = input.output_unit
    browser["flusso"] = input.flux_count_ratio
    browser["nh"] = input.gal_nh
    ## choice of model and corresponding field(s)
    browser["model"] = input.model_src
    if input.model_src == 'Power Law':
        browser["gama"] = input.phot_ind
    elif input.model_src == 'model_black_body':
        browser["gamb"] = input.bb_temp_kev
    elif input.model_src == 'model_therm_bremss':
        browser["gamc"] = input.temp_kev
    elif input.model_src == 'model_apec':
        browser.form.set_select({"solar": input.solar_abd+"\n"})
        browser.form.set_select({"logt": input.logt+"\n"})
    else:
        print("No source model set.")
        exit()
    ## optional form fields
    browser["red"] = input.redshift
    browser["nhi"] = input.intrinsic_nh

    ## get response and filter on absorbed flux
    response = browser.submit_selected()
    re = response.soup.find_all("h3")
    re = [x.text for x in re if ("a flux") in x.text]
    oflux = re[0].split()[-2]
    
    return oflux

## save output to new file
def save_data_fmtd(input_data, fetched_data, fileout):
    ## assign new column to input data and save as .CSV
    output_data = input_data.assign(output_flux=pd.Series(fetched_data,dtype='float64').values)
    output_data.to_csv(fileout, index=False, sep=",")

parser = arg.ArgumentParser()
parser.add_argument('--filein', help='filein, e.g., example_input.csv', type=str, default='')
parser.add_argument('--fileout', help='fileout, e.g., example_output.csv', type=str, default='autopimms_out.csv')
args = parser.parse_args()

## check input
## lack of input file
if args.filein == '':
    print('No input file defined.')
    exit()
## not a .CSV file
ext = args.filein.rpartition('.')[-1].upper()
if ext != 'CSV':
    print('Input must be a CSV file.')
    exit()

## load file into data frame
dObj = DataObj()
dObj.load_data(args.filein)
data = dObj.data

## create fetch object
data_row = Params()

## output variable
output_flux = []

## iterate over each row of data frame
for index, row in data.iterrows():
    data_row.input_energy = row["input_energy"]
    output_flux.append(fetch(data_row))

## add output and save to file
save_data_fmtd(data,output_flux,args.fileout)

