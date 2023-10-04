data = []

# Read the CSV file and load data into the list
with open("life_expectancy.csv") as file:
    next(file)  # skip header line
    for line in file:
        record = line.strip().split(",")  # split by comma
        data.append(record)

# Initialize variables and calculate overall statistics
overall_min_life_expectancy = float("inf")
overall_max_life_expectancy = float("-inf")
overall_min_year = 9999
overall_max_year = 0
overall_min_country = ""
overall_max_country = ""
sum_life_expectancy = 0
count_countries = 0

for record in data:
    if len(record) >= 4:
        print(record)
        entity, country, year, life_expectancy = record[:4]

        year = int(year)
        life_expectancy = float(life_expectancy)

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

overall_average_life_expectancy = (
    sum_life_expectancy / count_countries if count_countries > 0 else 0
)

# Prompt the user to enter a specific year of interest

year_of_interest = int(input("Enter the year of interest: "))

# Initialize variables for the specific year
year_min_life_expectancy = float("inf")
year_max_life_expectancy = float("-inf")
year_min_country = ""
year_max_country = ""
sum_year_life_expectancy = 0
count_year_countries = 0

# Calculate statistics for the specific year
for record in data:
    if len(record) >= 4:
        entity, country, year, life_expectancy = record[:4]

        year = int(year)
        life_expectancy = float(life_expectancy)

        if year != year_of_interest:
            continue

        if life_expectancy < year_min_life_expectancy:
            year_min_life_expectancy = life_expectancy
            year_min_country = country
        if life_expectancy > year_max_life_expectancy:
            year_max_life_expectancy = life_expectancy
            year_max_country = country

        sum_year_life_expectancy += life_expectancy
        count_year_countries += 1

year_average_life_expectancy = (
    sum_year_life_expectancy / count_year_countries if count_year_countries > 0 else 0
)


# Display the overall maximum and minimum life expectancies and their respective years and countries
print("The overall max life expectancy is: {:.3f}".format(overall_max_life_expectancy))
print("The overall min life expectancy is: {:.3f}".format(overall_min_life_expectancy))
