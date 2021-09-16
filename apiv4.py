import json
import requests

from credentials import *

headers = {"Content-Type": "application/json", "Authorization": "Bearer " + auth}


# ----------------------------------------------------------------------------------------------------------------------
def handle_errors(response, debug):
    if response.status_code != 200:
        print("STATUS ", response.status_code)
        exit(1)
    ret = response.json()
    if ret['retcode'] != 0:
        print(ret['error'])
        exit(1)
    if debug:
        print(response.status_code,json.dumps(ret, indent=4))
    return ret


# ----------------------------------------------------------------------------------------------------------------------
def get_avatars(id, debug=False):
    params = {"subscription_ids[]": id}
    response = requests.get(url=f'{URL}/subscriptions/avatars', headers=headers, params=params)
    ret = handle_errors(response,debug)
    return ret

# ----------------------------------------------------------------------------------------------------------------------
def get_subscription_public(meeting_id, debug=False):
    response = requests.get(url=f'{URL}/meeting_url/{meeting_id}/subscription', headers=headers)
    handle_errors(response, debug)


# ----------------------------------------------------------------------------------------------------------------------
def get_broadcasting_resources(offset=0, limit=10, debug=False):
    params = {"offset": offset,
              "limit": limit}
    response = requests.get(url=f'{URL}/broadcast_resources', headers=headers, params=params)
    ret = handle_errors(response, debug)
    files = ret["broadcast_resources"]
    for file in files:
        if file['pages_count'] is not None:
            file["media"] = {'audio': False, 'video': False, 'document': True, 'screen_sharing': False}
            file['duration'] = file['pages_count']
        else:
            file["media"] = {'audio': True, 'video': file['video'], 'screen_sharing': file['screen_sharing'],
                             'document': False}
        del file['video'], file['screen_sharing'], file['pages_count']
    return files


# ----------------------------------------------------------------------------------------------------------------------
def start_broadcasting(id, debug=False):
    params = {"id": id}
    response = requests.post(url=f'{URL}/broadcast_sessions', headers=headers, params=params)
    ret = handle_errors(response, debug)
    return ret["id"]


# ----------------------------------------------------------------------------------------------------------------------
def stop_broadcasting(id, debug=False):
    response = requests.delete(url=f'{URL}/broadcast_sessions/{id}', headers=headers)
    handle_errors(response, debug)


# ----------------------------------------------------------------------------------------------------------------------
def set_broadcasting_positon(id, position, debug=False):
    params = {"progress": position}
    if position == 'play':  params = {"state": "playing"}
    if position == 'pause':  params = {"state": "pause"}
    response = requests.patch(url=f'{URL}/broadcast_sessions/{id}', headers=headers, params=params)
    handle_errors(response, debug)


# ----------------------------------------------------------------------------------------------------------------------
def get_broadcasting_status(id, debug=False):
    response = requests.get(url=f'{URL}/broadcast_sessions/{id}', headers=headers)
    ret = handle_errors(response, debug)
    return ret
