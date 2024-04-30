import requests
import json

_server = 'https://hub.pinata.cloud'
dbStats = requests.get(f'{_server}/v1/info?dbstats=1')
lastUserDownloaded = 36645

for userFid in range(lastUserDownloaded,dbStats.json()['dbStats']['numFidEvents']):
    userData = requests.get(f'{_server}/v1/userDataByFid?fid={userFid}')
    print(userFid)
    try:
        with open(f'/Users/andrewgoldberg/Projects/farcaster-analysis/data/user/{userFid}.json', 'w', encoding='utf-8') as f:
            json.dump(userData.json(), f, ensure_ascii=False, indent=4)
    except:
        continue