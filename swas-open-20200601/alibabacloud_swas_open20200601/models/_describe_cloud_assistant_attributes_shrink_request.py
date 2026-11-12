# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudAssistantAttributesShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_ids_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The instance IDs of the simple application server instances.
        # 
        # This parameter is required.
        self.instance_ids_shrink = instance_ids_shrink
        # The page number.
        # 
        # Minimum value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID of the simple application servers.
        # You can call [ListRegions](https://help.aliyun.com/document_detail/189315.html) to query the list of supported Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

