import csv
import matplotlib.pyplot as plt

# Step 1
life_expectancy_data = []
with open("life_expectancy.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        life_expectancy_data.append(row)

# Step 2
life_expectancy_by_birth_data = []
with open("life_expectancy_by_birth.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        life_expectancy_by_birth_data.append(row)

# Step 3
overall_min_life_expectancy = float("inf")
overall_max_life_expectancy = float("-inf")
overall_min_year = 0
overall_max_year = 0
overall_max_country = ""
overall_min_country = ""
sum_life_expectancy = 0
count_countries = 0

# Step 4
for record in life_expectancy_data:
    country = record["Country"]
    year = int(record["Year"])
    life_expectancy = float(record["Life expectancy"])

    overall_min_life_expectancy = min(overall_min_life_expectancy, life_expectancy)
    overall_max_life_expectancy = max(overall_max_life_expectancy, life_expectancy)

    if life_expectancy < overall_min_life_expectancy:
        overall_min_life_expectancy = life_expectancy
        overall_min_year = year
        overall_min_country = country
    if life_expectancy > overall_max_life_expectancy:
        overall_max_life_expectancy = life_expectancy
        overall_max_year = year
        overall_max_country = country

    sum_life_expectancy += life_expectancy
    count_countries += 1

# Step 5
overall_average_life_expectancy = sum_life_expectancy / count_countries

# Step 6
print(
    f"The overall max life expectancy is: {overall_max_life_expectancy} from {overall_max_country} in {overall_max_year}"  # noqa: E501
)
print(
    f"The overall min life expectancy is: {overall_min_life_expectancy} from {overall_min_country} in {overall_min_year}"  # noqa: E501
)

# Step 7
while True:
    print("\nPlease choose an option:")
    print("a) Enter a specific year of interest.")
    print("b) Enter a specific country of interest.")
    print("c) Exit the program.")
    user_choice = input("Your choice: ")

    # Step 7b
    if user_choice == "a":
        year_of_interest = int(input("Enter a specific year of interest: "))
        year_min_life_expectancy = float("inf")
        year_max_life_expectancy = float("-inf")
        year_min_country = None
        year_max_country = None
        sum_year_life_expectancy = 0
        count_year_countries = 0

        for record in life_expectancy_by_birth_data:
            country = record["Country_Name"]
            years = [year for year in record.keys() if year.isnumeric()]
            expectancies = [float(record[year]) for year in years]

            if str(year_of_interest) in years:
                index = years.index(str(year_of_interest))
                life_expectancy = expectancies[index]

                year_min_life_expectancy = min(
                    year_min_life_expectancy, life_expectancy
                )
                year_max_life_expectancy = max(
                    year_max_life_expectancy, life_expectancy
                )

                if life_expectancy < year_min_life_expectancy:
                    year_min_life_expectancy = life_expectancy
                    year_min_country = country
                if life_expectancy > year_max_life_expectancy:
                    year_max_life_expectancy = life_expectancy
                    year_max_country = country

                sum_year_life_expectancy += life_expectancy
                count_year_countries += 1

        if count_year_countries > 0:
            avg_year_life_expectancy = sum_year_life_expectancy / count_year_countries
            print(
                f"Min life expectancy: {year_min_life_expectancy} ({year_min_country})"
            )
            print(
                f"Max life expectancy: {year_max_life_expectancy} ({year_max_country})"
            )
            print(f"Avg life expectancy: {avg_year_life_expectancy}")
        else:
            print("No data available for the specified year.")

    # Step 7c

    elif user_choice == "b":
        chosen_country = input("Enter a specific country of interest: ")

        chosen_country_records = [
            record
            for record in life_expectancy_data
            if record["country"] == chosen_country
        ]
        chosen_country_records = [
            record
            for record in life_expectancy_by_birth_data
            if record["Country_Name"] == chosen_country
        ]

        if chosen_country_records:
            chosen_country_min = min(
                chosen_country_records, key=lambda x: float(x["life_expectancy"])
            )
            chosen_country_max = max(
                chosen_country_records, key=lambda x: float(x["life_expectancy"])
            )

            chosen_country_min = min(
                chosen_country_records, key=lambda x: float(x[year])
            )
            chosen_country_max = max(
                chosen_country_records, key=lambda x: float(x[year])
            )

            country_life_expectancies = [
                float(record[year]) for record in chosen_country_records
            ]

            print(f"\nFor {chosen_country}:")
            print(
                f"The overall max life expectancy is {chosen_country_max['life_expectancy']} in {chosen_country_max['year']}"  # noqa: E501
            )
            print(
                f"The overall min life expectancy is {chosen_country_min['life_expectancy']} in {chosen_country_min['year']}"  # noqa: E501
            )

            country_life_expectancies = [
                float(record["life_expectancy"]) for record in chosen_country_records
            ]
            average_life_expectancy = sum(country_life_expectancies) / len(
                country_life_expectancies
            )
            print(
                f"The average life expectancy for {chosen_country} is {average_life_expectancy}"
            )

            # Additional data exploration and analysis
            # Example code to plot the life expectancy over the years for a specific country
            selected_country = "Afghanistan"
            years = []
            life_expectancies = []
            for record in life_expectancy_by_birth_data:
                if record["Country_Name"] == selected_country:
                    for year in range(1960, 2023):
                        years.append(year)
                        life_expectancy = float(record[str(year)])
                        life_expectancies.append(life_expectancy)

            plt.plot(years, life_expectancies)
            plt.xlabel("Year")
            plt.ylabel("Life Expectancy")
            plt.title(f"Life Expectancy Over the Years ({selected_country})")
            plt.show()

        # Point 2: Compare life expectancy between different regions or continents
        # Group countries by regions or continents, calculate average life expectancies, and compare them

        # Point 3: Analyze correlation between life expectancy and other factors
        # If additional datasets are available, analyze correlations between life expectancy and socioeconomic factors

        # Point 4: Detect outliers and anomalies
        # Examine the distribution of life expectancy values to identify outliers or countries with significant deviations

        # Point 5: Perform time series forecasting
        # Apply time series forecasting techniques to predict future life expectancy values based on historical data

        # Point 6: Conduct clustering analysis
        # Apply clustering algorithms to group countries based on life expectancy patterns and identify common characteristics

        # Point 7: Analyze life expectancy disparities
        # Calculate the difference in life expectancy between different groups of countries and analyze disparities

        else:
            print(f"No data available for {chosen_country}.")

    # Step 7d
    elif user_choice == "c":
        break

# Step 8
# End the program
