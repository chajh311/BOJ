n = int(input())

count = 0   # 봉지 수
mid = 0   # 5킬로그램 봉지로 담을 수 없는 양
breaker = False

if n % 5 == 0:   # n이 5의 배수면
    count = n//5   # 5킬로그램 봉지로
else:   # n이 5의 배수 아니면
    mid = n % 5
    while mid <= n:
        if mid % 3 == 0:   # mid를 3킬로그램 봉지로 담을 수 있는가
            count = mid//3   # count에 3킬로그램 봉지 수 더하기
            count += (n-mid)//5   # count에 5킬로그램 봉지수
            breaker = True   # n킬로그램을 만들 수 있다.
            break
        else:
            mid += 5   # 5킬로그램 봉지 하나를 포기
    if breaker == False:
        count = -1
print(count)
