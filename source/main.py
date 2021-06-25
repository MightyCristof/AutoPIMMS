import os
import sys
from dataobj import DataObj, Params
from PyQt6.QtWidgets import QApplication, QComboBox, QLabel, QPushButton, QFileDialog, QToolTip, QWidget
from PyQt6.QtGui import QFont

class PIMMSGui(QWidget):

  ncol = 0 #number of columns found in the file
  
  labelMap = {"Input Energy Range" : "input_energy",
                "Input Units" : "input_unit",
                "Output Energy Range" : "output_energy",
                "Output Units" : "output_unit",
                "Source Flux/Count Rate" : "flux_count_ratio",
                "Galactic NH (cm^-2)" : "gal_nh",
                "Model of Source" : "model_src",
                "Photon Index (Power Law)" : "phot_ind",
                "keV (Blackbody)" : "bb_temp_kev",
                "kT (Therm. Bremss.)" : "temp_kev",
                "Solar Abundance (APEC)" : "solar_abd",
                "log T (APEC)" : "logt",
                "Redshift" : "redshift",
                "Intrinsic NH (cm^-2)" : "intrinsic_nh"}

  labelNames = list(labelMap.keys())

  nLabels = len(labelNames)

  eachHeight = 20 # number of px that each label in the table uses vertically
  eachWidth = 150 # number of px that each label in the table uses horizontally

  def __init__(self):
    super().__init__()
    self.initUI()

  ####################################################
  ##### Functions that interact with the backend #####
  ####################################################

  def useFile(self, file):
    print("filename is " + file)

    ## load file into data frame
    self.dObj = DataObj()
    self.dObj.load_data(file)
    self.ncol = self.dObj.ncol

    fileLabel = QLabel(self)
    fileLabel.setText(str("File {} has {} columns").format(os.path.basename(file), self.ncol))
    fileLabel.move(10,80)
    fileLabel.show()
    self.createColumnDropdown(self.ncol)


  # Submit job to PIMMS
  def submitJob(self):
    #do all the stuff here

    for col in self.labelNames:
      # col: nice column name
      # self.labelMap[col]: match to params
      # idx: int of column 
      idx = self.dropdown[col].currentIndex() - 1 # -1 means not select, 0-ncol corresponds to the file column.
      print(idx)
      params = Params()
      # params[self.labelMap[col]] = self.data[idx]

      # newHeaders = zip(self.labelMap[col], idx)

      print(str("Column {} has value {}").format(col, idx))
    
    outputContent = "this is the nice output we will save to file"
    file = open(self.outputFilename, "w")
    file.write(outputContent)
    file.close()

  #########################
  ##### GUI Functions #####
  #########################

  # Create the table 
  def createColumnDropdown(self, ncol):

    #use empty dicts for labels and dropdowns
    labels = {}
    self.dropdown = {}

    dropdowns = {"Input Energy Range" : 0, "Output Energy Range" : 1, "Output Unit" : 2, "Model of Source" : -1 }

    for col in self.labelNames:
      labels[col] = QLabel(self)
      labels[col].setText(col)
      labels[col].move(30, 120 + self.labelNames.index(col) * self.eachHeight)
      labels[col].show()
      self.dropdown[col] = self.getDropdown(30 + self.eachWidth, 110 + self.labelNames.index(col) * self.eachHeight, ncol)
      self.dropdown[col].show()
    
    # Submit job button
    self.submit = QPushButton('Submit', self)
    self.submit.resize(self.submit.sizeHint())
    self.submit.move(300, 450)
    self.submit.clicked.connect(self.submitJob)
    self.submit.show()
    self.submit.setDisabled(True)

    # Output file selection button
    outputFile = QPushButton('Output file', self)
    outputFile.resize(outputFile.sizeHint())
    outputFile.move(150, 450)
    outputFile.clicked.connect(self.outputFileDialog)
    outputFile.show()

  #########################
  ##### Aux functions #####
  #########################

  # Function to create a dropdown with specific values in a specific position 
  def getDropdown(self, posX, posY, ncol):
    dropdown = QComboBox(self)
    #add values using the number of columns
    dropdown.addItem("No mapping")
    for value in range(ncol):
      dropdown.addItem(str("Column #{}").format(value+1))
    #set position
    dropdown.move(posX, posY)
    return dropdown
    
  # Open menu to select input file and trigger process
  def inputFileDialog(self):
    dialog = QFileDialog()
    #for now we only accept csv
    input_format = 'csv'

    dialog.setFilter(dialog.filter())
    #file must exist
    dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    #open file when selected
    dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)

    dialog.setDefaultSuffix(input_format)
    dialog.setNameFilters([f'{input_format} (*.{input_format})'])
    
    if dialog.exec():
      filename = dialog.selectedFiles()[0]
      self.btn.setDisabled(True)
      self.useFile(filename)

  # Open menu to select output file
  def outputFileDialog(self):
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.AnyFile)
    #open file when selected
    dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)

    if dialog.exec():
      self.outputFilename = dialog.selectedFiles()[0]
      self.submit.setEnabled(True)

  # Create main window
  def initUI(self):

    QToolTip.setFont(QFont('SansSerif', 10))

    self.text = QLabel(self)
    self.text.setText("Please select your input CSV file:")
    self.text.move(10, 20)
    self.text.show()

    self.btn = QPushButton('Open file', self)
    self.btn.resize(self.btn.sizeHint())
    self.btn.move(30, 40)
    self.btn.clicked.connect(self.inputFileDialog)

    self.setGeometry(200, 200, 500, 500)
    self.setWindowTitle('AutoPIMMS')
    self.show()


def main():

    app = QApplication(sys.argv)
    gui = PIMMSGui()
    gui.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()