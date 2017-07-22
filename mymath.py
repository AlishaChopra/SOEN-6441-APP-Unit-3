class mymath:

    def cal_pi(self):
        sum=0
        for i in range(1,1000):
            sum=sum+(1/(i*i))
        val=6*sum
        pi=val**(0.5)
        return round(pi,4)


    def sin_cal(self,x):
        sum_sin=0
        for i in range(1,10):
            b=(2 * i) - 1
            c=i-1
            factorial=self.factorial_cal(b)
            sum_sin+=((-1)**c)*(x**b)/factorial
        return round(sum_sin,4)

    def factorial_cal(self,fact_val):
        if (fact_val==0 or fact_val==1):
            return 1
        else:
            return fact_val * self.factorial_cal(fact_val-1)

    def cos_cal(self,alpha):
        sum_cos=0
        for i in range(0,10):
            val = 2 * i
            fact = self.factorial_cal(val)
            sum_cos+= ((-1) **i) * (alpha ** val) / fact
        print(sum_cos)
        return round(sum_cos, 4)



