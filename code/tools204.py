#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import becquerel as bq
import uncertainties as uc

def linear_calib(nrg_list, hist_list):
    '''
    nrg_list   float                list of known energies to calibrate against, loaded from low to hight

    hist_list   list of histograms  histogramed detector data

    returns

    energies   list     calibrated energy list
    '''

    chan=list(range(1,len(hist_list[0])+1)) #number of channels:8192

    centroid_x1=np.argmax(hist_list[0]) # 661.66 keV
    centroid_x2=np.argmax(hist_list[1]) # 59.54 keV

    x1=centroid_x1
    x2=centroid_x2

    y1=nrg_list[0]
    y2=nrg_list[1]

    energies=[]
    m=(y2-y1)/(x2-x1)
    b=(-m*x1+y1)
    print(m,b)

    chan_array=np.array(chan)

    for i in chan:
        energies.append(np.multiply(m, chan_array[i-1])+b)

    return energies, (m, b, x1, x2)

def gammaEnergy(isotope):
    data = bq.tools.fetch_decay_radiation(nuc=isotope, i_range=(5, 100), type='Gamma')
    data[['Z', 'Element', 'A', 'Decay Mode', 'Radiation', 'Radiation Energy (keV)', 'Radiation Intensity (%)', 'T1/2 (txt)']]
    npeaks = len(data['Radiation Energy (keV)'])
    if npeaks > 1:
        elist = []
        err_list = []
        for p in range(npeaks):
#                 try:
#                     energy = data.loc[p, 'Radiation Energy (keV)'].nominal_value
#                     err = data.loc[p, 'Radiation Energy (keV)'].std_dev

#                 except AttributeError as e:
#                     energy = data.loc[p, 'Radiation Energy (keV)']
#                     err = 0.00
                energy = data.loc[p, 'Radiation Energy (keV)']
                I = data.loc[p, 'Radiation Intensity (%)']
                elist.append((energy, I))
                #err_list.append(err)
        df = pd.DataFrame(elist, index = None, columns= ['Energy (keV)','Intensity %'])
        return elist, df

    energy = data.loc[0, 'Radiation Energy (keV)'].nominal_value
    I = data.loc[0, 'Radiation Intensity (%)']
    df = pd.DataFrame([(energy,I)], index = None, columns= ['Energy (keV)', 'Intensity %'])
    return (energy, I), df

def isoDetails(isotope):
    data = bq.tools.fetch_decay_radiation(nuc=isotope, i_range=(5, 100), type='Gamma')
    info = data[['Z', 'Element', 'A', 'Decay Mode', 'Radiation', 'Radiation Energy (keV)', 'Radiation Intensity (%)', 'T1/2 (txt)']]
    return info


def simpleFindPeak(array, num_peaks, stripLR, calibrated_energy):
    '''
    Inputs
    ===============
    aray                list or array
                        histogrammed data to search for peaks in

    num_peaks            str
                        in YYYY-MM-DD format

    n_sites_text        str
                        string of index values for sites to check, this input is checked
                        to make sure each input is an int

    dest_email          str
                        e-mail address to send notification to, proper entry checked by validate_email



    Returns
    ================
    site_text           str
                        pulls a string from the returned html so let the user know if there are multiple
                        locations availale within the campsite
    '''
    c = 0
    workingcopy = array
    found_list = []
    while c < num_peaks:
        nrg = np.argmax(workingcopy)
        found_list.append((nrg, workingcopy[nrg], calibrated_energy[nrg]))
        for r in range(nrg-stripLR, nrg+stripLR):
            workingcopy[r]=0
        c +=1
    print(found_list)
    return found_list
