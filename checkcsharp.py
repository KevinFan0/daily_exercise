import pandas as pd
import json

def check_values(drools_csv, rubik_csv, vars_lst):
    res_lst = []
    #import pdb;pdb.set_trace()
    df_mobile_dev = pd.read_csv(drools_csv,keep_default_na=False,encoding='utf-8')
    df_rubik = pd.read_csv(rubik_csv,keep_default_na=False,encoding='utf-8')
    for var in vars_lst:
        var_info = {}
        for k in ["zero_cnt", "non_zero_cnt", "default_cnt", "downgrade_cnt", "match_cnt", "not_match_cnt"]:
            var_info[k] = 0
        var_info["var_name"] = var
        for i in range(len(df_mobile_dev)):
            mobile_value = df_mobile_dev[var].ix[i]
            rubik_value = df_rubik[var].ix[i]
            #if var == 'monthCallStats':
            #      import pdb;pdb.set_trace()
            if var in('monthCallStats','faHaiList','lianDongList','contactsRelated'):
                  #import pdb;pdb.set_trace()
                  mobile_value = mobile_value.replace("'", '"').replace('None', 'null').replace('True','true').replace('False','false')
                  rubik_value  = rubik_value.replace("'", '"').replace('None', 'null').replace('True','true').replace('False','false')
                  mobile_value = json.loads(mobile_value,strict=False)
                  rubik_value  = json.loads(rubik_value,strict=False)
            if mobile_value == rubik_value and type(mobile_value) == type(rubik_value):
                var_info["match_cnt"] += 1
            else:
                var_info["not_match_cnt"] += 1
                if var == 'phoneNameCertifStatus':
                   print(df_rubik['userid'].ix[i],mobile_value,rubik_value)
            if rubik_value in [-2, -2.0, "-2"]:
                var_info["downgrade_cnt"] += 1
            elif rubik_value in [-1, -1.0, "-1","","[]"] or rubik_value == []:
                var_info["default_cnt"] += 1
            elif rubik_value in [0, 0.0]:
                var_info["zero_cnt"] += 1
            else:
                var_info["non_zero_cnt"] += 1
        #print(var_info)
        #import pdb;pdb.set_trace()
        res_lst.append(var_info)

    df_check = pd.DataFrame(res_lst)
    print(df_check)
    # check_csv = write_csv(df_check, output_path, "check")
    return df_check


if __name__ == '__main__':
    var_list = ["faHaiList"]
    check_values("drools.csv", "rubik.csv", var_list)