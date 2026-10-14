# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDDoSEventsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. This is a UNIX timestamp. Unit: seconds.
        # 
        # > The timestamp must be on the minute.
        self.end_time = end_time
        # The IDs of the Anti-DDoS Pro or Anti-DDoS Premium instances.
        # 
        # > Call [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) to query the IDs of all Anti-DDoS Pro and Anti-DDoS Premium instances.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The number of the page to return. For example, to query the first page, set this parameter to **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the resource group in Resource Management to which the Anti-DDoS Pro or Anti-DDoS Premium instance belongs. By default, this parameter is empty, which means that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. This is a UNIX timestamp. Unit: seconds.
        # 
        # > The timestamp must be on the minute.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

