from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Display a scatter of life expectancy of a country \
by its gross national product of a given year"""
    life_exp = load("life_expectancy_years.csv")
    incomes = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    try:
        incomes = incomes[["country", "1900"]]
        life_exp = life_exp[["country", "1900"]]
        if (not incomes["country"].equals(life_exp["country"])):
            raise ValueError("countries are not equals")
    except TypeError as msg:
        print("TypeError:", msg)
        exit(-1)
    except AttributeError as msg:
        print("AttributeError:", msg)
        exit(-1)
    except KeyError as msg:
        print("KeyError:", msg)
        exit(-1)
    except IndexError as msg:
        print("IndexError:", msg)
        exit(-1)
    except ValueError as msg:
        print("ValueError:", msg)
        exit(-1)

    fig, ax = plt.subplots()
    plt.xscale("log")
    plt.xlim(300, 11000)
    xticks = [300, 1000, 10000]
    xlabel = ["300", "1k", "10k"]
    plt.xticks(xticks, xlabel)
    plt.scatter(incomes['1900'], life_exp['1900'])
    plt.title('1900')
    plt.ylabel('Life expectancy')
    plt.xlabel('Gross domestic product')
    plt.show()


if __name__ == "__main__":
    main()
