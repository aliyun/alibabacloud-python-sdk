# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOpEntitiesRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        entity_object: str = None,
        entity_type: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # > The time must be in the latest 30 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The operation object that you want to query.
        self.entity_object = entity_object
        # The type of the operation object that you want to query. Valid values:
        # 
        # *   **1**: the IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance
        # *   **2**: Anti-DDoS plans
        # *   **3**: ECS instances
        # *   **4**: all logs
        self.entity_type = entity_type
        # The number of the page to return. For example, to query the returned results on the first page, set the value to **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **50**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # > The time must be in the latest 30 days.
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

        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

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

        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

