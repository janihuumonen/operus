from datetime import datetime

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

# s = "2004-05-12T04:26"
# datetime.fromisoformat(s)
#> datetime.datetime(2004, 5, 12, 4, 26)
# datetime.strptime(s, "%Y-%m-%dT%H:%M")
#> datetime.datetime(2004, 5, 12, 4, 26)

def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
	lst = []
	with open(PFilename) as f:
		for l in f.readlines():
			l = l.strip()
			if len(l): lst.append(datetime.fromisoformat(l))
	PTimestamps[:] = lst
	return None

def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
	return len(list(filter(lambda v: v.year == PYear, PTimestamps)))

def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
	mon = MONTHS.index(PMonth)+1
	return len(list(filter(lambda v: v.month == mon, PTimestamps)))

def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
	wday = WEEKDAYS.index(PWeekday)
	return len(list(filter(lambda v: v.weekday() == wday, PTimestamps)))

