import math

print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
user_need = "a"  # input()

if user_need == "n":
    print("Enter the loan principal:")
    loan_principal = int(input())
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    print("Enter the loan interest:")
    interest = float(input())

    i = interest / 1200

    months = math.ceil(math.log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i))

    if months == 1:
        print(f"It will take {months} month to repay the loan")
    elif months < 12:
        print(f"It will take {round(months)} months to repay the loan")
    elif months == 12:
        print(f"It will take 1 year to repay the loan")
    elif round(months) % 12 == 0:
        years = int((round(months) / 12))
        print(f"It will take {years} years to repay the loan")
    elif round(months) < 24:
        months = round(months) - 12
        print(f"It will take 1 year and {months} months to repay the loan")
    else:
        years = int((round(months) / 12))
        months = round(months) - 12 * years
        print(f"It will take {years} years and {months} months to repay the loan")

elif user_need == "a":
    print("Enter the loan principal:")
    loan_principal = 1000000  # int(input())
    print("Enter the number of periods:")
    months = 8  # int(input())
    print("Enter the loan interest:")
    interest = 9.8  # float(input())

    i = interest / 1200

    monthly_payment = loan_principal * ((i * pow((1 + i), months)) / (pow((1 + i), months) - 1))

    overpayment = math.ceil(monthly_payment) * months - loan_principal
    print(f"Your annuity payment = {math.ceil(monthly_payment)}!")
    print(f"Overpayment = {overpayment}")
    # different calculation method of the monthly payment from the previous stage
    # if math.ceil(monthly_payment) > 0:
    #     # monthly_payment = round(monthly_payment) + 1
    #     monthly_payment = math.ceil(monthly_payment)
    #     last_payment = loan_principal - (monthly_payment * (months - 1))
    #     print(f"Your monthly payment = {monthly_payment} and the last payment = {last_payment}!")
    # else:
    #     print(f"Your monthly payment = {int(monthly_payment)}!")
elif user_need == "p":
    print("Enter the annuity payment:")
    monthly_payment = float(input())
    print("Enter the number of periods:")
    months = int(input())
    print("Enter the loan interest:")
    interest = float(input())

    i = interest / 1200

    loan_principal = monthly_payment / ((i * pow((1 + i), months)) / (pow((1 + i), months) - 1))

    print(f"Your loan principal = {round(loan_principal)}!")
