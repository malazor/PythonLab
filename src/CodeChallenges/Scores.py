if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    if n>=2 and n<=100:
        for x in arr:
            if x==n:
                print(n)