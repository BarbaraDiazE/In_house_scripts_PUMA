import pandas as pd 
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

import seaborn as sns

import os
from scipy.stats import uniform
import scipy.special
from pylab import savefig



def grid_boxplot(file, descriptor):
    data = pd.read_csv(file1, index_col="Unnamed: 0")


    colors_dict = {
        "APEXBIO":"mediumvioletred",
        "Asinex":"mediumslateblue",
        "ChemDiv":"lightsalmon",
        "Enamine":"gold",
        "Life_Chemicals":"violet",
        "MedChemExpress":"mediumaquamarine",
        "OTAVA_DNMT1":"steelblue",
        "OTAVA_DNMT3b":"navy",
        "SelleckChem":"darkred",
        "Targetmol":"indigo",
        "Tocris":"pink"
    }

    sns.boxplot(data=data, x="Library", y="TPSA", palette=colors_dict.values())
    plt.xlabel("Library", fontsize=14)
    plt.ylabel("TPSA",fontsize=14)
    plt.subplots_adjust(left=0.064, bottom=0.076, right=0.962, top=0.952)
    plt.show()


file1 = "/Users/eurijuarez/Desktop/Alexis/Quimiotecas_enfocadas_descriptores/AllDB_descriptores.csv"

grid_boxplot(file1, "TPSA")