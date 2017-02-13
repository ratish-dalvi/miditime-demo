import pandas as pd
import matplotlib
from datetime import datetime
import seaborn as sns
from miditime.miditime import MIDITime

# Read data
df = pd.read_excel("data/data_akbilgic.xlsx", header=[0, 1])

# describe
print "Dataset size: %s rows, %s columns" % df.shape

# Get time series for USD BASED ISE
ts = df[("USD BASED", "ISE")]

# plot time series and save the figure
fig = sns.plt.figure(figsize=(12, 8))
sns.plt.plot(ts, "-o")
sns.plt.xlabel("Date")
sns.plt.ylabel("USD based ISE")
sns.plt.title("Istanbul Stock Exchange")
fig.savefig("timeseries_plot.png")
sns.plt.clf()
sns.plt.close()
sns.plt.show()
