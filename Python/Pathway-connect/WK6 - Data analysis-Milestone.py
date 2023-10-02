print("\n~~~ Data Analysis ~~~")
print("~~~ Milestone ~~~\n")
print("Welcome to this data analysis program")
print("*" * 40)


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
        entity = record[0]
        country = record[1]
        year = int(record[2])
        life_expectancy = float(record[3])

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

if count_countries > 0:
    overall_average_life_expectancy = sum_life_expectancy / count_countries
else:
    overall_average_life_expectancy = 0

# Prompt the user to enter a specific year of interest
print()
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
        year = int(record[2])
        if year != year_of_interest:
            continue
        country = record[0]
        life_expectancy = float(record[3])

        if life_expectancy < year_min_life_expectancy:
            year_min_life_expectancy = life_expectancy
            year_min_country = country
        if life_expectancy > year_max_life_expectancy:
            year_max_life_expectancy = life_expectancy
            year_max_country = country

        sum_year_life_expectancy += life_expectancy
        count_year_countries += 1

# Calculate average life expectancy for the specific year
if count_year_countries > 0:
    year_average_life_expectancy = sum_year_life_expectancy / count_year_countries
else:
    year_average_life_expectancy = 0

# Display the overall maximum and minimum life expectancies and their respective years and countries
print(
    "The overall max life expectancy is: {:.3f} from {} in {}".format(
        overall_max_life_expectancy, overall_max_country, overall_max_year
    )
)
print(
    "The overall min life expectancy is: {:.3f} from {} in {}".format(
        overall_min_life_expectancy, overall_min_country, overall_min_year
    )
)

# Display the average life expectancy, maximum, and minimum life expectancies for the specific year
print("\nFor the year {}:".format(year_of_interest))
print(
    "The max life expectancy is: {:.3f} from {}.".format(
        year_max_life_expectancy, year_max_country
    )
)
print(
    "The min life expectancy is: {:.3f} from {}.".format(
        year_min_life_expectancy, year_min_country
    )
)
print("The average life expectancy is: {:.3f}".format(year_average_life_expectancy))
