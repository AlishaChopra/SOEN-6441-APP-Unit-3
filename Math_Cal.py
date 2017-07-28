'''
TITLE:MATHEMATICAL COMPUTATION FOR FACTORIAL, SIN, COS AND PI
CREATED:18-JUL-2017
'''
class MathCalculations:


# This is FACTORIAL function

 def fact(self, fact_val):
    if(fact_val<0):
        return 0
    elif (fact_val == 0 or fact_val == 1):
        return 1
    else:
        return fact_val * self.fact(fact_val-1)

#Returns the value of factorial to sin and cos methods

# CALCULATION OF COS ALPHA USING TAYLOR SERIES

 def cos_cal(self,alpha):

        sum_cal = 0
        for i in range(0,10):
            n = 2 * i
            factorial = self.fact(n)
            if(factorial>0):
                sum_cal += ((-1)**i) * (alpha**n)/factorial
            else:
                print("Factorial calculation is not possible")
                break
        return round(sum_cal, 4)

# CALCULATION OF SIN ALPHA USING TAYLOR SERIES

 def sin_cal(self,x):

        sum_sin = 0
        for i in range(1,10):
            pow = (2*i) - 1
            pow1 = i - 1
            fact_val = self.fact(pow)
            if (fact_val > 0):
                sum_sin += ((-1)**pow1) * (x**pow)/fact_val
            else:
                print("Factorial calculation is not possible")
                break
        return round(sum_sin,4)

# COMPUTATION OF THE VALUE OF PI

 def cal_pi(self):

        sum = 0
        for i in range(1,1000):
            sum = sum + (1/(i*i))
        val = 6*sum
        pi = val**(0.5)
        return round(pi,4)


