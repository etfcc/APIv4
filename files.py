import os
import requests

from credentials import *
from common import *


# ----------------------------------------------------------------------------------------------------------------------
def get_files(resource="", offset=0, limit=10, debug=False):
    params = {"offset": offset,
              "limit": limit,
              "order_by": "created_at"}
    if resource != "": params["resource_type"] = resource
    response = requests.get(url=f'{URL}/storage/files', headers=headers, params=params)
    ret = handle_errors(response, debug)
    return ret


# ----------------------------------------------------------------------------------------------------------------------
def patch_file(file, description, debug=False):
    params = {"description": description}
    response = requests.patch(url=f'{URL}/storage/files/{file}', params=params, headers=headers)
    ret = handle_errors(response, debug)
    return ret


# ----------------------------------------------------------------------------------------------------------------------
def delete_file(id, debug=False):
    response = requests.delete(url=f'{URL}/storage/files/{id}', headers=headers)
    ret = handle_errors(response, debug)
    return ret


# ----------------------------------------------------------------------------------------------------------------------
def upload_file(filename, debug=False):
    headers = {"Authorization": "Bearer " + auth}
    headers["Filename"] = os.path.basename(filename)
    files = {'data': open(filename, 'rb')}
    response = requests.post(url=f'{URL}/storage/upload?resource_type=broadcast_resource', files=files, headers=headers)
    ret = handle_errors(response, debug)
    return ret
