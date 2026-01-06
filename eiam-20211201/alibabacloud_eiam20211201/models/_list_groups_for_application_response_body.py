# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListGroupsForApplicationResponseBody(DaraModel):
    def __init__(
        self,
        groups: List[main_models.ListGroupsForApplicationResponseBodyGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The group IDs.
        self.groups = groups
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.ListGroupsForApplicationResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListGroupsForApplicationResponseBodyGroups(DaraModel):
    def __init__(
        self,
        application_roles: List[main_models.ListGroupsForApplicationResponseBodyGroupsApplicationRoles] = None,
        group_id: str = None,
    ):
        # 应用角色列表。
        self.application_roles = application_roles
        # The group ID.
        self.group_id = group_id

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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_roles = []
        if m.get('ApplicationRoles') is not None:
            for k1 in m.get('ApplicationRoles'):
                temp_model = main_models.ListGroupsForApplicationResponseBodyGroupsApplicationRoles()
                self.application_roles.append(temp_model.from_map(k1))

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        return self

class ListGroupsForApplicationResponseBodyGroupsApplicationRoles(DaraModel):
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

