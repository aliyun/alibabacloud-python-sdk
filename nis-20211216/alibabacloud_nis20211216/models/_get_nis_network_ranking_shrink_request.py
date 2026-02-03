# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetNisNetworkRankingShrinkRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        begin_time: int = None,
        direction: str = None,
        end_time: int = None,
        filter_shrink: str = None,
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
        self.filter_shrink = filter_shrink
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
        pass

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

        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink

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

        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')

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

