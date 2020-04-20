import pdb
import json
import requests

def astar_send_alert_msg(input_request):
    message = input_request.get("message")
    details = input_request.get("details")
    details = details.replace("&#34;", "'").replace("'", '"')
    details = json.loads(details)
    msg_content = details.get("Fields")
    varname = message.split("_")[0]
    type = message.split("_")[1]
    # print(details)
    # print(message)
    content ="【字段名】：<%s>\n【告警类型】：<%s>\n【告警内容】：<%s>" % (str(varname), str(type), str(msg_content))
    phone = 15000406743
    # res = send_msg(content, phone)
    code = 200
    print(content)
    return code


def send_msg(message, phone):
    url = "http://q.hl95.com:8061"
    params = {
        "username": "上海耳序科技",
        "password": "PaiPaiDai888",
        "phone": phone,
        "message": message,
        "epid": 124901
    }
    res = requests.get(url, params=params)
    if res.status_code == 200:
        pdb.set_trace()
        print(res)

input_request = {'id': 'test_rubik_var_value:nil', 'message': 'CellphoneCount_平均值告警', 'details': '{&#34;Name&#34;:&#34;test_rubik_var_value&#34;,&#34;TaskName&#34;:&#34;post_test_平均值&#34;,&#34;Group&#34;:&#34;nil&#34;,&#34;Tags&#34;:{},&#34;ServerInfo&#34;:{&#34;Hostname&#34;:&#34;791707fc0f9c&#34;,&#34;ClusterID&#34;:&#34;0e5b45ab-6296-46cc-8402-e5001b9b1bb8&#34;,&#34;ServerID&#34;:&#34;5fb489bc-c7ac-4c2b-bfbd-9ae4458f477a&#34;},&#34;ID&#34;:&#34;test_rubik_var_value:nil&#34;,&#34;Fields&#34;:{&#34;fenmu_mean_value&#34;:0.3333333333333333,&#34;fenzi_mean_value&#34;:0.3333333333333333},&#34;Level&#34;:&#34;CRITICAL&#34;,&#34;Time&#34;:&#34;2019-06-06T07:43:30Z&#34;,&#34;Duration&#34;:990000000000,&#34;Message&#34;:&#34;CellphoneCount app新客 平均值告警&#34;}\n', 'time': '2019-06-06T07:43:30Z', 'duration': 990000000000, 'level': 'CRITICAL', 'data': {'series': [{'name': 'test_rubik_var_value', 'columns': ['time', 'fenmu_mean_value', 'fenzi_mean_value'], 'values': [['2019-06-06T07:43:30Z', 0.3333333333333333, 0.3333333333333333]]}]}, 'previousLevel': 'CRITICAL', 'recoverable': True}


if __name__ == '__main__':
    print(astar_send_alert_msg(input_request))