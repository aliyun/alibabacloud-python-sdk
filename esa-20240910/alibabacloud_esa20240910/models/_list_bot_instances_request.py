# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBotInstancesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
        status: str = None,
    ):
        # The instance ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the ID.
        self.instance_id = instance_id
        # The page number for the paged query. Settings this parameter for paging. Default value: 1. Valid values: 1 to 100000.
        self.page_number = page_number
        # The number of entries per page for the paged query. This parameter is used for paging. Valid values: 1 to 500.
        self.page_size = page_size
        # The field by which to sort the results. By default, the results are sorted by purchase time. Valid values:
        # 
        # - **CreateTime**: purchase time.
        # - **ExpireTime**: expiration time.
        self.sort_by = sort_by
        # The sort order. Default value: desc. Valid values:
        # 
        # - **asc**: ascending order.
        # - **desc**: descending order.
        self.sort_order = sort_order
        # The instance status. Valid values:
        # - **online**: The instance is running normally.
        # - **offline**: The instance has expired but has not exceeded the retention period and is unavailable.
        # - **disable**: The instance has been released.
        # - **overdue**: The instance has an overdue payment.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

