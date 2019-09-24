import sys, datetime


def print_usage():
    print("Usage: python3 md_maker.py [mode] [simple_filename]")
    print("mode: -a for auto-date, -m for manual-date")


if len(sys.argv) != 3:
    print_usage()
    exit()

simple_filename = sys.argv[2]
post_layout = "post"

post_title = str()
post_filename = str()
post_date = str()
post_categories = str()

now_date = datetime.datetime.now()
date_year = str(now_date.year)
date_month = str(now_date.month)
date_day = str(now_date.day)
date_hour = str(now_date.hour)
date_minute = str(now_date.minute)
date_second = str(now_date.second)

# str(post_categories).replace("'", '')

if sys.argv[1] == '-m':
    post_title = input("title: ")
    date_month = input("month: ")
    date_day = input("day: ")
    date_hour = input("hour: ")
    date_minute = input("minute: ")
    date_second = "00"
elif sys.argv[1] == '-a':
    post_title = input("title: ")
else:
    print_usage()
    exit()

post_filename = f"{date_year}-{date_month}-{date_day}-{simple_filename}.md"
post_date = date_year + "-" + date_month + "-" + date_day + " " + date_hour + ":" + date_minute + ":" + date_second + " +0900"
post_categories = "[" + input("categories: ") + "]"

file = open(post_filename, 'w')
file.write("---")
file.write("\nlayout: " + post_layout)
file.write("\ntitle: " + post_title)
file.write("\ndate: " + post_date)
file.write("\ncategories: " + post_categories)
file.write("\n---\n\n")
