# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeContainerResourceRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The page number for paged queries. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Minimum value: 1. Maximum value: 99. Default value: 10.
        self.page_size = page_size
        # The resource ID.
        # 
        # - **ResourceType=PV**: The persistent volume ID.
        self.resource_id = resource_id
        # The resource type. Valid value:
        # 
        # - **PV**: persistent volume (PV).
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

