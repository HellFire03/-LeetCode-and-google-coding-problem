class Solution:
    def nthUglyNumber(self,nums: int) -> int:
        if(nums==1):
            return 1
        d=[0]*nums
        d[0]=1
        i=1
        i2,i3,i5=0,0,0
        m2,m3,m5=2,3,5
        while(i<nums):
            d[i]=min(m2,m3,m5)
            if(d[i]==m2):
                i2+=1
                m2=d[i2]*2
            if(d[i]==m3):
                i3+=1
                m3=d[i3]*3
            if(d[i]==m5):
                i5+=1
                m5=d[i5]*5
            i+=1
        return(d[-1])
