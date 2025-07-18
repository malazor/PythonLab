from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def main():
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    start = datetime.now()
    print("Inicio:", start.strftime(DATE_FORMAT))

    cumple = datetime(1977,12,20,8,45,35)
    diff_dates(cumple)

    alter_dates(cumple)

    end = datetime.now()
    print("Fin:", end.strftime(DATE_FORMAT))


def diff_dates(cumple):
    date1 = datetime.now()
    date2 = datetime.now()


    print("\tDate1: ", date1)
    print("\tDate2: ", date2)
    print("\tMi cumpleaños: ", cumple)

    if date1==cumple:
        print("\tSon iguales")
    elif date1>cumple: 
        print("\tDate 1 es mayor que mi cumple")
    elif date1<cumple:
        print("\tDate 2 es mayor que mi cumple")

def alter_dates(c):
    c = c + timedelta(days=-5)
    print("\tDate alterado: ", c)

if __name__ == "__main__":
    main()  # Esto debe estar a la misma altura que el bloque if
