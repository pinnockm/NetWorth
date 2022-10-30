# NetWorth
## Project Description
Shitty net-worth target calculator loosely based on the"The Millionaire Next Door" book by idk who...

## Purpose
The original formulation was motivated by an argument along the lines of:

> Take your age in years A, your annual pretax income I; the 10% of the product A*I is your target net-worth T.

An Under Accumulator of Wealth (**UAW**) is someone who's net worth N < T. The reciprocal category is the Prodigious Accumulator of Wealth (**PAW**) which is characterized by a net-worth N > T. An Average Accumulator of Wealth (**AAW**) is one who's net-worth N=T.

A lot of people think this formula is busted (source: me LOL). Two main problems that can be remedied easily are:

1. Since the abolishment of child-slavery in the first world -- the first 16-18 years of life are near-worthless for generating income. Ergo scale back the age parameter by 18 years.
    * B-B-but what about student loans which takes years to pay off and keep your net-worth negative?? 
    > Not everyone takes on student loans

    > Not everyone is economically unproductive until their mid-20s
2. Pre-tax income numbers. Why are we counting money that we don't have anymore? Remedy to this is to take annual income adjusted for regional taxes.

## Modified Target
The new equation will be `T = I(A-18)/10`. Where `I` is your post-tax yearly income, and `A` is your current age.

### Further considerations

#### **1. Possible?**
These targets are still pretty high. Suppose we are interested in the question: is it possible for me to reach this goal?

Assume your real-life net-worth grows linearly per month. Let the linear growth of your networth be described by `L(x) = m*x + b`. Where `x` is in months, `b` is your current net-worth, and `m` is the amount that your net-worth increases per month. We can answer this question if at any point in the future `L(x)/T(x) = 1`. To define the target as it varies over time we assume that your income grows by ~3.5% per annum. This gives us the expression 

`T(x) = I(1.035)**(x/12)*(A-18 + x/12)/10`.

#### **2. Point of No Return?**
Let's say we will not make our target but we are getting closer each month/year. What is the closest we will get to our target?

This problem reduces to finding a turning point in the function `L(x)/T(x)`. That is, solving for when

`[L'(x)T(x)-L(x)T'(x)]/[T(x)]**2 = 0  ==> L'(x)T(x)-L(x)T'(x)` &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (1)

assuming `L(x)/T(x)` is concave down. This should yield a quadratic in `x` and the 'point of no-return' will be at the positive solution of this equation. There will be solutions so as long as the discriminant of (1) is positive. 

You can interperet this value to be the number of months that your current saving habits will afford you progress towards reaching the target. After this point, the magnitude of your current saving habits will not be enough to outwiegh the growing expectation that a higher age imposes on the net-worth formula.
