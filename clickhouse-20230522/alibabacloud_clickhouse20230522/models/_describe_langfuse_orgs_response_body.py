# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeLangfuseOrgsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeLangfuseOrgsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
            temp_model = main_models.DescribeLangfuseOrgsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLangfuseOrgsResponseBodyData(DaraModel):
    def __init__(
        self,
        organizations: List[main_models.DescribeLangfuseOrgsResponseBodyDataOrganizations] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.organizations = organizations
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.organizations:
            for v1 in self.organizations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Organizations'] = []
        if self.organizations is not None:
            for k1 in self.organizations:
                result['Organizations'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.organizations = []
        if m.get('Organizations') is not None:
            for k1 in m.get('Organizations'):
                temp_model = main_models.DescribeLangfuseOrgsResponseBodyDataOrganizations()
                self.organizations.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLangfuseOrgsResponseBodyDataOrganizations(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        name: str = None,
        organization_id: str = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.name = name
        self.organization_id = organization_id
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.name is not None:
            result['Name'] = self.name

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

