
import json
import os
from os.path import dirname, join

import requests
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class OpencastAPI:
    def __init__(self, args=None):
        self.api_url = os.getenv('OPENCAST_API_URL')
        self.post_event(args)

    def post_event(self, args=None):
        api_url = os.getenv('OPENCAST_API_URL')
        with open('OpencastAPI/acl.json') as openfile:
            acl = json.dumps(json.load(openfile))

        with open('OpencastAPI/metadata.json', 'r', encoding='utf8') as openfile:
            metadata = json.load(openfile)

            metadata[0]['fields'][0]['value'] = f'{args.location}_{args.camera}_{args.year}.{args.month}.{args.day}_{args.hour}.{args.minutes}'
            metadata[0]['fields'][9]['value'] = f'{args.year}-{args.month}-{args.day}'
            metadata[0]['fields'][10]['value'] = f'{args.hour}:{args.minutes}'
            metadata = json.dumps(metadata).encode('utf8')

        with open('OpencastAPI/processing.json', 'r') as openfile:
            processing = json.load(openfile)

            processing['workflow'] = os.getenv('OPENCAST_WORKFLOW_ID')

            processing = json.dumps(processing)
        try:
            body = {
                "metadata": (None, metadata),
                "acl": (None, acl),
                "processing": (None, processing),
                "presentation": open(args.path[0], 'rb'),
                "presenter": open(args.path[1], 'rb'),
            }

        except IndexError:
            body = {
                "metadata": (None, metadata),
                "acl": (None, acl),
                "processing": (None, processing),
                "presentation": open(args.path[0], 'rb'),
            }

        headers = {
            'content-disposition': "form-data",
            'cache-control': "no-cache",
            'Connection': 'close'
        }
        
        response = requests.post(f'{api_url}/events', files=body, headers=headers, auth=(os.getenv('OPENCAST_API_USER'), os.getenv('OPENCAST_API_PASSWORD')))
        print(response.status_code)
