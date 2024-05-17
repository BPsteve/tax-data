import csv
import json
import datetime

# List of salaries
salaries = [100, 300, 500, 1000, 1500, 3000, 4000, 5000, 6000, 7000, 10000, 15000, 25000]

# Set the state tax rate for Virginia
statetax = 0.0472

# Standard tax rates
sstax = 0.062
medicaretax = 0.0145

# Function to calculate federal tax based on salary
def calculate_fed_tax(salary):
    if salary <= 317:
        return 0.00 + 0.10 * salary
    elif 317 < salary <= 1125:
        return 31.70 + 0.12 * (salary - 317)
    elif 1125 < salary <= 3606:
        return 116.14 + 0.22 * (salary - 1125)
    elif 3606 < salary <= 7333:
        return 633.50 + 0.24 * (salary - 3606)
    elif 7333 < salary <= 13710:
        return 1508.54 + 0.32 * (salary - 7333)
    elif 13710 < salary <= 17325:
        return 3617.02 + 0.35 * (salary - 13710)
    else:
        return 4863.47 + 0.37 * (salary - 17325)

# Prepare the data for writing to files
results = []

for salary in salaries:
    # Calculate the state tax
    stax = salary * statetax

    # Calculate the federal tax
    ftax = calculate_fed_tax(salary)

    # Calculate other taxes
    soctax = salary * sstax
    mtax = salary * medicaretax

    # Find total taxes
    total_taxes = stax + ftax + soctax + mtax

    # Calculate the take-home on an annual basis
    monthly_takehome = salary - total_taxes
    annual_takehome = monthly_takehome * 12

    # Append the results to the list
    results.append({
        "Salary": salary,
        "Monthly Take-home": round(monthly_takehome, 2),
        "Annual Take-home": round(annual_takehome, 2)
    })

# Ask the user for the desired output format
output_format = input("Enter the desired output format (csv, json, both): ").strip().lower()

# Generate a timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

if output_format == 'csv' or output_format == 'both':
    # Write the results to a CSV file with a timestamp
    csv_filename = f'salary_takehome_{timestamp}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["Salary", "Monthly Take-home", "Annual Take-home"])
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    print(f"Results have been written to '{csv_filename}'.")

if output_format == 'json' or output_format == 'both':
    # Write the results to a JSON file with a timestamp
    json_filename = f'salary_takehome_{timestamp}.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(results, json_file, indent=4)
    print(f"Results have been written to '{json_filename}'.")

if output_format not in ['csv', 'json', 'both']:
    print("Invalid output format. Please enter 'csv', 'json', or 'both'.")
