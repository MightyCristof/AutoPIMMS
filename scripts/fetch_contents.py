import mechanicalsoup

## dummy class for testing
class Params:
    From = "Flux"
    sat = "FLUX"
    dummy = "Examples+of+Common+FLUX+Input%2FOutput+Ranges"
    range = "2-7"
    etype = "keV"
    orange = "2-10"
    otype = "keV"
    flusso = 1
    nh = 2e20
    red = "none"
    nhi = "none"
    model = "Power Law"
    gama = 1.8
    gamb = "" 
    gamc = ""
    solar = "1.0 Solar Abundance"
    logt = ""
    frame = ""

def main():
    ## pull the URL and select the form
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://heasarc.gsfc.nasa.gov/cgi-bin/Tools/w3pimms/w3pimms.pl")
    #browser.page.find_all('select')
    browser.select_form('form[action="/cgi-bin/Tools/w3pimms/w3pimms.pl"]')
    #browser.form.print_summary()

    ## set parameters
    browser.form.set_select({"from": "Flux\n"})
    browser.form.set_select({"sat": "FLUX\n"})
    browser["range"] = Params.range
    #browser["etype"] = "keV"
    browser["orange"] = Params.orange
    #browser["otype"] = "keV"
    browser["flusso"] = Params.flusso
    browser["nh"] = Params.nh
    browser["model"] = Params.model
    browser["gama"] = Params.gama

    ## get response and filter on absorbed flux
    response = browser.submit_selected()
    re = response.soup.find_all("h3")
    re = [x.text for x in re if ("a flux") in x.text]
    oflux = re[0].split()[-2]
    print(oflux)

if __name__ == "__main__":
    main()
