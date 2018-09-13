## WJ Vanderlip NE204 Lab 0

Data was collected with a Coaxial HPGe detector with Co-60,
Am-241, Ba-133, Cs-137 and Eu-152 sources.

A python script was written to perform an energy calibration for the
Am-241 and Cs-137 sources. Results are presented via a calibrated energy
spectrum and a statistical comparison of the calibration vs accepted values
for Ba-133 gamma energies.

Instructions for using the Makefile to run the calibration script and
compiling the LaTeX lab report are posted below:

### Install Becquerel

Becquerel is a Python package for analyzing nuclear spectroscopic measurements developed by the Applied Physics Program at LBNL. The core functionalities are reading and writing different spectrum file types, fitting spectral features, performing detector calibrations, and interpreting measurement results. It includes tools for plotting radiation spectra as well as convenient access to tabulated nuclear data, and it will include fits of different spectral features. It relies heavily on the standard scientific Python stack of numpy, scipy, matplotlib, and pandas. It is intended to be general-purpose enough that it can be useful to anyone from an undergraduate taking a laboratory course to the advanced researcher.

https://github.com/lbl-anp/becquerel


```
git clone https://github.com/lbl-anp/becquerel.git
pip install -r requirements.txt
python setup.py install --user
```

### Setting up the Lab 0 repo
```
git clone https://github.com/NE204-Fall2018/wjvanderlip-lab0.git
pip install -r requirements.txt
```

### File instructions

#### Step 1: Download the data
```
make data

```
This will download a text file of the from dropbox with all necessary data.

#### Step 2: Ensure the data is not corrupted:
```
make validate
```
Downloads the checksum from dropbox and runs the comparison between the data file and checksum
to ensure the data was not corrupted.

#### Step 3: Test key functions within analysis script:
```
make test
```

#### Step 4: Run analysis script

```
make analysis
```
Runs the python script which conducts a linear energy calibration of the Cs and Am data. Then compares
this calibration with the accepted values of the Ba gamma energies. This call will output three figures into the images
folder as well as update two LaTeX tables for the report.

### Step 5: Compile the lab report using outputs from the calibration script
```
make
```
Will output report.pdf as the final document.
