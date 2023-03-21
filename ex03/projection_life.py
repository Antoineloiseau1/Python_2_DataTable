from load_csv import load
import matplotlib.pyplot as plt


def main():
	life_exp = load("life_expectancy_years.csv")
	incomes = load ("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
	first = life_exp.loc[life_exp["1900"]]
	print(first)


if __name__ == "__main__":
	main()