# List of salaries
salaries = [100, 300, 500, 1000, 1500, 3000, 4000, 5000, 6000, 7000, 10000, 15000, 25000]  # Example list of monthly salaries

# Tax rates input for Virginia
statetax = 0.0472

# Standard tax rates
sstax = .062
medicaretax = .0145


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


# Iterate over the list of salaries and calculate taxes and take-home pay for each
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

    # Display the results for each salary
    print(f"For a monthly salary of ${salary:.2f}:")
    print(f"  Monthly take-home pay will be: ${monthly_takehome:.2f}")
    print(f"  Annual take-home pay will be: ${annual_takehome:.2f}\n")
