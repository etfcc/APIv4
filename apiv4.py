from files import *
from broadcasting import *

# ----------------------------------------------------------------------------------------------------------------------
def get_subscription(debug=False):
    response = requests.get(url=f'{URL}/subscription', headers=headers)
    ret = handle_errors(response, debug)
    return ret["subscription"]


# ----------------------------------------------------------------------------------------------------------------------
def patch_subscription(params, debug=False):
    response = requests.patch(url=f'{URL}/subscription', params=params, headers=headers)
    ret = handle_errors(response, debug)
    return ret["subscription"]


# ----------------------------------------------------------------------------------------------------------------------
def get_avatars(id, debug=False):
    params = {"subscription_ids[]": id}
    response = requests.get(url=f'{URL}/subscriptions/avatars', headers=headers, params=params)
    ret = handle_errors(response, debug)
    return ret


# ----------------------------------------------------------------------------------------------------------------------
def get_subscription_public(meeting_id, debug=False):
    response = requests.get(url=f'{URL}/meeting_url/{meeting_id}/subscription', headers=headers)
    handle_errors(response, debug)


