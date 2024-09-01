from savings import calculate_monthly_saving_amount

def Retier_funds(salary, time, monthly_exp):
    year_exp = monthly_exp*20

    save = calculate_monthly_saving_amount(years=time,monthly_salary=salary,goal_saving=year_exp)
    return save
