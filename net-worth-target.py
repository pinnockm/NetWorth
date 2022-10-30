#from math import log1p, sqrt
from cProfile import label
from numpy import arange, array, linspace
import matplotlib.pyplot as plt

def target_nw(income:float, age:float, x=0):
    return income*(1.035)**(x/12)*(age-18 + x/12)/10

def linear_growth(net_worth:float, monthly_savings:float, x):
    return net_worth + monthly_savings*x


def plotter(income, age, net_worth, savings):

    x = linspace(0,240,700)
    y = linear_growth(net_worth, savings, x)/target_nw(income, age, x)

    plt.figure(figsize=(14,8))
    plt.title("Progress Towards 'Prodigious Accumulator of Wealth' Status")
    plt.plot(x, y, lw=2, label='$L(x)/T(x)$')
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
    
    print(f"For your age, the AAW target is ${target_nw(income, age):.2f}.")

    plotter(income, age, nw, savings)
    print("End of Program")
