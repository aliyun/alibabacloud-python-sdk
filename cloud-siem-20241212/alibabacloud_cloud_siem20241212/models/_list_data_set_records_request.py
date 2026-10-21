# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataSetRecordsRequest(DaraModel):
    def __init__(
        self,
        data_set_id: str = None,
        filter: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        order_field: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The ID of the dataset.
        # 
        # This parameter is required.
        self.data_set_id = data_set_id
        # The JSON string for field fuzzy match. Example:
        # {"field1":"value1","field2":"value2"}
        self.filter = filter
        # The language of the response message. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The maximum number of results to return per query when you use the NextToken parameter. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The token used to start the next query.
        self.next_token = next_token
        # The sort direction. Valid values:
        # - "desc" (default): Descending order.
        # - "asc": Ascending order.
        self.order = order
        # The field by which to sort. Valid values:
        # - "updatetime" (default): Update time.
        # - "createtime": Creation time.
        self.order_field = order_field
        # The current page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region where the data management center for threat analysis is located. Select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland.
        # - ap-southeast-1: Assets are located outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the user whose perspective the administrator switches to.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_set_id is not None:
            result['DataSetId'] = self.data_set_id

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.order_field is not None:
            result['OrderField'] = self.order_field

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSetId') is not None:
            self.data_set_id = m.get('DataSetId')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

