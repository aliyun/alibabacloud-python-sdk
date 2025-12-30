# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListUserGroupsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListUserGroupsResponseBodyPageResult = None,
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
            temp_model = main_models.ListUserGroupsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListUserGroupsResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        total_count: int = None,
        user_group_list: List[main_models.ListUserGroupsResponseBodyPageResultUserGroupList] = None,
    ):
        self.total_count = total_count
        self.user_group_list = user_group_list

    def validate(self):
        if self.user_group_list:
            for v1 in self.user_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UserGroupList'] = []
        if self.user_group_list is not None:
            for k1 in self.user_group_list:
                result['UserGroupList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.user_group_list = []
        if m.get('UserGroupList') is not None:
            for k1 in m.get('UserGroupList'):
                temp_model = main_models.ListUserGroupsResponseBodyPageResultUserGroupList()
                self.user_group_list.append(temp_model.from_map(k1))

        return self

class ListUserGroupsResponseBodyPageResultUserGroupList(DaraModel):
    def __init__(
        self,
        active: bool = None,
        admin_list: List[main_models.ListUserGroupsResponseBodyPageResultUserGroupListAdminList] = None,
        description: str = None,
        id: str = None,
        my_role: str = None,
        name: str = None,
    ):
        self.active = active
        self.admin_list = admin_list
        self.description = description
        self.id = id
        self.my_role = my_role
        self.name = name

    def validate(self):
        if self.admin_list:
            for v1 in self.admin_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        result['AdminList'] = []
        if self.admin_list is not None:
            for k1 in self.admin_list:
                result['AdminList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.my_role is not None:
            result['MyRole'] = self.my_role

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        self.admin_list = []
        if m.get('AdminList') is not None:
            for k1 in m.get('AdminList'):
                temp_model = main_models.ListUserGroupsResponseBodyPageResultUserGroupListAdminList()
                self.admin_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MyRole') is not None:
            self.my_role = m.get('MyRole')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListUserGroupsResponseBodyPageResultUserGroupListAdminList(DaraModel):
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

