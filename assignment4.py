import numpy as np
import csv
import matplotlib.pyplot as plt


###########################################
# Problem 1
###########################################

def mcev(fun, n_samples, mu, sigma):
    pass


###########################################
# Problem 2
###########################################

def plot_total_volume_histogram(volume_traded):
    plt.clf() # reset the plot

    """Your code here. You need to compute the total volume sold for each stock during the entire time period first.
    Plot those in a histogram with 10 bins.
    Then put the title and axis labels. 
    Then save into a file total_volume_hist.png"""

###########################################
# Problem 3
###########################################

def plot_closing_prices(stocks, dates, closing_price):
    plt.clf() # reset the plot

    for stock in ["IBM", "INTC", "MSFT"]:
        stock_idx = stocks.index(stock)
        ## Your code here. Plot the stock's closing price over time ##

    """Your code here. Put the title, axis labels, tick marks, and legend. Then save into a file closing_prices.png"""


###########################################
# Testing Code
###########################################
def load_data(filename):
    stocks = []
    dates = []

    closing_price = np.empty((30, 25))
    volume_traded = np.empty((30, 25))

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        curr_stock = ""
        row_idx = -1
        col_idx = 0
        for row in reader:
            if row[0] not in stocks:
                stocks.append(row[0])
            if row[1] not in dates:
                dates.append(row[1])

            if row[0] != curr_stock:
                curr_stock = row[0]
                row_idx += 1
                col_idx = 0

            print(curr_stock, row_idx, col_idx)
            closing_price[row_idx, col_idx] = float(row[2])
            volume_traded[row_idx, col_idx] = int(row[3])
            col_idx += 1

    return stocks, dates, closing_price, volume_traded


if __name__ == "__main__":
    def fun(x):
        return x ** 2


    # # plot_samples()
    print(mcev(fun, 100000, 0.0, 1.0))

    # stocks is a list of stock names in alphabetical order
    # dates is the list of dates contained in this dataset in order, as strings
    # closing_price is an SxD array, with element s,d holding the closing price in US dollars for stock s on date d
    # volume_traded is an SxD array, with element s,d holding the volume of trades
    #   that occured for stock s during the week ending on date d
    stocks, dates, closing_price, volume_traded = load_data("dow_jones.csv")

    plot_closing_prices(stocks, dates, closing_price)
    plot_total_volume_histogram(volume_traded)