import matplotlib.pyplot as plt

import pandas as pd 
import matplotlib.pyplot as plt
import ecg_plot

def my_figure():

    url = 'https://raw.githubusercontent.com/DannyRavi/holterPloter/master/ECG2.csv'
    data = pd.read_csv(url, error_bad_lines=False) 
    fig, ax = plt.subplots()
    v1 = []
    v1 = data.V2
    ecg_ = v1[1:250]
   # ax.plot([1, 3, 4 , 5 ,6], [3, 2, 5 , 5 ,-1])
    ax.plot(ecg_)

    D1 = data.V2.tolist()
    for i in range(0, len(D1)): 
        D1[i] = float(D1[i]/256)
    ecg = D1#[1:150] # load data should be implemented by yourself 
    ecg_plot.plot_1(ecg, sample_rate = 500, title = 'ECG 12')
    ecg_plot.save_as_png('plot_ecg')

    # try:
    #     with open(valid_image, "rb") as f:
    #      return HttpResponse(f.read(), content_type="example_ecg/png")
    # except IOError:
    #     red = Image.new('RGBA', (1, 1), (255,0,0,0))
    #     response = HttpResponse(content_type="image/jpeg")
    #     red.save(response, "JPEG")
    #     return response
    # ecg2 = D1
   # ax.ecg_plot(ecg2, sample_rate=256, title = 'ECG')

    return fig


# Preview the first 5 lines of the loaded data 
