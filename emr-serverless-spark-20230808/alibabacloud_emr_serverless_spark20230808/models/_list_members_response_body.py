# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListMembersResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        members: List[main_models.ListMembersResponseBodyMembers] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 一次获取的最大记录数。
        self.max_results = max_results
        self.members = members
        # 下一页TOKEN。
        self.next_token = next_token
        # 请求ID。
        self.request_id = request_id
        # 记录总数。
        self.total_count = total_count

    def validate(self):
        if self.members:
            for v1 in self.members:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        result['members'] = []
        if self.members is not None:
            for k1 in self.members:
                result['members'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        self.members = []
        if m.get('members') is not None:
            for k1 in m.get('members'):
                temp_model = main_models.ListMembersResponseBodyMembers()
                self.members.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListMembersResponseBodyMembers(DaraModel):
    def __init__(
        self,
        actions: List[main_models.ListMembersResponseBodyMembersActions] = None,
        create_time: str = None,
        display_name: str = None,
        member_arn: str = None,
        roles: List[main_models.ListMembersResponseBodyMembersRoles] = None,
        user_name: str = None,
        user_type: str = None,
        visible: bool = None,
    ):
        # 针对此用户允许的操作列表。
        self.actions = actions
        self.create_time = create_time
        # 用户展示名称。
        self.display_name = display_name
        # 用户 arn。
        self.member_arn = member_arn
        # 用户角色列表。
        self.roles = roles
        # 用户名称。
        self.user_name = user_name
        # 用户类型。
        self.user_type = user_type
        self.visible = visible

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()
        if self.roles:
            for v1 in self.roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['actions'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.member_arn is not None:
            result['memberArn'] = self.member_arn

        result['roles'] = []
        if self.roles is not None:
            for k1 in self.roles:
                result['roles'].append(k1.to_map() if k1 else None)

        if self.user_name is not None:
            result['userName'] = self.user_name

        if self.user_type is not None:
            result['userType'] = self.user_type

        if self.visible is not None:
            result['visible'] = self.visible

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('actions') is not None:
            for k1 in m.get('actions'):
                temp_model = main_models.ListMembersResponseBodyMembersActions()
                self.actions.append(temp_model.from_map(k1))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('memberArn') is not None:
            self.member_arn = m.get('memberArn')

        self.roles = []
        if m.get('roles') is not None:
            for k1 in m.get('roles'):
                temp_model = main_models.ListMembersResponseBodyMembersRoles()
                self.roles.append(temp_model.from_map(k1))

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        if m.get('userType') is not None:
            self.user_type = m.get('userType')

        if m.get('visible') is not None:
            self.visible = m.get('visible')

        return self

class ListMembersResponseBodyMembersRoles(DaraModel):
    def __init__(
        self,
        actions: List[main_models.ListMembersResponseBodyMembersRolesActions] = None,
        create_time: int = None,
        description: str = None,
        role_arn: str = None,
        role_name: str = None,
    ):
        # 权限列表。
        self.actions = actions
        # 创建时间。
        self.create_time = create_time
        # 描述。
        self.description = description
        # 角色 arn。
        self.role_arn = role_arn
        # 角色名称。
        self.role_name = role_name

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['actions'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        if self.role_name is not None:
            result['roleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('actions') is not None:
            for k1 in m.get('actions'):
                temp_model = main_models.ListMembersResponseBodyMembersRolesActions()
                self.actions.append(temp_model.from_map(k1))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')

        return self

class ListMembersResponseBodyMembersRolesActions(DaraModel):
    def __init__(
        self,
        action_arn: str = None,
        action_name: str = None,
        dependencies: List[str] = None,
        description: str = None,
        display_name: str = None,
    ):
        # 行为 arn。
        self.action_arn = action_arn
        # 权限名称。
        self.action_name = action_name
        # action 依赖列表。
        self.dependencies = dependencies
        # action 描述。
        self.description = description
        # 权限展示名称。
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_arn is not None:
            result['actionArn'] = self.action_arn

        if self.action_name is not None:
            result['actionName'] = self.action_name

        if self.dependencies is not None:
            result['dependencies'] = self.dependencies

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionArn') is not None:
            self.action_arn = m.get('actionArn')

        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')

        if m.get('dependencies') is not None:
            self.dependencies = m.get('dependencies')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        return self

class ListMembersResponseBodyMembersActions(DaraModel):
    def __init__(
        self,
        action_arn: str = None,
        action_name: str = None,
        dependencies: List[str] = None,
        description: str = None,
        display_name: str = None,
    ):
        # 行为 arn。
        self.action_arn = action_arn
        # 权限名称。
        self.action_name = action_name
        # action 依赖列表。
        self.dependencies = dependencies
        # action 描述。
        self.description = description
        # 权限展示名称。
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_arn is not None:
            result['actionArn'] = self.action_arn

        if self.action_name is not None:
            result['actionName'] = self.action_name

        if self.dependencies is not None:
            result['dependencies'] = self.dependencies

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionArn') is not None:
            self.action_arn = m.get('actionArn')

        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')

        if m.get('dependencies') is not None:
            self.dependencies = m.get('dependencies')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        return self

