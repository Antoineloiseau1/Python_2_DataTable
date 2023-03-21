from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """
This program displays the population by years of a selected country
"""
    # opening file
    file = load("population_total.csv")

    # Extracting Data from contries
    first = file.loc[file['country'] == 'France']
    second = file.loc[file['country'] == 'Belgium']

    # setting x_plots for each contry
    first_name = first.iloc[0][0]
    second_name = second.iloc[0][0]
    x_first = first.columns[1:252]
    x_first = pd.to_numeric(x_first)
    x_second = second.columns[1:252]
    x_second = pd.to_numeric(x_second)

    # setting y_plots for each contry
    exp = {'K': 1e3, 'M': 1e6, 'B': 1e9}
    y_first = first.iloc[0][1:252]
    y_first = [int(float(i[:-1]) * exp.get(i[-1], 1)) for i in y_first]
    y_first = pd.DataFrame(y_first)
    y_second = second.iloc[0][1:252]
    y_second = [int(float(i[:-1]) * exp.get(i[-1], 1)) for i in y_second]
    y_second = pd.DataFrame(y_second)

    # Setting ticks
    fig, ax = plt.subplots()
    plt.xticks(range(1800, 2051, 40))
    max_value = max(int(y_first.max()), int(y_second.max()))
    if (max_value > 1e9):
        step = 200000000
    else:
        step = 20000000
    yticks = (range(0, max_value, step))
    ylabels = [f"{i/1e6:.0f}M" for i in yticks]
    plt.yticks(yticks, ylabels)

    # Setting the entire plot to show
    ax.plot(x_second, y_second, label=second_name)
    ax.plot(x_first, y_first, color='green', label=first_name)
    ax.legend(loc='lower right')
    plt.title('Population Projections')
    plt.ylabel('Population')
    plt.xlabel('Year')
    plt.show()


if __name__ == "__main__":
    main()
