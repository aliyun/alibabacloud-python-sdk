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
        # The tags. Tags are used to filter alerts, and each alert can be marked with special tags.
        # 
        # Currently, only filtering by product is supported. That is, the `name` is `product`. For example: {"name":"product","value":"ECS"}.
        # >We do not recommend that you use the special tags for the CloudMonitor console in Alibaba Cloud.
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
        # >Currently, Alibaba Cloud does not impose a limit on this parameter. If you need to obtain all results, set the page size to a large value.
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

