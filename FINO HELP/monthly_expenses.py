def distribution_of_salary_rural(salary):
    housing = (salary * 10) / 100
    food = (salary * 15) / 100
    transportation = (salary * 5) / 100
    healthcare = (salary * 15) / 100
    emergency_fund = (salary * 5) / 100
    retirement_savings = (salary * 5) / 100
    other_investments = (salary * 10) / 100
    debt_repayment = (salary * 10) / 100
    insurance = (salary * 5) / 100
    education = (salary * 10) / 100
    agricultural_inputs_and_livelihood_investments = (salary * 10) / 100

    return {
        "Housing": housing,
        "Food": food,
        "Transportation": transportation,
        "Healthcare": healthcare,
        "Emergency Fund": emergency_fund,
        "Retirement Savings": retirement_savings,
        "Other Investments": other_investments,
        "Debt Repayment": debt_repayment,
        "Insurance": insurance,
        "Education": education,
        "Agricultural Inputs and Livelihood Investments": agricultural_inputs_and_livelihood_investments
    }

def salary_calculator_urban(salary):

    # Calculate expenses based on percentages
    budget_breakdown = {
        "Food": round(salary * 0.11, 2),
        "Transportation": round(salary * 0.14, 2),
        "Housing": round(salary * 0.30, 2),
        "Healthcare": round(salary * 0.10, 2),
        "Shopping": round(salary * 0.07, 2),
        "Miscellaneous": round(salary - (salary * (0.11 + 0.14 + 0.30 + 0.10 + 0.07)), 2)
    }

    return budget_breakdown



