import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    # create a scatter plot where the points on the x-axis come from x(years) 
    # and the points on the y-axis come from y (sea level data).
    plt.scatter(x, y)
    # Create first line of best fit
    # calculate the linear regression for the data in x and y. The result, which includes the slope and 
    # intercept of the best fit line, is stored in the variable line_1
    line_1 = linregress(x,y)
    # Create series in range 1880 to 2050
    x_data = pd.Series([i for i in range(1880,2051)])
    # Use the slope and intercept from line_1 to calculate sea level for year (x_data)
    y_data =  line_1.intercept + line_1.slope * x_data
    plt.plot(x_data, y_data, "r")

    # Create second line of best fit
    # only use data from the year 2000+
    df_2 = df.loc[df['Year'] >= 2000]
    x_2 = df_2['Year']
    y_2 = df_2['CSIRO Adjusted Sea Level']
    # calculate linear regression using recent years and recent sea levels
    line_2 = linregress(x_2,y_2)
    # create series in range 2000 to 2050
    x_data_2 = pd.Series([i for i in range(2000,2051)])
    # calculates predicted sea level values (y_pred2) for each year in x_data_2 using the slope and intercept 
    # from line_2 (which represents the recent trend)
    y_data_2 =  line_2.intercept + line_2.slope * x_data_2 
    plt.plot(x_data_2, y_data_2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
