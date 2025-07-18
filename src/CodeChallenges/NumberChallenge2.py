if __name__ == '__main__':
    n = int(input())
    i=0

    if (n>=0 and n<=20):
        while (i<n):
            print(i*i)
            i=i+1
    else:
        print("Incorrecto")
