# import pprint
import time
from os.path import dirname, join


from dotenv import load_dotenv

from GoogleAPI.google_api import GoogleCalendarAPI

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

RETRY_TIME = 2400


def main():
    while True:
        GoogleCalendarAPI()
        time.sleep(RETRY_TIME)


if __name__ == '__main__':
    main()
