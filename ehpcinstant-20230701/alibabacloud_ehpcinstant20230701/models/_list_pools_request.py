# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class ListPoolsRequest(DaraModel):
    def __init__(
        self,
        filter: main_models.ListPoolsRequestFilter = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The filter conditions for querying resource pools.
        self.filter = filter
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 50. Default value: 10.
        self.page_size = page_size

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = main_models.ListPoolsRequestFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListPoolsRequestFilter(DaraModel):
    def __init__(
        self,
        pool_name: List[str] = None,
        status: List[str] = None,
        time_created_after: int = None,
        time_created_before: int = None,
    ):
        # The list of resource pool names to query.
        self.pool_name = pool_name
        # The list of resource pool statuses to query.
        self.status = status
        # Returns only resource pools created after the specified time. The time must be a Unix timestamp in UTC+8.
        self.time_created_after = time_created_after
        # Returns only resource pools created before the specified time. The time must be a Unix timestamp in UTC+8.
        self.time_created_before = time_created_before

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name

        if self.status is not None:
            result['Status'] = self.status

        if self.time_created_after is not None:
            result['TimeCreatedAfter'] = self.time_created_after

        if self.time_created_before is not None:
            result['TimeCreatedBefore'] = self.time_created_before

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeCreatedAfter') is not None:
            self.time_created_after = m.get('TimeCreatedAfter')

        if m.get('TimeCreatedBefore') is not None:
            self.time_created_before = m.get('TimeCreatedBefore')

        return self

