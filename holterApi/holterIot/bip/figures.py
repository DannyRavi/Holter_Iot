import matplotlib.pyplot as plt

import pandas as pd 
import matplotlib.pyplot as plt
#import ecg_plot

def my_figure():
    data = pd.read_csv("ECG2.csv") 
    fig, ax = plt.subplots()
    v1 = []
    v1 = data.V2
    ecg = v1[1:250]
   # ax.plot([1, 3, 4 , 5 ,6], [3, 2, 5 , 5 ,-1])
    ax.plot(ecg)
    return fig



# Preview the first 5 lines of the loaded data 


# plt.plot(u)
# plt.ylabel('some numbers')
# plt.show()