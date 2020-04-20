import requests
import pandas as pd

filename = ""
csv = pd.read_csv(filename)

for i in range(len(csv)):
    userid = csv.iloc[i]["user_id"]
    listingid = csv.iloc[i]["listing_id"]
    listingtime =
    body = """
    curl -X POST   http://127.0.0.1:8091   -H 'Content-Type: application/json'   -H 'cache-control: no-cache'   -d '{
            "user_info": {
                "userid":  {userid},
                "listingid": {listingid},
                "listingtime":  {listingtime},
                "bizid": 0,
                "dingid": 0,
                "zuid": 0,
                "flow_count": 1,
                "options": {
                    "tanentid": "xx222xx" 
                }
            },
            "variables": [
                "befbid_chuoe_appnotapp_timediff",
                "befbid_chuoe_not0_diffmins_fst",
                "befbid_chuoe_not0times_cnt_l1w",
                "befbid_chuoe_times_daytime",
                "befbid_chuoe_timesbyday_avg_l1w",
                "befbid_listing_bidamount_max",
                "befbid_listing_bidtimes_cnt_l1w",
                "befbid_listing_times_fst10d",
                "befbid_listing_appnewtimes_daytime",
                "befbid_listing_appnewmostfreqhour",
                "befbid_chuoe_amountusediff_lst",
                "befbid_listing_bidamountrat_lst",
                "befbid_details_regbiddiffdays_lst"
            ],
            "rubik_info": {
                "flow_appid": "11050001"
            }
        }'
    """ .format(userid=userid, listingid=listingid, listingtime=listingtime)
