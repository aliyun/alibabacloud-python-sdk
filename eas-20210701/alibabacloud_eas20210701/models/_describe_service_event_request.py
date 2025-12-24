# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeServiceEventRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        event_type: str = None,
        instance_name: str = None,
        page_num: str = None,
        page_size: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. By default, the current point in time is the end of the time range to query.
        self.end_time = end_time
        # The event type. Valid values:
        # 
        # *   Normal
        # *   Warning
        self.event_type = event_type
        # The instance name. For more information about how to obtain the instance name, see [ListServiceInstances](https://help.aliyun.com/document_detail/412108.html).
        self.instance_name = instance_name
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        # The beginning of the time range to query. The time must be in UTC. The default value is seven days ago.
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

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

