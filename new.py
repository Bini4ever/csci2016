import numpy as np
from datascience import *

# These lines do some fancy plotting magic.
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.simplefilter('ignore', FutureWarning)
import pandas as pd

def main():

   Mined_Ar = make_array(47.9062, 50.2549, 49.7059, 47.6818, 47.6538, 49.1143)
   FinalBlock_Ar = make_array(7, 25.8235, 37.5294, 45.5, 10.2692, 24.5143)
   df = pd.DataFrame({'Mined': Mined_Ar, 'FinalBlock': FinalBlock_Ar},
                    index=['function-fork-1', 'function-fork-2','function-fork-4', 
                           'function-fork-8', 'petty-honest', 'lazy-fork']) 
   Mined_vals = df.Mined
   Final_vals = df.FinalBlock                         

   ind = np.arange(df.shape[0])
   width = 0.40

   # Set the colors
   colors = ['b', 'g', 'r', 'c', 'm', 'y', 'g']


   def autolabel(bars):
       # attach some text labels
       for bar in bars:
           width = bar.get_width()
           ax.text(width*0.95, bar.get_y() + bar.get_height()/2,
                   '%d' % int(width),
                   ha='right', va='center')
   # make the plots
   fig, ax = plt.subplots()
   mined = ax.barh(ind, Mined_vals, width, color = colors) # plot a vals
   final = ax.barh(ind + width, Final_vals, width, color = colors, alpha=0.5)  # plot b vals
   ax.set_yticks(ind + width)  # position axis ticks
   ax.set_yticklabels(df.index)  # set them to the names
   ax.legend((mined[0], final[0]), ['Mined', 'Made it to final'], loc='center right')

   autolabel(mined)
   autolabel(final)

   plt.show()

   
if __name__ == "__main__":
    main()
