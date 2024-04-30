import requests
import json

_server = 'https://hub.pinata.cloud'
fidEvents = 508183
lastUserDownloaded = 2


for userFid in range(lastUserDownloaded,fidEvents):
    castsByFid = requests.get(f'{_server}/v1/castsByFid?fid={userFid}')
    print(userFid)
    # print(castsByFid.json())
    try:
        with open(f'/Users/andrewgoldberg/Projects/farcaster-analysis/data/castsByFid/{userFid}.json', 'w', encoding='utf-8') as f:
            json.dump(castsByFid.json(), f, ensure_ascii=False, indent=4)
    except:
        continue