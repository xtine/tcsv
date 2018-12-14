import sys
import csv

import datetime
import pytz


def parseTimestamp(timestamp):
    # convert to datetime object
    date_format = '%m/%d/%y %I:%M:%S %p'
    ts_unaware_pst = datetime.datetime.strptime(timestamp, date_format)
    # set naive datetime to PST
    timezone = pytz.timezone('US/Pacific')
    ts_aware_pst = timezone.localize(ts_unaware_pst)
    # convert to EST
    ts_aware_est = ts_aware_pst.astimezone(pytz.timezone('US/Eastern'))

    return ts_aware_est.isoformat()


def parseDuration(duration):
    hours, minutes, seconds = duration.split(':')

    return(int(hours) * 3600 + int(minutes) * 60 + float(seconds))


def main(input):
    # test for input error (no file or too many specified)
    if len(input) > 2:
        print("Error: You can only parse one file at a time.")
        return
    elif len(input) == 1:
        print("Error: You have to include a csv file to parse.")
        return

    # ready to attempt to parse csv
    with open(input[1], newline='', encoding="utf-8", errors='replace') as csv_file:

        csv_data = csv.DictReader(csv_file)

        print(",".join(csv_data.fieldnames))

        for row in csv_data:
            # Timestamp: convert to ISO-8601
            # Timestamp: convert from PST to EST
            print(parseTimestamp(row['Timestamp']), end=',')

            # Address
            print(''.join(('"', row['Address'], '"')), end=',')

            # ZIP: zero pad to 5 digits total
            row['ZIP'] = row['ZIP'].zfill(5)
            print(row['ZIP'], end=',')

            # FullName: Uppercase english names
            print(row['FullName'].upper(), end=',')

            # FooDuration: HH:MM:SS.MS to floating point seconds
            print(parseDuration(row['FooDuration']), end=',')

            # BarDuration: HH:MM:SS.MS to floating point seconds
            print(parseDuration(row['BarDuration']), end=',')

            # TotalDuration: Sum of FooDuration and BarDuration
            print(parseDuration(row['FooDuration']) + parseDuration(row['BarDuration']), end=',')

            # Notes
            print(''.join(('"', row['Notes'], '"')))


# TODO:
# - Change lazy STDOUT printing of every line
#   - Save changed OrderedDict to a new CSV and print
# - Check for invalid UTF on dates/floats
#   - STDERR and drop row
# - Check if input file is valid (not csv) and STDERR if not


if __name__ == "__main__":
    main(sys.argv)
