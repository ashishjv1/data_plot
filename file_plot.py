import json
import numpy as np
import matplotlib.pyplot as plt
import os
# import itertools
import pandas as pd


def read_json(directory, filename, metric='psnr', comparison_metric='bpp'):
    path = os.path.join(directory, filename)
    with open(path) as f:
        data = json.load(f)
        results = data["results"]
        metric = metric
        comparison_metric = comparison_metric
        var = {
            "name": data.get("name"),
            "xs": results[comparison_metric],
            "ys": results[metric],
        }
        # values = np.array(results[metric])
    return (var)


directory = "/home/puppy/CompressAI/results/kodak/"
values = []
dict_xs = {}
dict_ys = {}
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        values = read_json(directory, filename)
        for value in values:
            curve_dict_xs = {values['name']: values['xs']}
            dict_xs.update(curve_dict_xs)
            curve_dict_ys = {values['name']: values['ys']}
            dict_ys.update(curve_dict_ys)

df1 = pd.DataFrame.from_dict(dict_xs, orient='index').transpose()
df2 = pd.DataFrame.from_dict(dict_ys, orient='index').transpose()
df1 = df1[["bmshj2018-factorized", "bmshj2018-hyperprior", "WebP", "JPEG", "JPEG2000", "AV1", "cheng2020-anchor", "cheng2020-attn", "VTM"]]
df2 = df2[["bmshj2018-factorized", "bmshj2018-hyperprior", "WebP", "JPEG", "JPEG2000", "AV1", "cheng2020-anchor", "cheng2020-attn", "VTM"]]
df_name = df1.columns
xs = df1[:].values
ys = df2[:].values
linestyle = "-"
figsize = (9, 6)
fig, ax = plt.subplots(figsize=figsize)
linestyle = "--"
ax.plot(
    xs,
    ys,
    marker=".",
    linestyle=linestyle,
    linewidth=0.7,
    label=df_name,
)

ax.set_xlabel("Bit-rate [bpp]")
ax.set_ylabel('psnr')
major_ticks = np.arange(0, 5, 0.5)
minor_ticks = np.arange(0, 5, 0.25)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.legend(loc="lower right")
ax.title.set_text("Rate-Distrotion Curves [RD]")
plt.show()
