import scipy as sp

import matplotlib.pyplot as plt

data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")
#print(data[:10])
x = data[:,0]
y = data[:,1]
#print(y)
x= x[~sp.isnan(y)]
y = y[~sp.isnan(y)]
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")

plt.xticks([w*7*24 for w in range(10)],#list
 ['week %i'%w for w in range(10)])#names in the axis


fp1, res1, rank1, sv1, rcond1 = sp.polyfit(x, y, 1, full=True)

f1 = sp.poly1d(fp1)
fx = sp.linspace(0,x[-1], 1000) # generate X-values for plotting
plt.plot(fx, f1(fx), linewidth=4,color='green')
plt.legend(["d=%i" % f1.order], loc="upper left")
plt.autoscale(tight=True)
plt.grid()
plt.show()