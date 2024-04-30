import requests
import json

_server = 'https://hub.pinata.cloud'
fidEvents = 508183
lastUserDownloaded = 1


for userFid in range(lastUserDownloaded,fidEvents):
    reactionsByFid = requests.get(f'{_server}/v1/reactionsByFid?fid={userFid}')
    print(userFid)
    try:
        with open(f'data/reactionsByFid/{userFid}.json', 'w', encoding='utf-8') as f:
            json.dump(reactionsByFid.json(), f, ensure_ascii=False, indent=4)
    except:
        continue