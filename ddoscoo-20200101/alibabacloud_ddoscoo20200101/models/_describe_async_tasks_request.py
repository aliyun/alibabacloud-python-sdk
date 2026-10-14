# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAsyncTasksRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        # The page number for the paged query.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of asynchronous export tasks to return on each page for the paged query.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The resource group ID of the Anti-DDoS instance in Resource Management.
        # 
        # If this parameter is not specified, the default resource group is used.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

