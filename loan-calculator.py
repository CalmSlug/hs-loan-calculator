import math
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type")
    parser.add_argument("--principal", type=float)
    parser.add_argument("--payment", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    args = parser.parse_args()
    
    if args.type == args.principal == args.payment == args.periods == args.interest == None:
        print("What do you want to calculate?")
        print('type "n" for number of monthly payments,')
        print('type "a" for annuity monthly payment amount,')
        print('type "p" for loan principal,')
        print('type "d" for differentiated payments:')
        user_input = input()
        loan_data(user_input)
    
    else:
        parser_check(args.type, args.principal, args.payment, args.periods, args.interest)


def parser_check(type, principal, payment, periods, interest):
    
    if type != "diff" and type != "annuity":
        print("Incorrect parameters")
    
    elif type == "diff" and payment == True:
        print("Incorrect parameters")
    
    elif interest == None:
        print("Incorrect parameters")
    
    elif True == principal < 0 or True == payment < 0 or True == periods < 0 or True == interest < 0:
        print("Incorrect parameters")
    
    elif type == "annuity" and periods == None:
        calc("n", principal, payment, interest)
    
    elif type == "annuity" and payment == None:
        calc("a", principal, periods, interest)
    
    elif type == "annuity" and principal == None:
        calc("p", payment, periods, interest)
    
    elif type == "diff" and payment == None:
        calc("d", principal, periods, interest)
    
    else:
        print("Incorrect parameters")


def loan_data(skip):
    
    if skip == "n":
        print("Enter the loan principal:")
        loan = int(input())
        print("Enter the monthly payment:")
        payment = float(input())
        print("Enter the loan interest:")
        interest = float(input())
        calc(skip, loan, payment, interest)
    
    elif skip == "a":
        print("Enter the loan principal:")
        loan = int(input())
        print("Enter the number of periods:")
        n_months = int(input())
        print("Enter the loan interest:")
        interest = float(input())
        calc(skip, loan, n_months, interest)
    
    elif skip == "p":
        print("Enter the monthly payment:")
        payment = float(input())
        print("Enter the number of periods:")
        n_months = int(input())
        print("Enter the loan interest:")
        interest = float(input())
        calc(skip, payment, n_months, interest)
    
    elif skip == "d":
        print("Enter the loan principal:")
        loan = int(input())
        print("Enter the number of periods:")
        n_months = int(input())
        print("Enter the loan interest:")
        interest = float(input())
        calc(skip, loan, n_months, interest)


def calc(skip, arg1, arg2, arg3):
    
    if skip == "n":
        nom_interest = arg3 / (12 * 100)
        n_months = math.ceil(math.log(arg2 / (arg2 - nom_interest * arg1), 1 + nom_interest))
        overpayment = round(arg2 * n_months - arg1)
        result(skip, n_months, overpayment)
    
    elif skip == "a":
        nom_interest = arg3 / (12 * 100)
        payment = math.ceil(arg1 * ((nom_interest * ((1 + nom_interest) ** arg2)) / (((1 + nom_interest) ** arg2) - 1)))
        overpayment = round(payment * arg2 - arg1)
        result(skip, payment, overpayment)
    
    elif skip == "p":
        nom_interest = arg3 / (12 * 100)
        loan = math.floor(arg1 / ((nom_interest * ((1 + nom_interest) ** arg2)) / (((1 + nom_interest) ** arg2) - 1)))
        overpayment = round(arg1 * arg2 - loan)
        result(skip, loan, overpayment)
    
    elif skip == "d":
        d_payments = []
        total = 0
        nom_interest = arg3 / (12 * 100)
        
        for i in range(arg2):
            payment = math.ceil(arg1 / arg2 + nom_interest * (arg1 - arg1 * i / arg2))
            d_payments.append(payment)
            total += payment
        
        overpayment = round(total - arg1)
        result(skip, d_payments, overpayment)


def result(skip, arg, over):
    
    if skip == "n":
        print(converter(arg))
        print(f"Overpayment = {over}")
    
    elif skip == "a":
        print(f"Your monthly payment = {arg}!")
        print(f"Overpayment = {over}")
    
    elif skip == "p":
        print(f"Your loan principal = {arg}!")
        print(f"Overpayment = {over}")
    
    elif skip == "d":
        n = 1
        
        for i in arg:
            print(f"Month {n}: payment is {i}")
            n += 1
        
        print()
        print(f"Overpayment = {over}")


def converter(arg):
    x_years = arg // 12
    y_months = arg % 12
    
    if x_years == 0:
        str_x_years = ""
    
    elif x_years == 1:
        str_x_years = "1 year"
    
    else:
        str_x_years = f"{x_years} years"
    
    if y_months == 0:
        str_y_months = ""
    
    elif y_months == 1:
        str_y_months = "1 month"
    
    else:
        str_y_months = f"{y_months} months"
    
    if x_years == 0:
        return f"It will take {str_y_months} to repay this loan!"
    
    elif y_months == 0:
        return f"It will take {str_x_years} to repay this loan!"
    
    else:
        return f"It will take {str_x_years} and {str_y_months} to repay this loan!"


main()


# principal = 0
# payment = 0
# months = 0
# lastpayment = 0

# print("Enter the loan principal:")
# principal = int(input())


# if user_input == "m":
#     print("Enter the monthly payment:")
#     payment = int(input())
#     months = round(principal / payment)
#     if months == 1:
#         print()
#         print("It will take " + str(months) + " month to repay the loan")
#     else:
#         print()
#         print("It will take " + str(months) + " months to repay the loan")

# elif user_input == "p":
#     print("Enter the number of months:")
#     months = int(input())
#     payment = math.ceil(principal / months)
#     if principal / payment == months:
#         print()
#         print("Your monthly payment =", payment)
#     else:
#         lastpayment = principal - (months - 1) * payment
#         print()
#         print("Your monthly payment = " + str(payment) + " and the last payment = " + str(lastpayment))

# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'

# print(loan_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)