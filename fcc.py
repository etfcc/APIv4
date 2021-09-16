import apiv4

#apiv4.get_subscription_public("et", debug=True)
#apiv4.get_avatars(10937821, debug=True)

session=7095164
while True:
    line = input("Enter command> ").split()
    if line[0] == 'list':
        files = apiv4.get_broadcasting_resources()
        print("#".center(4) + "|" + "ID".center(35) + "|" + "Description".center(20) + "|" + "Media".center(10) + "|" + "Duration".center(10))
        print('-----------------------------------------------------------------------------------------')
        i = 1
        for file in files:
            media = list('----')
            if file['media']['audio']: media[0] = 'A'
            if file['media']['video']: media[1] = 'V'
            if file['media']['screen_sharing']: media[2] = 'S'
            if file['media']['document']: media[3] = 'D'
            media = "".join(media)
            print(f'{i:4}|{file["id"]:35}|{file["description"]:20}|{media:10}|{file["duration"]:10}')
            i += 1
    elif line[0] == 'start':
        session = apiv4.start_broadcasting(files[int(line[1]) - 1]["id"], True)
    elif line[0] == 'stop':
        apiv4.stop_broadcasting(session)
    elif line[0] == 'pos':
        apiv4.set_broadcasting_positon(session, line[1])
    elif line[0] == 'status':
        apiv4.get_broadcasting_status(session, True)
