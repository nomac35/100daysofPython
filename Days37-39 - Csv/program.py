import refactor
def main():
    print("Weather research for Seattle, 2014-2015")
    print()
    refactor.init()
    print(("The hottest 5 days:"))
    days = refactor.hot_days()

    for idx, i in enumerate(days[:5],1):
         print("{} {} F on {}".format(idx,i.actual_max_temp,i.date))

    print(("The coldest 5 days:"))
    print()
    days = refactor.cold_days()

    for idx, i in enumerate(days[:5], 1):
        print("{} {} F on {}".format(idx, i.actual_max_temp, i.date))
    print()
    print(("The wettest 5 days:"))
    days = refactor.wet_days()


    for idx, i in enumerate(days[:5], 1):
        print("{} {} inches of on {}".format(idx, i.actual_precipitation, i.date))


if __name__ == '__main__':
    main()

