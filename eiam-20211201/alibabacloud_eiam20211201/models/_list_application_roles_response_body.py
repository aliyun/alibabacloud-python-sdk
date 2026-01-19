# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListApplicationRolesResponseBody(DaraModel):
    def __init__(
        self,
        application_roles: List[main_models.ListApplicationRolesResponseBodyApplicationRoles] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.application_roles = application_roles
        self.max_results = max_results
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.application_roles:
            for v1 in self.application_roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationRoles'] = []
        if self.application_roles is not None:
            for k1 in self.application_roles:
                result['ApplicationRoles'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_roles = []
        if m.get('ApplicationRoles') is not None:
            for k1 in m.get('ApplicationRoles'):
                temp_model = main_models.ListApplicationRolesResponseBodyApplicationRoles()
                self.application_roles.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationRolesResponseBodyApplicationRoles(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_role_id: str = None,
        application_role_name: str = None,
        application_role_value: str = None,
        description: str = None,
        instance_id: str = None,
    ):
        self.application_id = application_id
        # 应用角色的唯一标识
        self.application_role_id = application_role_id
        # 应用角色名称
        self.application_role_name = application_role_name
        self.application_role_value = application_role_value
        self.description = description
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_role_id is not None:
            result['ApplicationRoleId'] = self.application_role_id

        if self.application_role_name is not None:
            result['ApplicationRoleName'] = self.application_role_name

        if self.application_role_value is not None:
            result['ApplicationRoleValue'] = self.application_role_value

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationRoleId') is not None:
            self.application_role_id = m.get('ApplicationRoleId')

        if m.get('ApplicationRoleName') is not None:
            self.application_role_name = m.get('ApplicationRoleName')

        if m.get('ApplicationRoleValue') is not None:
            self.application_role_value = m.get('ApplicationRoleValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

