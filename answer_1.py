def server_cost(d1, m1, y1, d2, m2, y2):
    cost = 0
    

    if (d2>= d1) and (m2 >= m1) and (y2>y1):    #if it is greater than a year 
        cost = 20000
    elif (d2 == d1) and (m2 == m1) and (y2==y1): # if on the same day
        cost = 20 
    elif ( (d2>=d1 and m2==m1+1) or (m2 > m1+1) or (y2 > y1)): #if greater than a month ; y2 >y1 check because it can also get carried to different year in which case m2 will be less than m1
        if y2>y1 :
            m2 += 12
        cost = 1000 * (m2-m1)
    elif (m2<= m1+1): # if the days are less then a month , and m1+1 is kept in case 30 days isnt completed in the given month itself, highest it can reach is next month 
        if m2==(m1+1):
            d2 += 30
        cost = 30 * (d2-d1)

    return cost

if __name__ == '__main__':
    d1M1Y1 = input().split()
    d1 = int(d1M1Y1[0])
    m1 = int(d1M1Y1[1])
    y1 = int(d1M1Y1[2])
    d2M2Y2 = input().split()
    d2 = int(d2M2Y2[0])
    m2 = int(d2M2Y2[1])
    y2 = int(d2M2Y2[2])

    result = server_cost(d1, m1, y1, d2, m2, y2)
    print(str(result) + '\n')
