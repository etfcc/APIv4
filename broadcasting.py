import requests

from credentials import *
from common import *


# ----------------------------------------------------------------------------------------------------------------------
def start_broadcasting(id, debug=False):
    params = {"id": id}
    response = requests.post(url=f'{URL}/broadcast_sessions', headers=headers, params=params)
    ret = handle_errors(response, debug)
    return ret

# ----------------------------------------------------------------------------------------------------------------------
def stop_broadcasting(debug=False):
    response = requests.delete(url=f'{URL}/broadcast_sessions', headers=headers)
    ret = handle_errors(response, debug)
    return ret

# ----------------------------------------------------------------------------------------------------------------------
def pause_broadcasting(debug=False):
    params = {"state": "pause"}
    response = requests.patch(url=f'{URL}/broadcast_sessions', headers=headers, params=params)
    ret = handle_errors(response, debug)
    return ret

# ----------------------------------------------------------------------------------------------------------------------
def resume_broadcasting(debug=False):
    params = {"state": "resume"}
    response = requests.patch(url=f'{URL}/broadcast_sessions', headers=headers, params=params)
    ret = handle_errors(response, debug)
    return ret

# ----------------------------------------------------------------------------------------------------------------------
def set_broadcasting_position(position, debug=False):
    params = {"progress": position}
    response = requests.patch(url=f'{URL}/broadcast_sessions', headers=headers, params=params)
    ret = handle_errors(response, debug)
    return ret

# ----------------------------------------------------------------------------------------------------------------------
def get_broadcasting_status(debug=False):
    response = requests.get(url=f'{URL}/broadcast_sessions', headers=headers)
    ret = handle_errors(response, debug)
    return ret

