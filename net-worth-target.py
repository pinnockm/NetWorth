from funcs import *

if __name__ == '__main__':
    print("How old are you?")
    years, months = int(input("Years: ")), int(input("Months: "))
    age = years + months/12
    
    income = float(input("What is your current annual income (after taxes)? $"))
    nw = float(input("What is your current Net Worth (Savings - Debts)? $"))
    savings = float(input("About how much do you save each month? $"))
    
    plotter(income, age, nw, savings)
    try:
        xmax = no_return((years, months), savings, nw)
        min_required = crit_savings(income, age, nw, xmax)
        print(f"\nFor your age, the AAW target is ${target_nw(income, age):.2f}.")
        print(f"You need to save at least ${min_required:.2f} monthly (an extra ${min_required - savings:.2f}) to reach PAW status.")
        
    except:
        print("You do not save enough to reach PAW status or make progress towards the goal.")
    
    print("\nEnd of Program.")
