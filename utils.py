from typing import List
from datetime import date, timedelta
from decouple import config

import boto3

aws_access_key_id = config("aws_access_key_id", default = "")
aws_secret_access_key = config("aws_secret_access_key", default = "")

client = boto3.client('s3',
        aws_access_key_id = aws_access_key_id,
        aws_secret_access_key = aws_secret_access_key)


def list_files(s3_bucket: str, s3_folder: str, date: date) -> List[str]:
    '''Function to list files in S3 bucket in a particular folder for a particular date'''
    file_list: List[str] = []

    response = client.list_objects_v2(
        Bucket = s3_bucket,
        Prefix = s3_folder + str(date)
        )

    for content in response.get('Contents'):
        file_list.append(content['Key']) # append each filename to file_list

    return file_list


def loop_dates(s3_bucket: str, s3_folder: str, date: date) -> None:
    '''Loops through all dates until N consecutive dates have no files'''

    counter: int = 0
    delta = timedelta(days=1)
    max_tries: int = 5 # number of consecutive dates with no files until break

    while True:
        # print(date)

        try:
            date_file = list_files(s3_bucket, s3_folder, date)
            if len(date_file) > 0:
                counter = 0 # reset counter to 0 if file present for date

            if len(date_file) >= 5: # validate at least 5 files are available
                print(f"{date} has at least 5 files")
                print(date_file)
                # returns date and the bucket path for each file in a list
                break
        except TypeError:
            counter += 1

        if counter == max_tries:
            raise NoDaysRemaining("Number of consecutive dates exceeded")
            # no days remaining = throw error

        date -= delta # check previous date

class NoDaysRemaining(Exception):
    pass
