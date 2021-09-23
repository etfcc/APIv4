import json

# ----------------------------------------------------------------------------------------------------------------------
def handle_errors(response, debug):
    if response.status_code != 200:
        print("STATUS ", response.status_code)
        exit(1)
    try:
        ret = response.json()
    except:
        print(response)
        print("Exception: Reply from the server is not JSON")
        exit(1)
    if ret['retcode'] != 0:
        print(response.status_code, json.dumps(ret, indent=4))
        exit(1)
    if debug:
        print(response.status_code, json.dumps(ret, indent=4))
    return ret

