# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListUserGroupMembersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListUserGroupMembersResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListUserGroupMembersResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListUserGroupMembersResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        member_list: List[main_models.ListUserGroupMembersResponseBodyPageResultMemberList] = None,
        total_count: int = None,
    ):
        self.member_list = member_list
        self.total_count = total_count

    def validate(self):
        if self.member_list:
            for v1 in self.member_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MemberList'] = []
        if self.member_list is not None:
            for k1 in self.member_list:
                result['MemberList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_list = []
        if m.get('MemberList') is not None:
            for k1 in m.get('MemberList'):
                temp_model = main_models.ListUserGroupMembersResponseBodyPageResultMemberList()
                self.member_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListUserGroupMembersResponseBodyPageResultMemberList(DaraModel):
    def __init__(
        self,
        creator: main_models.ListUserGroupMembersResponseBodyPageResultMemberListCreator = None,
        gmt_create: int = None,
        id: str = None,
        user_group_id: str = None,
        user_info: main_models.ListUserGroupMembersResponseBodyPageResultMemberListUserInfo = None,
        user_role: str = None,
    ):
        self.creator = creator
        self.gmt_create = gmt_create
        self.id = id
        self.user_group_id = user_group_id
        self.user_info = user_info
        self.user_role = user_role

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.id is not None:
            result['Id'] = self.id

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        if self.user_role is not None:
            result['UserRole'] = self.user_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            temp_model = main_models.ListUserGroupMembersResponseBodyPageResultMemberListCreator()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserInfo') is not None:
            temp_model = main_models.ListUserGroupMembersResponseBodyPageResultMemberListUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        if m.get('UserRole') is not None:
            self.user_role = m.get('UserRole')

        return self

class ListUserGroupMembersResponseBodyPageResultMemberListUserInfo(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        display_name: str = None,
        id: str = None,
    ):
        self.account_name = account_name
        self.display_name = display_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class ListUserGroupMembersResponseBodyPageResultMemberListCreator(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        display_name: str = None,
        id: str = None,
    ):
        self.account_name = account_name
        self.display_name = display_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

