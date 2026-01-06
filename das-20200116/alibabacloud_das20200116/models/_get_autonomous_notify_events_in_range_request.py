# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAutonomousNotifyEventsInRangeRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        event_context: str = None,
        instance_id: str = None,
        level: str = None,
        min_level: str = None,
        node_id: str = None,
        page_offset: str = None,
        page_size: str = None,
        start_time: str = None,
        context: str = None,
    ):
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  The end time must be later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The reserved parameter.
        self.event_context = event_context
        # The instance ID.
        self.instance_id = instance_id
        # The urgency level of the events. If you specify this parameter, the MinLevel parameter does not take effect. Valid values:
        # 
        # *   **Notice**: events for which the system sends notifications.
        # *   **Optimization**: events that need to be optimized.
        # *   **Warn**: events for which the system sends warnings.
        # *   **Critical**: critical events.
        self.level = level
        # The minimum urgency level of the events. Valid values:
        # 
        # *   **Notice**: events for which the system sends notifications.
        # *   **Optimization**: events that need to be optimized.
        # *   **Warn**: events for which the system sends warnings.
        # *   **Critical**: critical events.
        self.min_level = min_level
        # The ID of the node in a PolarDB for MySQL cluster. You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the node ID returned by the DBNodeId response parameter.
        # 
        # >  You must specify the node ID if your database instance is a PolarDB for MySQL cluster.
        self.node_id = node_id
        # The page number. The value must be a positive integer. Default value: 1.
        self.page_offset = page_offset
        # The number of entries per page.
        self.page_size = page_size
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The reserved parameter.
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_context is not None:
            result['EventContext'] = self.event_context

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.level is not None:
            result['Level'] = self.level

        if self.min_level is not None:
            result['MinLevel'] = self.min_level

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.page_offset is not None:
            result['PageOffset'] = self.page_offset

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.context is not None:
            result['__context'] = self.context

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventContext') is not None:
            self.event_context = m.get('EventContext')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MinLevel') is not None:
            self.min_level = m.get('MinLevel')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PageOffset') is not None:
            self.page_offset = m.get('PageOffset')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('__context') is not None:
            self.context = m.get('__context')

        return self

