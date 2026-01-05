# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOrdersRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        order_status: str = None,
        page_number: int = None,
        page_size: int = None,
        product_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.category = category
        self.instance_id = instance_id
        self.max_results = max_results
        self.next_token = next_token
        self.order_status = order_status
        self.page_number = page_number
        self.page_size = page_size
        self.product_code = product_code
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

