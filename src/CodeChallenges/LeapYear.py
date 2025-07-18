def is_leap(year):
    leap = False
    
    # Write your logic here
    if year >= 1900 and year <=100000:
        if year%400==0: 
            leap=True
        elif(year%100!=0):
             leap=False
        else:
            if year%4==00:
                leap=True   
    else:
        leap=False
    return leap

year = int(input())
print(is_leap(year))