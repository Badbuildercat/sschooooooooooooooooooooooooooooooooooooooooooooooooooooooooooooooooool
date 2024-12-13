import random
import time

hour=time.time()
print("start of random numbers")
number=0
amount=0
while number<100000000000000000:
    number=random.randrange(1,100000000000000001)
    amount+=1
    print(number)
hour1=time.time()
time1=hour1-hour
print("end of random numbers final number was:",number, "and it took",amount,"tries and it took",time1,'seconds')
# if this acctualy fiishes your veryy luck because it would take about 3170979 years to complete