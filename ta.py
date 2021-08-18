import numpy
import talib
from numpy import genfromtxt

my_data = genfromtxt('5minutes.csv', delimiter=',')
#print(my_data)

close = my_data[:,4]

# close = numpy.random.random(100)
#
# moving_average = talib.SMA(close, timeperiod=10)
# #print(moving_average)
#
rsi = talib.RSI(close)
print(rsi)