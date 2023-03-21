from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """
This program displays the population by years of a selectd country
"""
    # opening file
    file = load("population_total.csv")

    # Extracting Data from contries
    france = file.loc[file['country'] == 'France']
    belgium = file.loc[file['country'] == 'Belgium']

    # setting x_plots for each contry
    x_france = france.columns[1:252]
    x_france = pd.to_numeric(x_france)
    x_belgium = belgium.columns[1:252]
    x_belgium = pd.to_numeric(x_belgium)

    # setting y_plots for each contry
    exp = {'k': 1e3, 'm': 1e6}
    y_france = france.iloc[0][1:252]
    y_france = [int(float(i[:-1]) * exp[i[-1].lower()]) for i in y_france]
    y_france = pd.DataFrame(y_france)
    y_belgium = belgium.iloc[0][1:252]
    y_belgium = [int(float(i[:-1]) * exp[i[-1].lower()]) for i in y_belgium]
    y_belgium = pd.DataFrame(y_belgium)

    # Setting ticks
    fig, ax = plt.subplots()
    plt.xticks(range(1800, 2051, 40))
    ax.set_yticks([0, 20000000, 40000000, 60000000, 80000000])
    ax.set_yticklabels(["0M", "20M", "40M", "60M", "80M"])

    # Setting the entire plot to show
    ax.plot(x_belgium, y_belgium, label='Belgium')
    ax.plot(x_france, y_france, color='green', label='France')
    ax.legend(loc='lower right')
    plt.title('Population Projections')
    plt.ylabel('Population')
    plt.xlabel('Year')
    plt.show()


if __name__ == "__main__":
    main()
