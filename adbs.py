# For future dates:
# 1. Change start/end values accordingly.
# 2. Add new rows of bs_data. Dont forget to add ',' to the existing last row.

bsStart, bsEnd = "2000-1-1", "2090-12-30"
adStart, adEnd = "1943-4-14", "2034-4-13"

bs_data = """
30,32,31,32,31,30,30,30,29,30,29,31,
31,31,32,31,31,31,30,29,30,29,30,30,
31,31,32,32,31,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
30,32,31,32,31,30,30,30,29,30,29,31,
31,31,32,31,31,31,30,29,30,29,30,30,
31,31,32,32,31,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
31,31,31,32,31,31,29,30,30,29,29,31,
31,31,32,31,31,31,30,29,30,29,30,30,
31,31,32,32,31,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
31,31,31,32,31,31,29,30,30,29,30,30,
31,31,32,31,31,31,30,29,30,29,30,30,
31,31,32,32,31,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
31,31,31,32,31,31,29,30,30,29,30,30,
31,31,32,31,31,31,30,29,30,29,30,30,
31,32,31,32,31,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,30,29,31,
31,31,31,32,31,31,30,29,30,29,30,30,
31,31,32,31,31,31,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,30,
31,32,31,32,31,30,30,30,29,30,29,31,
31,31,31,32,31,31,30,29,30,29,30,30,
31,31,32,31,31,31,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
30,32,31,32,31,30,30,30,29,30,29,31,
31,31,32,31,31,31,30,29,30,29,30,30,
31,31,32,31,32,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
30,32,31,32,31,30,30,30,29,30,29,31,
31,31,32,31,31,31,30,29,30,29,30,30,
31,31,32,32,31,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
30,32,31,32,31,31,29,30,30,29,29,31,
31,31,32,31,31,31,30,29,30,29,30,30,
31,31,32,32,31,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
31,31,31,32,31,31,29,30,30,29,30,30,
31,31,32,31,31,31,30,29,30,29,30,30,
31,31,32,32,31,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
31,31,31,32,31,31,29,30,30,29,30,30,
31,31,32,31,31,31,30,29,30,29,30,30,
31,32,31,32,31,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
31,31,31,32,31,31,30,29,30,29,30,30,
31,31,32,31,31,31,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,30,
31,32,31,32,31,30,30,30,29,30,29,31,
31,31,31,32,31,31,30,29,30,29,30,30,
31,31,32,31,31,31,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,30,
31,32,31,32,31,30,30,30,29,30,29,31,
31,31,32,31,31,31,30,29,30,29,30,30,
31,31,32,31,32,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
30,32,31,32,31,30,30,30,29,30,29,31,
31,31,32,31,31,31,30,29,30,29,30,30,
31,31,32,32,31,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
30,32,31,32,31,31,29,30,29,30,29,31,
31,31,32,31,31,31,30,29,30,29,30,30,
31,31,32,32,31,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
31,31,31,32,31,31,29,30,30,29,29,31,
31,31,32,31,31,31,30,29,30,29,30,30,
31,31,32,32,31,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
31,31,31,32,31,31,29,30,30,29,30,30,
31,31,32,31,31,31,30,29,30,29,30,30,
31,32,31,32,31,30,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,31,
31,31,31,32,31,31,30,29,30,29,30,30,
31,31,32,31,31,31,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,30,
31,32,31,32,31,30,30,30,29,30,29,31,
31,31,31,32,31,31,30,29,30,29,30,30,
31,31,32,31,31,31,30,29,30,29,30,30,
31,32,31,32,31,30,30,30,29,29,30,30,
31,31,32,32,31,30,30,30,29,30,30,30,
30,32,31,32,31,30,30,30,29,30,30,30,
31,31,32,31,31,30,30,30,29,30,30,30,
31,31,32,31,31,30,30,30,29,30,30,30,
31,32,31,32,30,31,30,30,29,30,30,30,
30,32,31,32,31,30,30,30,29,30,30,30,
31,31,32,31,31,31,30,30,29,30,30,30,
30,31,32,32,30,31,30,30,29,30,30,30,
30,32,31,32,31,30,30,30,29,30,30,30,
30,32,31,32,31,30,30,30,29,30,30,30"""

