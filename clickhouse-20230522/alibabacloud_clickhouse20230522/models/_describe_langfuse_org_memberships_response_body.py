# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeLangfuseOrgMembershipsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeLangfuseOrgMembershipsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeLangfuseOrgMembershipsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLangfuseOrgMembershipsResponseBodyData(DaraModel):
    def __init__(
        self,
        memberships: List[main_models.DescribeLangfuseOrgMembershipsResponseBodyDataMemberships] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of user roles in the organization.
        self.memberships = memberships
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.memberships:
            for v1 in self.memberships:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Memberships'] = []
        if self.memberships is not None:
            for k1 in self.memberships:
                result['Memberships'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.memberships = []
        if m.get('Memberships') is not None:
            for k1 in m.get('Memberships'):
                temp_model = main_models.DescribeLangfuseOrgMembershipsResponseBodyDataMemberships()
                self.memberships.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLangfuseOrgMembershipsResponseBodyDataMemberships(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        email: str = None,
        name: str = None,
        role: str = None,
    ):
        # The time when the user was created.
        self.created_at = created_at
        # The email address of the user.
        self.email = email
        # The username.
        self.name = name
        # The role of the user.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.email is not None:
            result['Email'] = self.email

        if self.name is not None:
            result['Name'] = self.name

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

