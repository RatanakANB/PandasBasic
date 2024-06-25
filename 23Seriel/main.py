import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Part 1: Creating and Manipulating Pandas Series
# 1.1
series1 = pd.Series([5, 10, 15, 20, 25])
print(series1)

# 1.2
marvel_heroes = ['Hulk', 'Black Widow', 'Doctor Strange', 'Hawkeye', 'Scarlet Witch']
series2 = pd.Series(marvel_heroes)
print(series2)

# 1.3
array = np.arange(50, 61)
series3 = pd.Series(array)
print(series3)

# 1.4
np.random.seed(42)
random_series = pd.Series(np.random.randint(1, 101, size=8))
print(random_series)

# 1.5
single_value_series = pd.Series(7)
print(single_value_series)

# 1.6
custom_index_series = pd.Series([100, 200, 300, 400, 500], index=['a', 'b', 'c', 'd', 'e'])
print(custom_index_series)

# Part 2: Working with Date Ranges
# 2.1
date_range = pd.date_range('2022-01-01', '2022-01-07')
print(date_range)

# Adding two more heroes to match the date range length
marvel_heroes.extend(['Iron Man', 'Thor'])
# 2.2
marvel_series_with_dates = pd.Series(marvel_heroes, index=date_range)
print(marvel_series_with_dates)

# Part 3: Basic Statistical Operations
# 3.1
np.random.seed(7)
data = np.random.randint(1, 100, 10)
statistics_series = pd.Series(data)

print("Count:", statistics_series.count())
print("Sum:", statistics_series.sum())
print("Mean:", statistics_series.mean())
print("Median:", statistics_series.median())
print("Mode:", statistics_series.mode())
print("Standard Deviation:", statistics_series.std())
print("Minimum:", statistics_series.min())
print("Maximum:", statistics_series.max())
print("Absolute Values:", statistics_series.abs())
print("Product:", statistics_series.prod())
print("Cumulative Sum:", statistics_series.cumsum())
print("Cumulative Product:", statistics_series.cumprod())

# Part 4: Plotting with Matplotlib
# 4.1
plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
plt.show()

# 4.2
x = range(100)
y = [value**2 for value in x]

plt.plot(x, y, linewidth=3, color='blue')
plt.title('Square Numbers')
plt.ylabel('y - values squared')
plt.xlabel('x - values')
plt.show()

# 4.3
days_in_year = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
plt.bar(range(len(days_in_year)), days_in_year)
plt.show()

# Part 5: Population Analysis and Visualization
# 5.1 Convert dictionaries to Series
population_2020 = {
    'New York': 8336817, 'Los Angeles': 3979576, 'Chicago': 2693976, 'Houston': 2320268,
    'Phoenix': 1680992, 'Philadelphia': 1584203, 'San Antonio': 1547253, 'San Diego': 1423851,
    'Dallas': 1341075, 'San Jose': 1021795
}

population_2021 = {
    'New York': 8398748, 'Los Angeles': 3980404, 'Chicago': 2716000, 'Houston': 2328000,
    'Phoenix': 1682500, 'Philadelphia': 1588000, 'San Antonio': 1550000, 'San Diego': 1430000,
    'Dallas': 1350000, 'San Jose': 1030000
}

city_area = {
    'New York': 783.8, 'Los Angeles': 1214, 'Chicago': 589, 'Houston': 1700,
    'Phoenix': 1340, 'Philadelphia': 347, 'San Antonio': 1194, 'San Diego': 964,
    'Dallas': 887, 'San Jose': 467
}

s_2020 = pd.Series(population_2020)
s_2021 = pd.Series(population_2021)
s_area = pd.Series(city_area)

# 5.2 Calculate and display population change
growth = s_2021 - s_2020
print('<Increase or Decrease in the population>')
print(growth)

# 5.3 Bar graph for population change
plt.figure(figsize=(10, 6))
plt.barh(growth.index, growth.values, color='skyblue')
plt.xlabel('Population Change')
plt.title('Population Change from 2020 to 2021')
plt.xticks(rotation='vertical', size=8)
plt.show()

# 5.4 Calculate the population density for each city
population_density = s_2020 / s_area
print('<Population Density>')
print(population_density)

# 5.5 Bar graph for population density
plt.figure(figsize=(10, 6))
plt.barh(population_density.index, population_density.values, color='orange')
plt.xlabel('Population Density (people per sq. km)')
plt.title('Population Density in 2020')
plt.xticks(rotation='vertical', size=8)
plt.show()

# 5.6 Print the city with the maximum and minimum population densities
max_density_city = population_density.idxmax()
max_density_value = population_density.max()
min_density_city = population_density.idxmin()
min_density_value = population_density.min()

print(f'The city with the maximum population density is {max_density_city} with {max_density_value:.2f} people per sq. km.')
print(f'The city with the minimum population density is {min_density_city} with {min_density_value:.2f} people per sq. km.')
