# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListApplicationsForGroupResponseBody(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ListApplicationsForGroupResponseBodyApplications] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.applications = applications
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListApplicationsForGroupResponseBodyApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationsForGroupResponseBodyApplications(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_roles: List[main_models.ListApplicationsForGroupResponseBodyApplicationsApplicationRoles] = None,
        has_direct_authorization: bool = None,
        has_inherit_authorization: bool = None,
    ):
        # 应用的唯一标识。
        self.application_id = application_id
        # 应用角色列表。
        self.application_roles = application_roles
        # 直接分配给当前用户的权限，视为直接授权。
        self.has_direct_authorization = has_direct_authorization
        # 通过用户隶属的组织、组获取的权限，视为继承权限。
        self.has_inherit_authorization = has_inherit_authorization

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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        result['ApplicationRoles'] = []
        if self.application_roles is not None:
            for k1 in self.application_roles:
                result['ApplicationRoles'].append(k1.to_map() if k1 else None)

        if self.has_direct_authorization is not None:
            result['HasDirectAuthorization'] = self.has_direct_authorization

        if self.has_inherit_authorization is not None:
            result['HasInheritAuthorization'] = self.has_inherit_authorization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        self.application_roles = []
        if m.get('ApplicationRoles') is not None:
            for k1 in m.get('ApplicationRoles'):
                temp_model = main_models.ListApplicationsForGroupResponseBodyApplicationsApplicationRoles()
                self.application_roles.append(temp_model.from_map(k1))

        if m.get('HasDirectAuthorization') is not None:
            self.has_direct_authorization = m.get('HasDirectAuthorization')

        if m.get('HasInheritAuthorization') is not None:
            self.has_inherit_authorization = m.get('HasInheritAuthorization')

        return self

class ListApplicationsForGroupResponseBodyApplicationsApplicationRoles(DaraModel):
    def __init__(
        self,
        application_role_id: str = None,
    ):
        # 应用角色标识。
        self.application_role_id = application_role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_role_id is not None:
            result['ApplicationRoleId'] = self.application_role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationRoleId') is not None:
            self.application_role_id = m.get('ApplicationRoleId')

        return self

