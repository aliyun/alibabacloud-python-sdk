# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListRoleResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        role_list: main_models.ListRoleResponseBodyRoleList = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        self.role_list = role_list

    def validate(self):
        if self.role_list:
            self.role_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_list is not None:
            result['RoleList'] = self.role_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleList') is not None:
            temp_model = main_models.ListRoleResponseBodyRoleList()
            self.role_list = temp_model.from_map(m.get('RoleList'))

        return self

class ListRoleResponseBodyRoleList(DaraModel):
    def __init__(
        self,
        role_item: List[main_models.ListRoleResponseBodyRoleListRoleItem] = None,
    ):
        self.role_item = role_item

    def validate(self):
        if self.role_item:
            for v1 in self.role_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RoleItem'] = []
        if self.role_item is not None:
            for k1 in self.role_item:
                result['RoleItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role_item = []
        if m.get('RoleItem') is not None:
            for k1 in m.get('RoleItem'):
                temp_model = main_models.ListRoleResponseBodyRoleListRoleItem()
                self.role_item.append(temp_model.from_map(k1))

        return self

class ListRoleResponseBodyRoleListRoleItem(DaraModel):
    def __init__(
        self,
        action_list: main_models.ListRoleResponseBodyRoleListRoleItemActionList = None,
        role: main_models.ListRoleResponseBodyRoleListRoleItemRole = None,
    ):
        self.action_list = action_list
        self.role = role

    def validate(self):
        if self.action_list:
            self.action_list.validate()
        if self.role:
            self.role.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_list is not None:
            result['ActionList'] = self.action_list.to_map()

        if self.role is not None:
            result['Role'] = self.role.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionList') is not None:
            temp_model = main_models.ListRoleResponseBodyRoleListRoleItemActionList()
            self.action_list = temp_model.from_map(m.get('ActionList'))

        if m.get('Role') is not None:
            temp_model = main_models.ListRoleResponseBodyRoleListRoleItemRole()
            self.role = temp_model.from_map(m.get('Role'))

        return self

class ListRoleResponseBodyRoleListRoleItemRole(DaraModel):
    def __init__(
        self,
        admin_user_id: str = None,
        create_time: int = None,
        id: int = None,
        is_default: bool = None,
        name: str = None,
        update_time: int = None,
    ):
        self.admin_user_id = admin_user_id
        self.create_time = create_time
        self.id = id
        self.is_default = is_default
        self.name = name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_user_id is not None:
            result['AdminUserId'] = self.admin_user_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.name is not None:
            result['Name'] = self.name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminUserId') is not None:
            self.admin_user_id = m.get('AdminUserId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListRoleResponseBodyRoleListRoleItemActionList(DaraModel):
    def __init__(
        self,
        action: List[main_models.ListRoleResponseBodyRoleListRoleItemActionListAction] = None,
    ):
        self.action = action

    def validate(self):
        if self.action:
            for v1 in self.action:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Action'] = []
        if self.action is not None:
            for k1 in self.action:
                result['Action'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action = []
        if m.get('Action') is not None:
            for k1 in m.get('Action'):
                temp_model = main_models.ListRoleResponseBodyRoleListRoleItemActionListAction()
                self.action.append(temp_model.from_map(k1))

        return self

class ListRoleResponseBodyRoleListRoleItemActionListAction(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        group_id: str = None,
        name: str = None,
    ):
        self.code = code
        self.description = description
        self.group_id = group_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

