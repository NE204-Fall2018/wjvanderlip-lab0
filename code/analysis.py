#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import becquerel as bq
import uncertainties as uc
from tools204 import linear_calib, gammaEnergy, isoDetails, simpleFindPeak


def get_change(exp_val, accepted):
    if exp_val == accepted:
        return 0.00 #no change
    return (abs(exp_val - accepted) / abs(accepted)) * 100.0

def do_work():
    data = np.loadtxt('../lab0_spectral_data.txt', comments="#", delimiter='\t', usecols=None)

    am = []
    ba = []
    cs = []
    co = []
    eu = []
    for s in range(5):
        for col in range(len(data)):
            x = data[col][s]
            if s == 0:
                am.append(x)
            if s == 1:
                ba.append(x)
            if s == 2:
                cs.append(x)
            if s == 3:
                co.append(x)
            if s == 4:
                eu.append(x)
    source_list = (am, ba, cs, co, eu)

    headers = ['$^{241}$Am',' ', '$^{137}$Cs']
    for p in [0, 2]:
        plt.semilogy(source_list[p], label=headers[p])
    plt.title('Lab 0 Uncalibrated $^{241}$Am and $^{137}$Cs Spectra')
    plt.xlabel("Channel")
    plt.ylabel("Counts")
    plt.legend()
    plt.savefig('../images/am_cs_uncalibrated.png')
    plt.clf()
    #plt.show()

    csE, csDF = gammaEnergy("Cs-137")
    amE, amDF = gammaEnergy("Am241")
    energies, plotdata = linear_calib([amE[1][0], csE[0]], [source_list[0], source_list[2]])


    plot_calib = []  #removes error so it will plot
    for e in energies:
        plot_calib.append(e.nominal_value)
    for p in [0, 2]:
        plt.semilogy(plot_calib, source_list[p], label=headers[p])
    plt.title('Lab 0 Calibrated $^{241}$Am and $^{137}$Cs Spectra')
    plt.xlabel("Energy [keV]")
    plt.ylabel("Counts")
    plt.legend(loc=1)
    plt.xlim(0, 1200)
    plt.savefig('../images/am_cs_calibrated.png')
    plt.clf()
    #plt.show()

    ## finds points for error plotting, error is so small it does not render on linear calib plot
    y1 = plotdata[0] * plotdata[2]+plotdata[1]
    y2 = plotdata[0] * plotdata[3]+plotdata[1]

    linear = []
    for x in range(len(source_list[0])):
        linear.append(plotdata[0].nominal_value*x+plotdata[1].nominal_value)

    plt.plot(range(len(linear)), linear, label='Linear Fit')
    plt.errorbar(plotdata[2], y1.nominal_value, yerr = y1.std_dev, ecolor="red")
    plt.errorbar(plotdata[3], y2.nominal_value, yerr = y2.std_dev, markersize=14)
    plt.title('Lab 0 Linear Fit')
    plt.xlabel("Channel")
    plt.ylabel("Energy [keV]")
    plt.legend(loc=0)
    #plt.xlim(0, 1500)
    plt.savefig('../images/linear_fit.png')
    plt.clf()
    #plt.show()


    plt.semilogy(plot_calib, ba, c='purple', label='$^{133}$Ba')
    plt.title('Lab 0 Calibrated $^{133}$Ba Spectra')
    plt.xlabel("Energy [keV]")
    plt.ylabel("Counts")
    plt.legend(loc=1)
    plt.xlim(0, 550)
    plt.savefig('../images/ba_calibrated.png')
    plt.clf()
    #plt.show()

    found_list = simpleFindPeak(ba, 7, 5, energies)

    baE, baDF = gammaEnergy("Ba133")

    select_list = [10, 13, 0, 12, 2, 4, 14]  #hard coded to link values from peak finder to accepted values
    info = isoDetails('Ba-133') #used to make latex data frame of Ba133 info

    final_compile = []
    for e in range(7):
        accepted = baE[select_list[e]][0]
        exp_val = found_list[e][2]
        d = get_change(exp_val, accepted)
        final_compile.append((exp_val, accepted, d))
    final_DF = pd.DataFrame(final_compile, index=None, columns=['Calculated Energy [keV]', 'Accepted Value [keV]',
                                                           'Precent Difference %'])

    ## takes data frame and writes to latex outfiles, index=False as to not display index in latex
    with open('../text/final_table.tex','w') as tf:
        tf.write(final_DF.to_latex(index=False))

    with open('../text/Ba133_table.tex','w') as tf:
        tf.write(info.loc[select_list].to_latex(index=False))


if __name__ == '__main__':
    do_work()
