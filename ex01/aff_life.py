from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    file = load("life_expectancy_years.csv")
    file = file.loc[file['country'] == 'France']
    x = file.columns[1:]
    y = file.iloc[0][1:]
    x = pd.to_numeric(x)
    plt.xticks(range(1800, 2081, 40))
    plt.yticks(range(30, 101, 10))
    plt.plot(x, y)
    plt.title('France Life Expectancy Projections')
    plt.ylabel('Life expectancy')
    plt.xlabel('Year')
    plt.show()


if __name__ == "__main__":
    main()
