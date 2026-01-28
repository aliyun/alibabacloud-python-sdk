# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryDomainGroupListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QueryDomainGroupListResponseBodyData = None,
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
            temp_model = main_models.QueryDomainGroupListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryDomainGroupListResponseBodyData(DaraModel):
    def __init__(
        self,
        domain_group: List[main_models.QueryDomainGroupListResponseBodyDataDomainGroup] = None,
    ):
        self.domain_group = domain_group

    def validate(self):
        if self.domain_group:
            for v1 in self.domain_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainGroup'] = []
        if self.domain_group is not None:
            for k1 in self.domain_group:
                result['DomainGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_group = []
        if m.get('DomainGroup') is not None:
            for k1 in m.get('DomainGroup'):
                temp_model = main_models.QueryDomainGroupListResponseBodyDataDomainGroup()
                self.domain_group.append(temp_model.from_map(k1))

        return self

class QueryDomainGroupListResponseBodyDataDomainGroup(DaraModel):
    def __init__(
        self,
        being_deleted: bool = None,
        creation_date: str = None,
        domain_group_id: str = None,
        domain_group_name: str = None,
        domain_group_status: str = None,
        modification_date: str = None,
        total_number: int = None,
    ):
        self.being_deleted = being_deleted
        self.creation_date = creation_date
        self.domain_group_id = domain_group_id
        self.domain_group_name = domain_group_name
        self.domain_group_status = domain_group_status
        self.modification_date = modification_date
        self.total_number = total_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.being_deleted is not None:
            result['BeingDeleted'] = self.being_deleted

        if self.creation_date is not None:
            result['CreationDate'] = self.creation_date

        if self.domain_group_id is not None:
            result['DomainGroupId'] = self.domain_group_id

        if self.domain_group_name is not None:
            result['DomainGroupName'] = self.domain_group_name

        if self.domain_group_status is not None:
            result['DomainGroupStatus'] = self.domain_group_status

        if self.modification_date is not None:
            result['ModificationDate'] = self.modification_date

        if self.total_number is not None:
            result['TotalNumber'] = self.total_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeingDeleted') is not None:
            self.being_deleted = m.get('BeingDeleted')

        if m.get('CreationDate') is not None:
            self.creation_date = m.get('CreationDate')

        if m.get('DomainGroupId') is not None:
            self.domain_group_id = m.get('DomainGroupId')

        if m.get('DomainGroupName') is not None:
            self.domain_group_name = m.get('DomainGroupName')

        if m.get('DomainGroupStatus') is not None:
            self.domain_group_status = m.get('DomainGroupStatus')

        if m.get('ModificationDate') is not None:
            self.modification_date = m.get('ModificationDate')

        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')

        return self

