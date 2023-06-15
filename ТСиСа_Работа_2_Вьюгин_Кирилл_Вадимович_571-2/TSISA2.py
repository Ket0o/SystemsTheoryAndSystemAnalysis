"""Импортируем нужные библиотеки"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
"""graphviz python"""

"""Для отображения графика"""
matplotlib.use('TkAgg')

"""Функция поиска минимального расстояния между точками (1 сосед)"""
def minDistance1(GPD, debt, populationDensity, X, Y, Z):
    minimum = np.sqrt(((X[0] - GPD) * (X[0] - GPD)) +
                      ((Y[0] - debt) * (Y[0] - debt)) +
                      ((Z[0] - populationDensity) * (Z[0] - populationDensity)))

    for i in range(X.size):
        value = np.sqrt(((X[i] - GPD) * (X[i] - GPD)) +
                        ((Y[i] - debt) * (Y[i] - debt)) +
                        ((Z[i] - populationDensity) * (Z[i] - populationDensity)))

        minimum = value if value < minimum else minimum
    return minimum

"""Функция поиска минимального расстояния между точками (3 соседа)"""
def minDistance3(GPD, debt, populationDensity, X1, Y1, Z1, X2, Y2, Z2):
    minimum = np.array([])
    valueOfDeveloped = np.array([])

    for i in range(X1.size):
        minimum = np.append(minimum, np.sqrt(((X1[i] - GPD) * (X1[i] - GPD)) +
                                             ((Y1[i] - debt) * (Y1[i] - debt)) +
                                             ((Z1[i] - populationDensity) * (Z1[i] - populationDensity))))
        valueOfDeveloped = np.append(valueOfDeveloped, "Развитая")

    for i in range(X2.size):
        minimum = np.append(minimum, np.sqrt(((X2[i] - GPD) * (X2[i] - GPD)) +
                                             ((Y2[i] - debt) * (Y2[i] - debt)) +
                                             ((Z2[i] - populationDensity) * (Z2[i] - populationDensity))))
        valueOfDeveloped = np.append(valueOfDeveloped, "Развивающаяся")

    indices = minimum.argsort()
    valueOfDeveloped = valueOfDeveloped[indices][0:3]

    if (np.count_nonzero(valueOfDeveloped == "Развитая") > np.count_nonzero(valueOfDeveloped == "Развивающаяся")):
        return "Развитая"
    else:
        return "Развивающаяся"

"""Данные на вход"""
countryTypes = np.array(["Развитая", "Развивающаяся", "Развивающаяся", "Развитая", "Развитая", "Развивающаяся", "Развитая", "Развивающаяся"])
ountrysGDP = np.array([0.305, 0.217, 0.285, 3.306, 0.729, 2.024, 1.477, 0.354])
CountrysDebt = np.array([0.627, 0.028, 0.043, 5.624, 0.310, 4.07, 0.396, 0.074])
populationDensityOfCountry = np.array([128, 80, 29.8, 230, 100, 23.6, 8.4, 40])

"""Развитые"""
X1 = np.array([])
Y1 = np.array([])
Z1 = np.array([])

"""Развивающиеся"""
X2 = np.array([])
Y2 = np.array([])
Z2 = np.array([])

"""Отбираем страны на развитые и на развивающиеся"""
for i in range(len(countryTypes)):
    if countryTypes[i] == "Развитая":
        X1 = np.append(X1, ountrysGDP[i])
        Y1 = np.append(Y1, CountrysDebt[i])
        Z1 = np.append(Z1, populationDensityOfCountry[i])
    else:
        X2 = np.append(X2, ountrysGDP[i])
        Y2 = np.append(Y2, CountrysDebt[i])
        Z2 = np.append(Z2, populationDensityOfCountry[i])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

"""Данные стран с неизвестными типами"""
countryTypes_unknown = np.array([9, 10])
GPD_unknown = np.array([14.624, 1.220])
debt_unknown = np.array([16.014, 1.376])
populationDensity_unknown = np.array([32, 2.8])

print("При k = 1:")

"""Проверяем каждую страну на принадлежность к типам ("Развитая", "Развивающаяся") при (k = 1)"""
for i in range(2):
    developed = minDistance1(GPD_unknown[i], debt_unknown[i], populationDensity_unknown[i], X1, Y1, Z1)
    developing = minDistance1(GPD_unknown[i], debt_unknown[i], populationDensity_unknown[i], X2, Y2, Z2)
    ax.scatter(GPD_unknown[i],debt_unknown[i],populationDensity_unknown[i],color='blue')

    if developed < developing:
        print(str(countryTypes_unknown[i]) + " - развитая")
    else:
        print(str(countryTypes_unknown[i]) + " - развивающаяся")

print("При k = 3:")

"""Проверяем каждую страну на принадлежность к типам ("Развитая", "Развивающаяся") при (k = 3)"""
for i in range(2):
    answer = minDistance3(GPD_unknown[i], debt_unknown[i], populationDensity_unknown[i], X1, Y1, Z1, X2, Y2, Z2)

    if (answer == "Развитая"):
        print(str(countryTypes_unknown[i]) + " - развитая")
    else:
        print(str(countryTypes_unknown[i]) + " - развивающаяся")

"""Выводим график"""
ax.scatter(X1,Y1,Z1,color='red')
ax.scatter(X2,Y2,Z2,color='green')
plt.legend(handles=[mpatches.Patch(color='red', label='развитая'),
                    mpatches.Patch(color='green', label='развивающаяся'),
                    mpatches.Patch(color='blue', label='Неизвестный объект')])
plt.show()