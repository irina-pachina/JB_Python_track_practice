# loan calculator can compute differentiated payments, annuity payment, monthly payments for every month and overpayment,
# loan principal and period to repay a loan
# program uses command-line arguments:
# python loan_calculator_cli.py --type=diff --principal=1000000 --periods=10 --interest=10
# python loan_calculator_cli.py --type=annuity --principal=1000000 --periods=60 --interest=10
# python loan_calculator_cli.py --type=annuity --payment=8722 --periods=120 --interest=5.6
# python loan_calculator_cli.py --type=annuity --principal=500000 --payment=23000 --interest=7.8

import argparse
import sys
import math

parser = argparse.ArgumentParser()

parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if args.type is None or args.type not in ["annuity", "diff"]:
    print("Incorrect parameters")
elif args.payment is not None and args.type == "diff":
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
elif len(sys.argv) < 5:
    print("Incorrect parameters")
elif args.interest is not None and float(args.interest) < 0:
    print("Incorrect parameters")
elif args.payment is not None and float(args.payment) < 0:
    print("Incorrect parameters")
elif args.periods is not None and int(args.periods) < 0:
    print("Incorrect parameters")
elif args.principal is None:
    monthly_payment = float(args.payment)
    months = int(args.periods)
    interest = float(args.interest)

    i = interest / 1200

    loan_principal = monthly_payment / ((i * pow((1 + i), months)) / (pow((1 + i), months) - 1))

    print(f"Your loan principal = {round(loan_principal)}!")
elif args.principal is not None and int(args.principal) < 0:
    print("Incorrect parameters")
elif args.type == "annuity" and args.payment is None:
    loan_principal = int(args.principal)
    months = int(args.periods)
    interest = float(args.interest)

    i = interest / 1200

    monthly_payment = loan_principal * ((i * pow((1 + i), months)) / (pow((1 + i), months) - 1))
    overpayment = math.ceil(monthly_payment) * months - loan_principal
    print(f"Your annuity payment = {math.ceil(monthly_payment)}!")
    print(f"Overpayment = {overpayment}")
elif args.type == "diff":
    loan_principal = int(args.principal)
    months = int(args.periods)
    interest = float(args.interest)

    i = interest / 1200
    paid = 0
    for x in range(1, months + 1):
        monthly_payment = math.ceil(loan_principal / months + i * (loan_principal - ((loan_principal * (x - 1)) / months)))
        paid += monthly_payment
        print(f"Month {i}: payment is {monthly_payment}")
    print()
    overpayment = paid - loan_principal
    print(f"Overpayment = {overpayment}")
elif args.payment is not None:
    loan_principal = int(args.principal)
    monthly_payment = float(args.payment)
    interest = float(args.interest)

    i = interest / 1200

    months = math.ceil(math.log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i))

    overpayment = monthly_payment * months - loan_principal

    if months == 1:
        print(f"It will take {months} month to repay the loan!")
        print(f"Overpayment = {overpayment}")
    elif months < 12:
        print(f"It will take {round(months)} months to repay the loan!")
        print(f"Overpayment = {overpayment}")
    elif months == 12:
        print(f"It will take 1 year to repay the loan!")
        print(f"Overpayment = {overpayment}")
    elif round(months) % 12 == 0:
        years = int((round(months) / 12))
        print(f"It will take {years} years to repay the loan!")
        print(f"Overpayment = {overpayment}")
    elif round(months) < 24:
        months = round(months) - 12
        print(f"It will take 1 year and {months} months to repay the loan!")
        print(f"Overpayment = {overpayment}")
    else:
        years = int((round(months) / 12))
        months = round(months) - 12 * years
        print(f"It will take {years} years and {months} months to repay the loan!")
        print(f"Overpayment = {overpayment}")
