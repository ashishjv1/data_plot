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

# for bitrate, psnr in read_json(directory, filename):
#     plt.plot(bitrate, psnr, color='skyblue')
#     plt.title('Lossy')
#     plt.xlabel('Bitrate')
#     plt.ylabel('PSNR')
#     plt.show()
#     plt.savefig(current_dir + '/results/lossy.png')
#     plt.clf()
import pandas as pd
df1 = pd.DataFrame.from_dict(dict_xs, orient='index')
df2 = pd.DataFrame.from_dict(dict_ys, orient='index')
df1 = df1.transpose()
df2 = df2.transpose()
df_name = df1.columns
xs = df1[:].values
# ys = df2.to_string(header=False)
ys = df2[:].values
print(xs)
print(ys)

# print(df1.head(), df2.head())
# linestyle = "--"
#
# plt.plot(xs, ys)
# plt.title('Lossy')
# plt.xlabel('Bitrate')
# plt.ylabel('PSNR')
# plt.show()

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
ax.grid()
ax.legend(loc="lower right")
ax.title.set_text("test")
plt.show()