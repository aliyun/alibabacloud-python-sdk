# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class ListEntitiesForPolicyResponseBody(DaraModel):
    def __init__(
        self,
        groups: main_models.ListEntitiesForPolicyResponseBodyGroups = None,
        request_id: str = None,
        roles: main_models.ListEntitiesForPolicyResponseBodyRoles = None,
        users: main_models.ListEntitiesForPolicyResponseBodyUsers = None,
    ):
        self.groups = groups
        # The request ID.
        self.request_id = request_id
        self.roles = roles
        self.users = users

    def validate(self):
        if self.groups:
            self.groups.validate()
        if self.roles:
            self.roles.validate()
        if self.users:
            self.users.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.roles is not None:
            result['Roles'] = self.roles.to_map()

        if self.users is not None:
            result['Users'] = self.users.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Groups') is not None:
            temp_model = main_models.ListEntitiesForPolicyResponseBodyGroups()
            self.groups = temp_model.from_map(m.get('Groups'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Roles') is not None:
            temp_model = main_models.ListEntitiesForPolicyResponseBodyRoles()
            self.roles = temp_model.from_map(m.get('Roles'))

        if m.get('Users') is not None:
            temp_model = main_models.ListEntitiesForPolicyResponseBodyUsers()
            self.users = temp_model.from_map(m.get('Users'))

        return self

class ListEntitiesForPolicyResponseBodyUsers(DaraModel):
    def __init__(
        self,
        user: List[main_models.ListEntitiesForPolicyResponseBodyUsersUser] = None,
    ):
        self.user = user

    def validate(self):
        if self.user:
            for v1 in self.user:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['User'] = []
        if self.user is not None:
            for k1 in self.user:
                result['User'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k1 in m.get('User'):
                temp_model = main_models.ListEntitiesForPolicyResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k1))

        return self

class ListEntitiesForPolicyResponseBodyUsersUser(DaraModel):
    def __init__(
        self,
        attach_date: str = None,
        display_name: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.attach_date = attach_date
        self.display_name = display_name
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class ListEntitiesForPolicyResponseBodyRoles(DaraModel):
    def __init__(
        self,
        role: List[main_models.ListEntitiesForPolicyResponseBodyRolesRole] = None,
    ):
        self.role = role

    def validate(self):
        if self.role:
            for v1 in self.role:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Role'] = []
        if self.role is not None:
            for k1 in self.role:
                result['Role'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role = []
        if m.get('Role') is not None:
            for k1 in m.get('Role'):
                temp_model = main_models.ListEntitiesForPolicyResponseBodyRolesRole()
                self.role.append(temp_model.from_map(k1))

        return self

class ListEntitiesForPolicyResponseBodyRolesRole(DaraModel):
    def __init__(
        self,
        arn: str = None,
        attach_date: str = None,
        description: str = None,
        role_id: str = None,
        role_name: str = None,
    ):
        self.arn = arn
        self.attach_date = attach_date
        self.description = description
        self.role_id = role_id
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date

        if self.description is not None:
            result['Description'] = self.description

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

class ListEntitiesForPolicyResponseBodyGroups(DaraModel):
    def __init__(
        self,
        group: List[main_models.ListEntitiesForPolicyResponseBodyGroupsGroup] = None,
    ):
        self.group = group

    def validate(self):
        if self.group:
            for v1 in self.group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Group'] = []
        if self.group is not None:
            for k1 in self.group:
                result['Group'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k1 in m.get('Group'):
                temp_model = main_models.ListEntitiesForPolicyResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k1))

        return self

class ListEntitiesForPolicyResponseBodyGroupsGroup(DaraModel):
    def __init__(
        self,
        attach_date: str = None,
        comments: str = None,
        group_name: str = None,
    ):
        self.attach_date = attach_date
        self.comments = comments
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date

        if self.comments is not None:
            result['Comments'] = self.comments

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')

        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

