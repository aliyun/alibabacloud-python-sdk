# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTicketRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: int = None,
        cmpt_id: str = None,
        expire_time: int = None,
        global_param: str = None,
        ticket_num: int = None,
        user_id: str = None,
        watermark_param: str = None,
        works_id: str = None,
    ):
        # The user\\"s account name.
        # 
        # - If the user is an Alibaba Cloud primary account **wangwu**, the format is **[Primary Account]**, for example, **wangwu**.
        # - If the user is a RAM account **zhangsan**@aliyun.cn**, the format is **[Primary Account: Sub-Account]**, for example, **wangwu:zhangsan**.
        # 
        # > Only one of UserId and AccountName needs to be filled in. If neither is filled in, it will default to binding the report\\"s Owner, and the report will be accessed with that user\\"s identity. If you need to configure row-level permissions, please refer to [Row-Level Permissions](https://help.aliyun.com/document_detail/322783.html).
        self.account_name = account_name
        # The type of the user\\"s account.
        # - 1: Alibaba Cloud account
        # - 3: Quick BI self-built account
        # - 4: DingTalk
        # - 5: RAM sub-account
        # - 9: WeCom
        # - 10: Feishu
        # > If AccountName is not empty, then AccountType must also not be empty.
        self.account_type = account_type
        # Component ID. This is the ID of a component within the above-mentioned dashboard; other types of works do not support this.
        # Refer to [QueryWorksBloodRelationship](https://next.api.aliyun.com/api/quickbi-public/2022-01-01/QueryWorksBloodRelationship?spm=a2c4g.11186623.0.0.15615d7aWVvWAl&params={}&lang=JAVA&tab=DOC&sdkStyle=old) for the API to get the component ID.
        self.cmpt_id = cmpt_id
        # Expiration time
        # - Unit: minutes
        # - Default: 240
        self.expire_time = expire_time
        # Global parameters for the report filter conditions.
        # - A string in JsonArray format.
        # 
        # > If you need to use global parameter capabilities, please contact the [Quick BI Operations Manager](https://h5-alimebot.dingtalk.com/intl/index.htm?spm=a2c4g.11186623.0.0.3da14f6chrDv9e&sourceType=ding_talk&from=DEFFB9G5KBByQkwq23wneFIOmaJ).
        self.global_param = global_param
        # The number of tickets. Each time a ticket is used, the number of tickets decreases by 1.
        # - Default value: 1
        # - Recommended value: 1
        # - Maximum value: 99999
        self.ticket_num = ticket_num
        # Quick BI\\"s UserId, which is not your Alibaba Cloud account ID.
        # You can call the [QueryUserInfoByAccount](https://next.api.aliyun.com/api/quickbi-public/2022-01-01/QueryUserInfoByAccount?spm=a2c4g.11186623.0.0.15615d7aWVvWAl&params={}&tab=DOC&sdkStyle=old) interface to obtain the UserId. An example of a UserId is fe67f61a35a94b7da1a34ba174a7****.
        # 
        # > Only one of UserId and AccountName needs to be filled in. If neither is filled in, it will default to binding the report\\"s Owner, and the report will be accessed with that user\\"s identity. If you need to configure row-level permissions, please refer to [Row-Level Permissions](https://help.aliyun.com/document_detail/322783.html).
        self.user_id = user_id
        # Watermark parameters for the report.
        # - Must not exceed 50 characters.
        # - When the report type is a large screen, watermark parameter passing is not supported.
        self.watermark_param = watermark_param
        # The ID of the report to be embedded. Currently supports dashboards, spreadsheets, data screens, self-service data retrieval, ad-hoc analysis, and data entry.
        # 
        # This parameter is required.
        self.works_id = works_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.cmpt_id is not None:
            result['CmptId'] = self.cmpt_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.global_param is not None:
            result['GlobalParam'] = self.global_param

        if self.ticket_num is not None:
            result['TicketNum'] = self.ticket_num

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.watermark_param is not None:
            result['WatermarkParam'] = self.watermark_param

        if self.works_id is not None:
            result['WorksId'] = self.works_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('CmptId') is not None:
            self.cmpt_id = m.get('CmptId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('GlobalParam') is not None:
            self.global_param = m.get('GlobalParam')

        if m.get('TicketNum') is not None:
            self.ticket_num = m.get('TicketNum')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WatermarkParam') is not None:
            self.watermark_param = m.get('WatermarkParam')

        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')

        return self

