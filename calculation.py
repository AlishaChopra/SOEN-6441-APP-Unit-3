class calculation:

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
            d=self.fact(b)
            sum_sin+=((-1)**c)*(x**b)/d
        return round(sum_sin,4)

    def fact(self,fact_val):
        if (fact_val==0 or fact_val==1):
            return 1
        else:
            return fact_val * self.fact(fact_val-1)

    def cos_cal(self,alpha):
        sum_cal=0
        for i in range(0,10):
            n = 2 * i
            factorial = self.fact(n)
            sum_cal+= ((-1) **i) * (alpha ** n) / factorial
        print(sum_cal)
        return round(sum_cal, 4)

    def cal_alpha(self):
        pi_cal=self.cal_pi()
        print(pi_cal)
        first=round((pi_cal/2),4)
        last=pi_cal
        mid=round((first+last)/2,4)
        while(first<=last):
            y1=round(mid-(pi_cal/2),4)
            y2=self.sin_cal(mid)
            if y1==y2:
                return round(mid,4)
                break
            elif y1<y2:
                first=mid+0.0001
            else:
                last=mid-0.0001
            mid=round((first+last)/2,4)

    def cal_length(self,alpha_val):
        radius=int(input("Enter the radius of the circle:"))
        cos_x=alpha_val/2;
        z=self.cos_cal(cos_x);
        length=2*radius*(1-z)
        return round(length,4)


obj2=calculation()
alpha_val=obj2.cal_alpha()
print("the value of alpha in radians is",alpha_val)
length=obj2.cal_length(alpha_val)
print("the length of the two segments X1X2 is",length)