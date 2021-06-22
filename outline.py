# AutoPIMMS functionality and structure outline

# AutoPIMMS "first edition" will read data from a text file into a pandas (or similar) object, 
# default Input Energy Range as the axis to iterate over, then input all appropriate values into
# the WebPIMMS interface while varying only along the chosen axis.

# WebPIMMS URL: https://heasarc.gsfc.nasa.gov/cgi-bin/Tools/w3pimms/w3pimms.pl

# The following is a very simple outline of possible functions, not necessarily in order.

### data loading and parsing ###
# allow user to input the name of the data file?
# load data file with column names into array, list, etc.

### "fetch" WebPIMMS vals input, submission, results parse ###
# using mechanize package Forms API, input values and menu selections based on known HTML tags
# all values remain fixed at each iteration except varying axis
# submit using mechanize.HTMLForm.click()
# after submission, parse results page for correct line of text

### saving results to temp list ###
# save the output value to array, list, etc.

### iterative loop ###
# this should talk to the data array for how many steps to iterate
# loads single line of data into object of params class and passes to "fetch"
# the WebPIMMS functions might be nested inside this function so it makes a call to the webpage
# for each iteration

### data output ###
# concatenate to input data and write out to new text file

#------------------------------------------------------------------------------------------------#

# Possible future functionalities:
# - user selection of varying data axis
# - multiple varying axes
# - loading of customized input/output ranges based on instrument
# - adding functionality for differing data structures
