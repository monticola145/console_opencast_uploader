import argparse

from OpencastAPI.opencast_api import OpencastAPI

# sample input = python video_uploader.py
# 504 cam228 2022 10 18 10 30 D:/.../file.mp4
parser = argparse.ArgumentParser(description='Uploads a video to Opencast')
parser.add_argument('location', type=str, help='Location of the camera')
parser.add_argument('camera', type=str, help='Camera name')
parser.add_argument('year', type=int, help='Year of the record')
parser.add_argument('month', type=int, help='Month of the record')
parser.add_argument('day', type=int, help='Day of the record')
parser.add_argument('hour', type=int, help='Hour of the record')
parser.add_argument('minutes', type=int, help='Minutes of the record')
parser.add_argument('path', type=str, help='Media path', nargs='+')

args = parser.parse_args()


def main():
    OpencastAPI(args)


if __name__ == '__main__':
    main()
