import json


class APIv4Exception(Exception):
    def __init__(self, code, body=""):
        self.code = code
        self.body = body


# ----------------------------------------------------------------------------------------------------------------------
def handle_errors(response, debug):
    if response.status_code != 200:
        raise APIv4Exception(response.status_code)
    try:
        ret = response.json()
    except:
        print(response)
        print("Exception: Reply from the server is not JSON")
        raise APIv4Exception(response.status_code)
    if ret['retcode'] != 0:
        raise APIv4Exception(response.status_code,json.dumps(ret, indent=4))
    if debug:
        print(response.status_code, json.dumps(ret, indent=4))
    return ret
