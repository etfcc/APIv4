import json
import apiv4

offset = 0
limit = 10
files = []


# ----------------------------------------------------------------------------------------------------------------------
def test_broadcasting(cmd):
    if cmd[0] != 'b' or len(cmd) < 2: return False

    if cmd[1] == 'start' and len(cmd) == 3:
        ret = apiv4.start_broadcasting(files[int(cmd[2]) - 1]["id"])
    elif cmd[1] == 'stop':
        ret = apiv4.stop_broadcasting()
    elif cmd[1] == 'pause':
        ret = apiv4.pause_broadcasting()
    elif cmd[1] == 'resume':
        ret = apiv4.resume_broadcasting()
    elif cmd[1] == 'pos' and len(cmd) == 3:
        ret = apiv4.set_broadcasting_position(cmd[2])
    elif cmd[1] == 'status':
        ret = apiv4.get_broadcasting_status(True)
    else: return False
    if ret["retcode"] != 0:
        print("Server returned error", ret)
    return True


# ----------------------------------------------------------------------------------------------------------------------
def test_subscription(cmd):
    if cmd[0] != 's': return False

    if len(cmd) > 2 and cmd[1] == 'name':
        if len(cmd) > 3:
            params = {"first_name": line[2], "last_name": line[3]}
        else:
            params = {"first_name": line[2], "last_name": ""}
        apiv4.patch_subscription(params)
    elif len(cmd) == 3 and cmd[1] == 'set':
        params = json.loads(cmd[2])
        apiv4.patch_subscription(params)
    else:
        ret = apiv4.get_subscription()
        print("[", ret["id"], "]", ret["email"], ret["first_name"], ret["last_name"])
        print("Meeting ID :", ret["meeting_url"])
        print("Access Code:", ret["access_code"])
        print("PIN:", ret["subscriber_pin"])
        if len(cmd) > 1 and cmd[1] == 'settings':
            print(json.dumps(ret["audio_attrs"], indent=4))
        if len(cmd) > 1 and cmd[1] == 'numbers':
            print(f'TOLL:')
            for n in ret["toll_numbers"]:
                print(f'\t{n["country_name"]:30}|{n["in_country_format"]:30}|{n["international_format"]:30}')
            print(f'TOLL Playback:')
            for n in ret["toll_playback_numbers"]:
                print(f'\t{n["country_name"]:30}|{n["in_country_format"]:30}|{n["international_format"]:30}')

    return True


# ----------------------------------------------------------------------------------------------------------------------
def test_files(cmd):
    global offset, limit, files
    if cmd[0] != 'f' or len(cmd) < 2: return False
    if cmd[1] == 'next':
        offset += limit
        cmd[1] = "list"
    if cmd[1] == 'prev':
        offset -= limit
        cmd[1] = "list"
    if cmd[1] == 'list':
        ret = apiv4.get_files("broadcast_resource", offset, limit)
        files = ret["files"]
        print("#".center(4) + "|" + "ID".center(40) + "|" + "Description".center(20) + "|" + "Media".center(
            10) + "|" + "Duration".center(10))
        print('-----------------------------------------------------------------------------------------')
        i = 1
        for file in files:
            media = list('----')
            if file['media']['audio']: media[0] = 'A'
            if file['media']['video']: media[1] = 'V'
            if file['media']['screen_sharing']: media[2] = 'S'
            if file['media']['document']: media[3] = 'D'
            media = "".join(media)
            print(
                f'{i + offset:4}|{file["id"].center(40)}|{file["description"].center(20)}|{media.center(10)}|{file["duration"]:10}')
            i += 1
        print("Total files", ret["meta"]["total"])
    elif cmd[1] == 'upload' and len(cmd) == 3:
        try:
            apiv4.upload_file(cmd[2], True)
        except (FileNotFoundError, IOError):
            print("file not found")
    elif cmd[1] == 'delete' and len(cmd) == 3:
        apiv4.delete_file(files[int(cmd[2]) - 1 - offset]["id"])
    elif cmd[1] == 'set' and len(cmd) == 3:
        apiv4.patch_file(files[int(cmd[2]) - 1 - offset]["id"], "hello")
    elif cmd[1] == 'limit' and len(cmd) == 3:
        limit = int(cmd[2])
        print("limit is set to:", limit)
    else: return False

    return True



while True:
    line = input("Enter command> ").split()
    if line[0] == 's':
        if not test_subscription(line):
            print("unknown file command, use 'list', 'next', 'prev','upload', 'delete', 'set', 'limit'")
    elif line[0] == 'b':
        if not test_broadcasting(line):
            print("unknown broadcasting command, use 'start', 'stop', 'pause','resume', 'pos'")
    elif line[0] == 'f':
        if not test_files(line):
            print("unknown file command, use 'list', 'next', 'prev','upload', 'delete', 'set', 'limit'")
    else:
        print("Unknown object, use 'f','s','b'")



