from datetime import datetime

def format_date(line):
    date_format = "%d/%b/%Y:%H:%M:%S"
    converted_date = datetime.strptime(line, date_format)
    return(converted_date)

