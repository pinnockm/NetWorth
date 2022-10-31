from math import log1p, sqrt
from numpy import arange, linspace
import matplotlib.pyplot as plt

def target_nw(income:float, age:float, x=0):
    return 0.1*income*(1.035)**(x/12)*(age-18 + x/12)

def linear_growth(net_worth:float, monthly_savings:float, x):
    return net_worth + monthly_savings*x

def no_return(age:tuple, monthly_savings:float, net_worth:float) -> float:
    # re-usable constants
    a0, a1 = age    # (years, months)
    a0 = a0 - 18    # rescale 18 years back
    m, b = monthly_savings, net_worth
    s = log1p(0.035)

    # Coefficients of the quadratic
    A = m*s/12
    B = (a0*m + (a1*m +b)/12) * s
    C = b*(1 + a0*s + a1*s/12) - 12*m*(a0 + a1/12)

    # Discriminant of the quadratic
    D = B**2 - 4*A*C
    if D < 0:
        # if discriminant is negative, no real solutions exist
        return None
    # return the positive result of the quadratic formula
    return (-B+sqrt(D))/(2*A)

def crit_savings(income:float, age:float, net_worth:float, xmax:float) -> float:
    """Return how much one should save in order to reach PAW status."""
    return (target_nw(income, age, xmax) - net_worth)/xmax

def plotter(income:float, age:float, net_worth:float, savings:float):

    x = linspace(0,240,700)
    y = linear_growth(net_worth, savings, x)/target_nw(income, age, x)

    plt.figure(figsize=(14,8))
    plt.title("Progress Towards 'Prodigious Accumulator of Wealth' Status")
    plt.plot(x, y, lw=2, label='$L(x)/T(x)$')
    
    xmax = no_return((int(age), (age-int(age))*12), savings, net_worth)
    if xmax:
        ymax = linear_growth(net_worth, savings, xmax)/target_nw(income, age, xmax)
        plt.plot(xmax, ymax, 'ro')
        plt.annotate(text=f"({xmax:.2f},{ymax:.3f})",xy=(xmax,ymax))
    
    plt.fill_between(x, y, 1, where=(y<1), color='red', alpha=0.25, label='UAW')
    plt.fill_between(x, y, 1, where=(y>=1), color='green', alpha=0.25, label='PAW')
    plt.xlabel("Months")
    plt.ylabel("Progress")
    plt.xticks(arange(0,max(x)+1,12))
    plt.xlim(left=0, right=max(x))
    plt.ylim(bottom=0, top=2)
    plt.legend()
    plt.show()
    pass


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
