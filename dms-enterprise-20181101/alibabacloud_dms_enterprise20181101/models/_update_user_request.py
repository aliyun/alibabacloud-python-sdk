# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserRequest(DaraModel):
    def __init__(
        self,
        max_execute_count: int = None,
        max_result_count: int = None,
        mobile: str = None,
        role_names: str = None,
        tid: int = None,
        uid: int = None,
        uid_string: str = None,
        user_nick: str = None,
    ):
        # The maximum number of queries that can be performed each day.
        self.max_execute_count = max_execute_count
        # The maximum number of rows that can be queried each day.
        self.max_result_count = max_result_count
        # The DingTalk ID or mobile number of the user.
        self.mobile = mobile
        # The roles that the user assumes. For more information about the valid values, see the Request parameters section in the [UpdateUser](https://help.aliyun.com/document_detail/465812.html) topic.
        self.role_names = role_names
        # The ID of the tenant.
        # 
        # > : To view the ID of the tenant, log on to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid
        # The Alibaba Cloud unique ID (UID) of the user to update.
        # 
        # This parameter is required.
        self.uid = uid
        # The UID of the String type. If you specify this parameter, the UID of the Long type is replaced.
        self.uid_string = uid_string
        # The nickname of the user.
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_execute_count is not None:
            result['MaxExecuteCount'] = self.max_execute_count

        if self.max_result_count is not None:
            result['MaxResultCount'] = self.max_result_count

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.role_names is not None:
            result['RoleNames'] = self.role_names

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.uid_string is not None:
            result['UidString'] = self.uid_string

        if self.user_nick is not None:
            result['UserNick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxExecuteCount') is not None:
            self.max_execute_count = m.get('MaxExecuteCount')

        if m.get('MaxResultCount') is not None:
            self.max_result_count = m.get('MaxResultCount')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('RoleNames') is not None:
            self.role_names = m.get('RoleNames')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UidString') is not None:
            self.uid_string = m.get('UidString')

        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')

        return self

