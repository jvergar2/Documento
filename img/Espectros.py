# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 15:38:12 2015

@author: admin
"""

import numpy as np
import matplotlib.pyplot as pl

from matplotlib import rcParams

rcParams['font.family'] = 'serif'

pl.close('all')

esp=np.loadtxt('SaNSR10.txt')

#valsx=[0.02, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.0, 2.25, 2.50, 2.75, 3.00]
valsx=[.5, 1., 1.5, 2., 2.5, 3.]
valsy=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

maxy=0.8
miny=0.0

xmin=2.0/600.
xmax=3.0

fuenteejes=20
fuentetitulos=20

pl.figure(figsize=(30./2.54, 15./2.54), facecolor='grey')

pl.xlim(xmin, xmax)
pl.ylim(miny, maxy)
pl.plot(esp[:,0], esp[:,1], '-', color='black', label='NSR-10', linewidth=3.)
pl.plot(esp[:,0], esp[:,1]*1.2, '-', color='blue', label='AFPS-95', linewidth=3.)
pl.plot(esp[:,0], esp[:,1]*1.17, '--', color='red', label='EC8', linewidth=3.)
pl.legend(loc="upper right", fontsize=16)
pl.xticks(valsx, fontsize=fuenteejes)
pl.yticks(valsy, fontsize=fuenteejes)
#pl.title(r'Apex', fontsize=fuentetitulos)
#pl.xlabel(r'Frecuencia (Hz)', fontsize=16)
pl.xlabel(r'T (s)', fontsize=25)
pl.ylabel(r'Sa (%g)', fontsize=25)
pl.grid()

pl.savefig("EspectroZonaA.pdf", facecolor='w', edgecolor='w',
           bbox_inches='tight')
#           
#
#
#
#
pl.figure(figsize=(30./2.54, 15./2.54), facecolor='grey')

pl.xlim(xmin, xmax)
pl.ylim(miny, maxy)
pl.plot(esp[:,0], esp[:,1], '-', color='black', label='NSR-10', linewidth=3.)
pl.plot(esp[:,0], esp[:,1]*1.4, '-', color='blue', label='AFPS-95', linewidth=3.)
pl.plot(esp[:,0], esp[:,1]*1.2, '--', color='red', label='EC8', linewidth=3.)
pl.legend(loc="upper right", fontsize=16)
pl.xticks(valsx, fontsize=fuenteejes)
pl.yticks(valsy, fontsize=fuenteejes)
#pl.title(r'Apex', fontsize=fuentetitulos)
#pl.xlabel(r'Frecuencia (Hz)', fontsize=16)
pl.xlabel(r'T (s)', fontsize=25)
pl.ylabel(r'Sa (%g)', fontsize=25)
pl.grid()

pl.savefig("EspectroZonaB.pdf", facecolor='w', edgecolor='w',
           bbox_inches='tight')
#
#
#
#
#
pl.figure(figsize=(30./2.54, 15./2.54), facecolor='grey')

pl.xlim(xmin, xmax)
pl.ylim(miny, maxy)
pl.plot(esp[:,0], esp[:,1], '-', color='black', label='NSR-10', linewidth=3.)
pl.plot(esp[:,0], esp[:,1]*1.2, '-', color='blue', label='AFPS-95', linewidth=3.)
pl.plot(esp[:,0], esp[:,1]*1.2, '--', color='red', label='EC8', linewidth=3.)
pl.legend(loc="upper right", fontsize=16)
pl.xticks(valsx, fontsize=fuenteejes)
pl.yticks(valsy, fontsize=fuenteejes)
#pl.title(r'Apex', fontsize=fuentetitulos)
#pl.xlabel(r'Frecuencia (Hz)', fontsize=16)
pl.xlabel(r'T (s)', fontsize=25)
pl.ylabel(r'Sa (%g)', fontsize=25)
pl.grid()

pl.savefig("EspectroZonaC.pdf", facecolor='w', edgecolor='w',
           bbox_inches='tight')