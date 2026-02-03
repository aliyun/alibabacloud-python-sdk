# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class GetNisNetworkRankingRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        begin_time: int = None,
        direction: str = None,
        end_time: int = None,
        filter: List[main_models.GetNisNetworkRankingRequestFilter] = None,
        group_by: str = None,
        order_by: str = None,
        region_no: str = None,
        resource_type: str = None,
        sort: str = None,
        top_n: int = None,
        use_cross_account: bool = None,
    ):
        self.account_ids = account_ids
        self.begin_time = begin_time
        # This parameter is required.
        self.direction = direction
        self.end_time = end_time
        self.filter = filter
        # This parameter is required.
        self.group_by = group_by
        # This parameter is required.
        self.order_by = order_by
        # This parameter is required.
        self.region_no = region_no
        # This parameter is required.
        self.resource_type = resource_type
        self.sort = sort
        self.top_n = top_n
        self.use_cross_account = use_cross_account

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.group_by is not None:
            result['GroupBy'] = self.group_by

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.top_n is not None:
            result['TopN'] = self.top_n

        if self.use_cross_account is not None:
            result['UseCrossAccount'] = self.use_cross_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.GetNisNetworkRankingRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')

        if m.get('UseCrossAccount') is not None:
            self.use_cross_account = m.get('UseCrossAccount')

        return self

class GetNisNetworkRankingRequestFilter(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

