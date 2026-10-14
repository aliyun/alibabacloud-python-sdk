# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribePortFlowListRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_ids: List[str] = None,
        interval: int = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The end time of the query. Specify the value as a UNIX timestamp. Unit: seconds.
        # 
        # > The value must be on the minute.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the Anti-DDoS Pro and Anti-DDoS Premium instance.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The interval at which data is returned. Unit: seconds. The supported interval values vary based on the query time range (determined by **StartTime** and **EndTime**). Recommended settings:
        # 
        # - Query time range ≤ 1 hour: minimum interval of 60 seconds, maximum not exceeding the query time range.
        # - Query time range > 1 hour and ≤ 6 hours: minimum interval of 600 seconds, maximum not exceeding the query time range.
        # - Query time range > 6 hours and ≤ 24 hours: minimum interval of 1800 seconds, maximum not exceeding the query time range.
        # - Query time range > 24 hours and ≤ 7 days: minimum interval of 3600 seconds, maximum not exceeding the query time range.
        # - Query time range > 7 days and ≤ 15 days: minimum interval of 14400 seconds, maximum not exceeding the query time range.
        # - Query time range > 15 days: minimum interval of 43200 seconds, maximum not exceeding the query time range.
        # 
        # This parameter is required.
        self.interval = interval
        # The ID of the resource group to which the Anti-DDoS Pro and Anti-DDoS Premium instance belongs in Resource Management. By default, this parameter is empty, which indicates that the instance belongs to the default resource group.
        # 
        # For more information about resource groups, see [Create a resource group](https://help.aliyun.com/document_detail/94485.html).
        self.resource_group_id = resource_group_id
        # The start time of the query. Specify the value as a UNIX timestamp. Unit: seconds.
        # 
        # > The value must be on the minute.
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

        if self.interval is not None:
            result['Interval'] = self.interval

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

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

