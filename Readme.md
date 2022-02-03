#credentials.py shall be like this
<pre>
client_id = ""
client_secret = ""
URL = "https://www.freeconferencecall.com/api/v4/"
auth = ""
</pre>

Sample session will be like:

<pre>
Enter command> f list 
#   |                   ID                   |    Description     |  Media   | Duration |    Created    
--------------------------------------------------------------------------------------------------------
 1-R|  ec769273-4e0d-4da6-b0cc-6de40953ab68  |01 Song 149.mp4     |   -V--   |       143|10-20 13:04:00 
 2-R|  c3f0641c-d370-4b57-8bc5-a1e6364c7c9d  |01 Song 149.mp4     |   -V--   |         0|10-11 18:08:30 
 3-R|  29b3e33d-06b8-437f-9776-d31e528b35b9  |KLME-promo.mp4      |   -V--   |        79|10-24 16:50:25 
 4-R|  f6c81129-e664-4c7f-b564-d3d90fc243e6  |calls_0-1000-2.xlsx |   ---D   |         1|10-09 23:16:38 
 5-R|  ac5328d7-07bf-4116-9da5-75da2142188a  |Maine.mp4           |   -V--   |       214|10-08 13:07:52 
 6-R|  7fc39d2e-aee4-48b8-86c6-ee52dd27858d  |2019-03-14-19.video.|   -V--   |      4005|10-08 08:47:11 
 7-R|  676bc295-937e-46f6-81bd-33847381d92b  |The_beauty_of_algebr|   -V--   |       605|10-07 22:48:06 
 8-R|  88449755-0664-4f03-84c8-7d048bc4b1d1  |I_Belong_To_You_Will|   A---   |       430|08-11 19:49:30 
 9-R|  ed9ad4b6-5936-4eb8-bac5-0993d0993584  |1FA84894-8674-47C0-B|   A---   |      3540|04-29 01:05:24 
10-R|  03077924-cec5-4e39-b044-615e4e33eb12  |DHDSALES_PROPOSAL565|   ---D   |         3|04-04 03:18:18 
Total files 15
Enter command> b start 3
Enter command> b status 
200 {
    "broadcast_session": {
        "duration": 79,
        "progress": 5,
        "resource_id": "29b3e33d-06b8-437f-9776-d31e528b35b9",
        "state": "playing"
    },
    "retcode": 0
}
Enter command> 

</pre>
