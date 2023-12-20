import numpy as np
import matplotlib.pyplot as plt

#Bemeneti adatok
x = np.array([1,2,3,4,5,6,7])
mert_ero = np.array([
                0.54167,
                0.50352,
                0.48826,
                0.473,
                0.45774,
                0.45011,
                0.43485])
magnes_ero = np.array([
                0.22838,
                0.19023,
                0.17497,
                0.15971,
                0.14445,
                0.13682,
                0.12156])
#Meghívások
fuggveny_abr(x , mert_ero , 
            param_megh(x, mert_ero), 
            "" , "",
            "o")
fuggveny_abr(x , magnes_ero , 
            param_megh(x, magnes_ero), 
            "Δx[mm]" , "Mágnes ereje(x) és Mért erő(o) [N] ",
            "x")

#Paraméterek meghatározása
def param_megh(x, y):
    #Mérések száma
    n = np.size(x)
 
    #Átlag számítás
    m_x = np.mean(x)
    m_y = np.mean(y)
 
    #∑yx és ∑x^2
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
 
    #paraméterek
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return (b_0, b_1)
#Grafikon ábrázolása
def fuggveny_abr(x, y, param, x_felirat, y_felirat, jel):
    #Adatpontok ábrázolása
    plt.scatter(x, y, color = "m", marker = jel, s = 30)
 
    #Egyenes számítása és ábrázolása
    plt.plot(x , param[0] + param[1]*x , color = "g")
 
    #Tengelyek feliratozása
    plt.xlabel(x_felirat)
    plt.ylabel(y_felirat)