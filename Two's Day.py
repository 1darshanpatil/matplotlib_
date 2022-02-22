import calendar as cl
import matplotlib.pyplot as plt
cl.weekday(2022,2,22)
yr = [y for y in range(1000, 9099)]
twoday = [years for years in yr if (cl.weekday(years, 2, 22) == 1 and str(years)[2:] == "22") ]
print(twoday)
bulian= [0 if (i not in twoday) else 1 for i in yr]
if bulian.count(0) == len(yr) - len(twoday):
    plt.scatter(yr, bulian, s = 3)
    plt.show()
