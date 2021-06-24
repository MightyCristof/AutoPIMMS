from os import sep
import argparse as arg
import pandas as pd
import mechanicalsoup


## object class for data
class Params: 
    conv_from = "Flux\n"
    conv_to = "FLUX\n"
    input_energy = "2-7"
    input_unit = "kev"
    output_energy = "2-10"
    output_unit = "kev"
    flux_count_ratio = 1
    gal_nh = 2e20
    model_src = "Power Law"
    phot_ind = 1.8

## load data frame
def load_data(filename):
    data = pd.read_csv(filename)
    return data

## ping web form
def fetch(Params):
    ## pull the URL and select the form
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://heasarc.gsfc.nasa.gov/cgi-bin/Tools/w3pimms/w3pimms.pl")
    #browser.page.find_all('select')
    browser.select_form('form[action="/cgi-bin/Tools/w3pimms/w3pimms.pl"]')
    #browser.form.print_summary()

    ## set parameters
    browser.form.set_select({"from": "Flux\n"})
    browser.form.set_select({"sat": "FLUX\n"})
    browser["range"] = Params.input_energy
    browser["etype"] = Params.input_unit
    browser["orange"] = Params.output_energy
    browser["otype"] = Params.output_unit
    browser["flusso"] = Params.flux_count_ratio
    browser["nh"] = Params.gal_nh
    browser["model"] = Params.model_src
    browser["gama"] = Params.phot_ind

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
parser.add_argument('--filein', help='filein, e.g., example_input.txt', type=str, default='')
parser.add_argument('--fileout', help='fileout, e.g., example_output.txt', type=str, default='autopimms_out.txt')
args = parser.parse_args()

#args.filein = '../demo/input_test.txt'

## check for input
if args.filein == '':
    print('No input file defined.')
    exit()

## load file into data frame
data = load_data(args.filein)

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

