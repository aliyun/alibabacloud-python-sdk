# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSystemLogRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        entity_object: str = None,
        entity_type: int = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        # The end of the time range to query. The bills of the burstable clean bandwidth that are issued before this point in time are queried. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The IP address of the instance.
        # 
        # > You can call the [DescribeInstanceDetails](https://help.aliyun.com/document_detail/91490.html) operation to query the IP addresses of all instances.
        self.entity_object = entity_object
        # The type of the system log. Set the value to **20**, which indicates the billing logs for the burstable clean bandwidth.
        # 
        # > You must specify this parameter. Otherwise, the call fails.
        self.entity_type = entity_type
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The beginning of the time range to query. The bills of the burstable clean bandwidth that are issued after this point in time are queried. The value is a UNIX timestamp. Unit: milliseconds.
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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

