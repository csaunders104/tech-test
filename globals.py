from datetime import datetime, date

# inputs
s3_bucket: str  = 'ipsos-mori-cole'
s3_folder: str  = 'daily-data-2023/'
start_date_str: str = '2023-02-05'

# convert date
start_date: date = datetime.strptime(start_date_str, '%Y-%m-%d').date()