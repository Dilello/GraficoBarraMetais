import glob
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import locale
# Confirando para formato local Brasileiro para vírgula como sperador decimal
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


# DEFINICAO DA FONTE
tamanho = 12
plt.close('all')
plt.rcdefaults()
plt.rcParams['axes.formatter.use_locale'] = True
plt.rc('text', usetex = False)
plt.rc('font', family = 'sans-serif')
plt.rc('font', serif = 'Calibri')
plt.rc('legend',fontsize = tamanho)
plt.rc('font', size = tamanho)         
plt.rc('axes', titlesize = tamanho)    
plt.rc('axes', labelsize = tamanho)   
plt.rc('xtick', labelsize = tamanho)  
plt.rc('ytick', labelsize = tamanho)
plt.rc('figure', titlesize = tamanho) 



def USunid_BRunid(lista, numCasas):
    lista1 = []
    casas = '{:,.'+str(numCasas)+'f}'
    for i in range(1,len(lista)):
        '''Criando uma lista de strings de números expressos com ponto no decimal e vírgula no milhar'''
        lista1 = [casas.format(lista[i-1]), casas.format(lista[i])]
        '''Convertendo strings de numeros com ponto no decimal e vírgula no milhar para 
        strings com virgula no decimal e pono no milhar:'''
        lista2 = []
        for j in range(len(lista1)):
            a = lista1[j]
            a1 = a.replace(',', 'x') # troca provisoriamente a virgula do milhar para string 'x'
            a2 = a1.replace('.', ',') # troca ponto do decimal para vírgula
            y = a2.replace('x', '.') # traca o 'x' do milhar para ponto
            lista2.append(y)

        return lista2


# VARIAVEIS DE ENTRADA

labels = ['mai-22', 'nov-22']
lista1 = [20540, 12040.5512]
lista2 = [6345, 4344.4343]
numCasas = 2
conc1  = USunid_BRunid(lista1, numCasas)
conc2  = USunid_BRunid(lista2, numCasas)
x = np.arange(len(labels))  # the label locations
width = 0.45  # the width of the bars
x1 = [0, 1]
y = [10, 10]

# GRÁFICO DE BARRAS

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, lista1, width, label='Mont.')
rects2 = ax.bar(x + width/2, lista2, width, label='Jus.', color = 'k', alpha = 0.5)

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize = '16', weight='bold' )
ax.set_yticks([])
ax.set_yticklabels([])
ax.bar_label(rects1, labels = conc1, padding=3, fontsize = '16', color = 'blue', weight='bold')
ax.bar_label(rects2, labels = conc2, padding=3, fontsize = '16', color = 'k', weight='bold', alpha = 0.5)
ax.set(frame_on=False)  # New

ax2 = ax.twinx()
rects3 = ax2.plot(x1, y, color='r', lw = 4, label = 'Nível 1')
ax2.set_yticks([])
ax2.set_yticklabels([])
ax2.set(frame_on=False)

myl=[rects1]+rects3+[rects2]
labs=[l.get_label() for l in myl]


ax.legend(myl, labs, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol = 2, prop=dict(size =14, weight='bold'))
ax.set_title ('Alumínio (mg.kg'+r'$^{-1}$'+')', x=0.5, y=1.15, fontsize = '16', weight='bold', alpha = 0.7)

fig.tight_layout()

plt.show()
