from datetime import datetime, date
import utils as u
import globals as g

def main():
    '''Calls function that loops through dates until break'''
    u.loop_dates(g.s3_bucket, g.s3_folder, g.start_date)

if __name__ == "__main__":
    main()
