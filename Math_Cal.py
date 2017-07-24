class MathCalculations:



# This is FACTORIAL function

 def fact(self, fact_val):

    if (fact_val == 0 or fact_val == 1):
        return 1
    else:
        return fact_val * self.fact(fact_val - 1)

# This is COS function

 def cos_cal(self,alpha):

        sum_cal=0
        for i in range(0,10):
            n = 2 * i
            factorial = self.fact(n)
            sum_cal+= ((-1) **i) * (alpha ** n) / factorial
        print(sum_cal)
        return round(sum_cal, 4)

# This is SIN function

 def sin_cal(self,x):

        sum_sin=0
        for i in range(1,10):
            b=(2 * i) - 1
            c=i-1
            d=self.fact(b)
            sum_sin+=((-1)**c)*(x**b)/d
        return round(sum_sin,4)

# This is PI function

 def cal_pi(self):

        sum=0
        for i in range(1,1000):
            sum=sum+(1/(i*i))
        val=6*sum
        pi=val**(0.5)
        return round(pi,4)


