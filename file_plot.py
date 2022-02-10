import json
import matplotlib as plt
import numpy as np
import matplotlib.pyplot as plt
import os
import itertools


def read_json(directory, filename, metric='psnr', comparison_metric='bpp'):
    path = os.path.join(directory, filename)
    with open(path) as f:
        data = json.load(f)
        if "results" in data:
            results = data["results"]
            metric=metric
            comparison_metric=comparison_metric
            var = {
                "name": data.get("name"),
                "xs": results[comparison_metric],
                "ys": results[metric],
            }
            values = np.array(results[metric])
        else:
            results = data
            metric = metric
            comparison_metric = comparison_metric
            var = {
                "name": data.get("name"),
                "xs": results[comparison_metric],
                "ys": results[metric],
            }
            # print(values)
        return(var)



directory = "D:/CompressAI/results/kodak/"
values = []
dict = {}
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        values = read_json(directory, filename)
        for value in values:
            curve_dict = {values['name']: values['xs']}
            dict.update(curve_dict)
print(dict)
import pandas as pd
df = pd.DataFrame.from_dict(dict, orient='index')
df = df.transpose()
print(df.head())
df.plot()
plt.show()
