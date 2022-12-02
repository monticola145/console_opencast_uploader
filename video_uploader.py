import argparse

from OpencastAPI.opencast_api import OpencastAPI

# sample input = python video_uploader.py
# 504 cam228 2022 10 18 10 30 D:/.../file.mp4
parser = argparse.ArgumentParser(description='Uploads a video to Opencast')
parser.add_argument('location', type=str, help='Location of the camera')
parser.add_argument('camera', type=str, help='Camera name')
parser.add_argument('year', type=str, help='Year of the record')
parser.add_argument('month', type=str, help='Month of the record')
parser.add_argument('day', type=str, help='Day of the record')
parser.add_argument('hour', type=str, help='Hour of the record')
parser.add_argument('minutes', type=str, help='Minutes of the record')
parser.add_argument('path', type=str, help='Media path', nargs='+')

args = parser.parse_args()


def main():
    OpencastAPI(args)


if __name__ == '__main__':
    main()
