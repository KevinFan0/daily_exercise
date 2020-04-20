import pandas as pd

from rubik.base import DataSource
from rubik.data_source.user_read_service.interface import UserReadService
from rubik.data_source.userinfo.interface import UserOtherInfo
from rubik.data_source.pc_details.itf_df import GetTalkByphonedf
from rubik.data_source.pc_details.interface import GetTalkByphone
from rubik.data_source.redis_cache.redis import PhonePrefixRedis



class ContactRelated(DataSource):
    async def compute(self, user_info, variable_name, var_default):
        userdetail_info = await self.get_dep_result(
            UserReadService, userid=user_info["userid"], options="userdetailsinfo", operators="EQUAL"
        )
        userdetail_info = userdetail_info.get("data", "")
        if userdetail_info:
            mobilephone = userdetail_info.get("mobilephone", "")
            idnumber = userdetail_info.get("idnumber", "")
            realname = userdetail_info.get("realname", "")
            contactid = user_info["userid"]
        else:
            mobilephone, contactid = "", ""
        userinfo_res = await self.get_dep_result(UserOtherInfo, userid=user_info["userid"], tableName="UserContract")
        userinfo_res = userinfo_res.get("user_contract_response_d_t_o_list", [])
        name_list, contactRelateType, phone_list, callTimes_list,  recentUpdateDate_list = [], [], [], [], []
        relationship_mapping = {
            1: "配偶",
            2: "子女",
            3: "父母",
            4: "兄弟姐妹",
            5: "朋友",
            6: "同事"
        }
        if userinfo_res:
            for item in userinfo_res:
                if item.get("orderid", "") == 0:
                    phone1 = item.get("phone", "")
                elif item.get("orderid", "") == 1:
                    phone2 = item.get("phone", "")
                name_list.append(item.get("realName", ""))
                relationship = relationship_mapping[item.get("relationshipid")]
                contactRelateType.append(relationship)
                phone = item.get("phone", "")
                phone_list.append(phone)
                pcdetailinfo = await self.get_dep_result(
                    GetTalkByphone, userid=user_info["userid"],
                    phone=mobilephone, phone1=phone1, phone2=phone2, operators="EQUAL"
                )
                for item in pcdetailinfo:
                    if item.get("CallPhoneNumber") == phone:
                        callTimes_list.append(item.get("TalkTime", 0))
                        recentUpdateDate_list.append(item.get("CallTime", ""))
                    else:
                        callTimes_list.append(0)
                        recentUpdateDate_list.append("")
                if variable_name in ["isFraud", "overdueDays", "isOverdue", "rejectTimes", "recentRejectReason"]:
                    if contactid == item.get("contactid", ""):
                        pass
        phoneCity = await self.get_dep_result(PhonePrefixRedis, phones=phone_list)
        return userinfo_res





