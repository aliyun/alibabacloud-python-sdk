# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class ListIdentityProviderDepartmentsResponseBody(DaraModel):
    def __init__(
        self,
        departments: List[main_models.ListIdentityProviderDepartmentsResponseBodyDepartments] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.departments = departments
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.departments:
            for v1 in self.departments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Departments'] = []
        if self.departments is not None:
            for k1 in self.departments:
                result['Departments'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.departments = []
        if m.get('Departments') is not None:
            for k1 in m.get('Departments'):
                temp_model = main_models.ListIdentityProviderDepartmentsResponseBodyDepartments()
                self.departments.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListIdentityProviderDepartmentsResponseBodyDepartments(DaraModel):
    def __init__(
        self,
        has_children: bool = None,
        id: str = None,
        member_count: int = None,
        name: str = None,
        parent_id: str = None,
    ):
        self.has_children = has_children
        self.id = id
        self.member_count = member_count
        self.name = name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_children is not None:
            result['HasChildren'] = self.has_children

        if self.id is not None:
            result['Id'] = self.id

        if self.member_count is not None:
            result['MemberCount'] = self.member_count

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasChildren') is not None:
            self.has_children = m.get('HasChildren')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        return self