bs_data = tuple(int(item) for item in bs_data.replace("\n", "").split(","))
ad_data = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def unpackDate(date):
    try:
        y, m, d = [int(item) for item in date.split("-")]
    except:
        try:
            y, m, d = [int(item) for item in date.split("/")]
        except:
            try:
                y, m, d = [int(item) for item in date.split(".")]
            except:
                raise AssertionError("Enter date in proper format: y-m-d")
    assert 0 < m < 13, "Invalid date. Check month."
    return (y, m, d)


def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def ad2days(ADdate):
    y, m, d = unpackDate(ADdate)
    assert (
        adStart["y"] < y < adEnd["y"]
        or (y == adStart["y"] and m > adStart["m"])
        or (y == adStart["y"] and m == adStart["m"] and d >= adStart["d"])
        or (y == adEnd["y"] and m < adEnd["m"])
        or (y == adEnd["y"] and m == adEnd["m"] and d <= adEnd["d"])
    ), f"Invalid date. Supported dates: {adStartS} to {adEndS}"
    assert (isLeapYear(y) and m == 2 and 0 < d <= ad_data[m - 1] + 1) or (
        0 < d <= ad_data[m - 1]
    ), "Invalid date. Check day."
    yy = 1
    days = 0
    while yy < y:
        if isLeapYear(yy):
            days += sum(ad_data) + 1
        else:
            days += sum(ad_data)
        yy += 1
    days += sum(ad_data[0 : m - 1])
    days += d
    if isLeapYear(y) and m > 2:
        days += 1
    return days


def bs2days(BSdate):
    y, m, d = unpackDate(BSdate)
    assert (
        bsStart["y"] <= y <= bsEnd["y"]
    ), f"Invalid date. Supported dates: {bsStartS} to {bsEndS}."
    assert 0 < d <= bs_data[(y - bsStart["y"]) * 12 + m - 1], "Invalid date. Check day."
    days = sum(bs_data[0 : (y - bsStart["y"]) * 12])
    days += sum(bs_data[(y - bsStart["y"]) * 12 : (y - bsStart["y"]) * 12 + m - 1])
    days += d
    return days


def days2ad(days):
    y = adStart["y"]
    m = adStart["m"] - 1
    days -= ad2days(adStartS) - adStart["d"]
    while days > 0:
        d = days
        if m == 12:
            m = 0
            y += 1
        if isLeapYear(y) and m == 1:
            days -= 29
        else:
            days -= ad_data[m]
        m += 1
    m = 12 if m % 12 == 0 else m % 12
    return f"{y}-{m}-{d}"


def days2bs(days):
    y = bsStart["y"]
    m = 0
    while days > 0:
        d = days
        if m != 0 and m % 12 == 0:
            y += 1
        days -= bs_data[m]
        m += 1
    m = 12 if m % 12 == 0 else m % 12
    return f"{y}-{m}-{d}"


def ad2bs(date):
    return days2bs(ad2days(date) - (ad2days(adStartS) - 1))


def bs2ad(date):
    return days2ad(bs2days(date) + (ad2days(adStartS) - 1))


def makeDict(*dates):
    keys = ("y", "m", "d")
    for date in dates:
        yield {key: value for key, value in zip(keys, unpackDate(date))}


bsStartS, bsEndS, adStartS, adEndS = bsStart, bsEnd, adStart, adEnd
bsStart, bsEnd, adStart, adEnd = makeDict(bsStart, bsEnd, adStart, adEnd)

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        from datetime import datetime

        print("Testing for dates since 1943-4-14")
        print("=================================")
        try:
            interval = int(sys.argv[2])
        except:
            interval = 91
        dateList = [
            days2ad(date)
            for date in range(
                ad2days(adStartS),
                ad2days(datetime.now().strftime("%Y-%m-%d")),
                interval,
            )
        ]
        t = datetime.now()
        resultList = [bs2ad(ad2bs(date)) for date in dateList]
        print(
            "Took",
            str(datetime.now() - t),
            f"for dates in interval of {interval} day(s).",
        )
        print(dateList == resultList)

    else:
        while True:
            choice = input("1. AD2BS\n2. BS2AD\nq. Quit\nChoice? ")
            if choice == "q":
                break
            elif not (choice == "1" or choice == "2"):
                print("Invalid Choice")
            date = input("Date: ")
            if choice == "1":
                print(f"BS Date: {ad2bs(date)}")
            elif choice == "2":
                print(f"AD Date: {bs2ad(date)}")