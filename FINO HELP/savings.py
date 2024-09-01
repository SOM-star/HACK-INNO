import math


def calculate_monthly_saving_amount(years, goal_saving, monthly_salary):
    # Fixed annual interest rate
    annual_interest_rate = 12.0

    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12.0

    # Convert years to months
    months = years * 12

    # Calculate the denominator part of the formula for monthly compounding
    denominator = math.pow(1 + monthly_interest_rate / 100, months) - 1

    # Calculate the required monthly saving
    monthly_saving_required = goal_saving * (monthly_interest_rate / 100) / denominator

    # Calculate the percentage of the monthly salary to be saved
    saving_percentage = (monthly_saving_required / monthly_salary) * 100

    # Calculate the actual monthly saving amount based on the saving percentage
    monthly_saving_amount = (saving_percentage / 100) * monthly_salary

    return monthly_saving_amount


