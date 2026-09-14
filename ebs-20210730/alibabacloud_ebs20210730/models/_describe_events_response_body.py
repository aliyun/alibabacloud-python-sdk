# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeEventsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_events: List[main_models.DescribeEventsResponseBodyResourceEvents] = None,
        total_count: int = None,
    ):
        # The token for the next query. If NextToken is empty, no more results exist.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The list of events.
        self.resource_events = resource_events
        # The total number of entries returned for the paged query.
        self.total_count = total_count

    def validate(self):
        if self.resource_events:
            for v1 in self.resource_events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceEvents'] = []
        if self.resource_events is not None:
            for k1 in self.resource_events:
                result['ResourceEvents'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_events = []
        if m.get('ResourceEvents') is not None:
            for k1 in m.get('ResourceEvents'):
                temp_model = main_models.DescribeEventsResponseBodyResourceEvents()
                self.resource_events.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEventsResponseBodyResourceEvents(DaraModel):
    def __init__(
        self,
        description: str = None,
        end_time: str = None,
        event_level: str = None,
        event_name: str = None,
        event_type: str = None,
        extra_attributes: str = None,
        recommend_action: str = None,
        recommend_params: str = None,
        resource_id: str = None,
        resource_type: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The event description.
        self.description = description
        # The end time of the event. This value is a timestamp in milliseconds.
        self.end_time = end_time
        # The event level. Valid values:
        # 
        # 1. INFO
        # 2. WARN
        # 3. CRITICAL
        self.event_level = event_level
        # The event name. Valid values:
        # 
        # - NoSnapshot: data protection
        # - BurstIOTriggered: burst I/O
        # - CostOptimizationNeeded: cost optimization
        # - DiskSpecNotMatchedWithInstance: instance and disk specification mismatch
        # - DiskIONo4kAligned: non-4K aligned read/write
        # - DiskIOHang: disk IOHang occurred
        # - InstanceIOPSExceedInstanceMaxLimit: instance IOPS reached the upper limit
        # - InstanceBPSExceedInstanceMaxLimit: instance BPS reached the upper limit
        # - DiskIOPSExceedInstanceMaxLimit: disk IOPS reached the instance upper limit
        # - DiskBPSExceedInstanceMaxLimit: disk BPS reached the instance upper limit
        # - DiskIOPSExceedDiskMaxLimit: disk IOPS reached the disk upper limit
        # - DiskBPSExceedDiskMaxLimit: disk BPS reached the disk upper limit
        self.event_name = event_name
        # The event type. Valid values:
        # 1. Notification
        # 2. SystemException
        # 3. Alert
        self.event_type = event_type
        # The additional properties. Possible fields:
        # 
        # - EcsInstanceId: the ID of the ECS instance to which the cloud disk is attached.
        # - Adapter: the mount point of the cloud disk.
        self.extra_attributes = extra_attributes
        # The recommended action after the event occurs. Valid values:
        # 
        # - ModifyDiskSpec: change disk specifications
        # - CreateSnapshot: create a snapshot
        # - ResizeDisk: expand disk capacity
        # - AdjustProvision: adjust provisioned performance
        # - ModifyInstanceSpec: change instance specifications
        self.recommend_action = recommend_action
        # The parameters for the recommended action after the event occurs.
        self.recommend_params = recommend_params
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type
        # The start time of the event. This value is a timestamp in milliseconds.
        self.start_time = start_time
        # The event status. Valid values:
        # 1. WillExecute: pending
        # 2. Executing: processing
        # 3. Executed: processed
        # 4. Ignore: ignored
        # 5. Expired: expired
        # 6. Deleted: deleted
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.extra_attributes is not None:
            result['ExtraAttributes'] = self.extra_attributes

        if self.recommend_action is not None:
            result['RecommendAction'] = self.recommend_action

        if self.recommend_params is not None:
            result['RecommendParams'] = self.recommend_params

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('ExtraAttributes') is not None:
            self.extra_attributes = m.get('ExtraAttributes')

        if m.get('RecommendAction') is not None:
            self.recommend_action = m.get('RecommendAction')

        if m.get('RecommendParams') is not None:
            self.recommend_params = m.get('RecommendParams')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

