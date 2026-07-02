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
        # The account name of the user.
        # 
        # - If the user is an Alibaba Cloud account **wangwu**, the format is **[primary account]**, for example, **wangwu**.
        # - If the user is a Resource Access Management (RAM) users account **zhangsan**@aliyun.cn**, the format is **[primary account:RAM user]**, for example, **wangwu:zhangsan**.
        # 
        # > Specify either UserId or AccountName. If neither is specified, the report owner is attached by default, and the report is accessed under that user\\"s identity. To configure row-level permissions for data, see [Row-level permissions](https://help.aliyun.com/document_detail/322783.html).
        self.account_name = account_name
        # The account type of the user. Valid values:
        # - 1: Alibaba Cloud account
        # - 3: Quick BI custom account
        # - 4: DingTalk
        # - 5: RAM user
        # - 9: WeCom
        # - 10: Lark
        # > If AccountName is specified, AccountType must also be specified.
        self.account_type = account_type
        # The component ID. This is the ID of a specific component in the dashboard. Other report types are not supported.
        # To obtain the component ID, see [QueryWorksBloodRelationship](https://next.api.aliyun.com/api/quickbi-public/2022-01-01/QueryWorksBloodRelationship?spm=a2c4g.11186623.0.0.15615d7aWVvWAl&params={}&lang=JAVA&tab=DOC&sdkStyle=old).
        self.cmpt_id = cmpt_id
        # The expiration time.
        # - Unit: minutes.
        # - Default value: 240.
        self.expire_time = expire_time
        # The global parameter.
        self.global_param = global_param
        # The number of times the ticket can be used. Each time the ticket is used for access, the count decreases by 1.
        # - Default value: 1.
        # - Recommended value: 1.
        # - Maximum value: 99999.
        self.ticket_num = ticket_num
        # The Quick BI user ID, not your Alibaba Cloud account ID.
        # You can call the [QueryUserInfoByAccount](https://next.api.aliyun.com/api/quickbi-public/2022-01-01/QueryUserInfoByAccount?spm=a2c4g.11186623.0.0.15615d7aWVvWAl&params={}&tab=DOC&sdkStyle=old) operation to obtain the user ID. Example: fe67f61a35a94b7da1a34ba174a7****.
        # 
        # > Specify either UserId or AccountName. If neither is specified, the report owner is used by default, and the report is accessed under that user\\"s identity. To configure row-level permissions for data, see [Row-level permissions](https://help.aliyun.com/document_detail/322783.html).
        self.user_id = user_id
        # The watermark parameter for the report.
        # - The value cannot exceed 50 characters.
        # - Watermark parameters are not supported when the report type is data screen.
        self.watermark_param = watermark_param
        # The ID of the report for which embedding is enabled. Dashboards, workbooks, data screens, ad hoc queries, ad hoc analyses, and data entry forms are supported.
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

