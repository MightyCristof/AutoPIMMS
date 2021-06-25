from os import sep
from .dataobj import DataObj, Params
import argparse as arg
import pandas as pd
import mechanicalsoup


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

def call_fetch(input_data, data_row):    
    ## output variable
    fetched_data = []
    
    ## iterate over each row of data frame
    for index, row in input_data.iterrows():
        data_row.input_energy = row["input_energy"]
        fetched_data.append(fetch(data_row))
    
    return fetched_data

