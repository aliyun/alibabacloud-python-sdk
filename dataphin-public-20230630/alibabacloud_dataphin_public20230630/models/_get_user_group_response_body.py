# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetUserGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user_group_info: main_models.GetUserGroupResponseBodyUserGroupInfo = None,
    ):
        # The error code. A value of OK indicates that the request was successful.
        self.code = code
        # The HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The user group details.
        self.user_group_info = user_group_info

    def validate(self):
        if self.user_group_info:
            self.user_group_info.validate()

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.user_group_info is not None:
            result['UserGroupInfo'] = self.user_group_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UserGroupInfo') is not None:
            temp_model = main_models.GetUserGroupResponseBodyUserGroupInfo()
            self.user_group_info = temp_model.from_map(m.get('UserGroupInfo'))

        return self

class GetUserGroupResponseBodyUserGroupInfo(DaraModel):
    def __init__(
        self,
        active: bool = None,
        admin_list: List[main_models.GetUserGroupResponseBodyUserGroupInfoAdminList] = None,
        description: str = None,
        id: str = None,
        my_role: str = None,
        name: str = None,
    ):
        # Indicates whether the user group is enabled.
        self.active = active
        # The administrators of the user group.
        self.admin_list = admin_list
        # The description of the user group.
        self.description = description
        # The user group ID.
        self.id = id
        # The role of the current user in the user group.
        self.my_role = my_role
        # The name of the user group.
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
                temp_model = main_models.GetUserGroupResponseBodyUserGroupInfoAdminList()
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

class GetUserGroupResponseBodyUserGroupInfoAdminList(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        display_name: str = None,
        id: str = None,
    ):
        # The account name of the user.
        self.account_name = account_name
        # The username.
        self.display_name = display_name
        # The user ID.
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

