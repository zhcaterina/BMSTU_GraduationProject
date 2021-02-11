# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

'''
x = [1, 2, 4, 8, 16, 32, 64]
y = [0.110245,
0.195088,
0.366018,
0.710634,
1.485563,
2.825662,
5.59129]
fig, ax = plt.subplots()
ax.plot(x, y, color='r', linewidth=3, label=u'Время обработки')
plt.scatter(x, y)
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))

ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.set_xlabel(u'Объем текста, блок')
ax.set_ylabel(u'Время, мс')
plt.legend(borderpad=1)
plt.show()
'''
'''
x = [3, 40, 82, 164, 328]
y = [0.027921,
0.046917,
0.046589,
0.059152,
0.09585]
fig, ax = plt.subplots()
ax.plot(x, y, color='r', linewidth=3, label=u'Время обработки')
plt.scatter(x, y)
#ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))

#ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.set_xlabel(u'Объем словаря, количество слов')
ax.set_ylabel(u'Время, мс')
plt.legend(borderpad=1)
plt.show()
'''