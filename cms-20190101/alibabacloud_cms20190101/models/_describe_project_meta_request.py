# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeProjectMetaRequest(DaraModel):
    def __init__(
        self,
        labels: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The tags. Tags are used to filter services.
        # 
        # You can filter services only by the tag whose `name` is `product`. Example: {"name":"product","value":"ECS"}.
        # 
        # > We recommend that you do not use the special tags in the CloudMonitor console.
        self.labels = labels
        # The page number.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 10000.
        # 
        # Default value: 30.
        # 
        # > The value of this parameter is not limited. You can view a large number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.labels is not None:
            result['Labels'] = self.labels

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

