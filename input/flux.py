# AutoPIMMS package by Chris Carroll, Ellie Lincoln, and Rosa Wallace Everson 2021

import mechanize as mz # (c) 2018? the mechanize developers

# tell mechanize the URL to parse/set input

#input parameters for WebPIMMS
#sat = "into"
#range =  "Input Energy Range"
#orange = "Output Energy Range"
#FluxCountRate = "Source Flux / Count Rate"
#nh = "Galactic nH"
#gama = "Photon Index"
def PIMMS_flux(sat, range, orange, FluxCountRate, nh, gama)
    
    flux = WebPIMMS pull
    return flux

