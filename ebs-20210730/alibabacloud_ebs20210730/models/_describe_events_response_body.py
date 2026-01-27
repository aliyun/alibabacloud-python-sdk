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
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The events.
        self.resource_events = resource_events
        # The total number of entries returned.
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
        # The description of the event.
        self.description = description
        # The end time of the event, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
        self.end_time = end_time
        # The level of the event. Valid values:
        # 
        # 1.  INFO
        # 2.  WARN
        # 3.  CRITICAL
        self.event_level = event_level
        # The name of the event. Valid values:
        # 
        # *   NoSnapshot: indicates the event that is triggered because no snapshot is created for a disk to protect data on the disk.
        # *   BurstIOTriggered: indicates the event that is triggered when a burst I/O operation is performed on a disk.
        # *   CostOptimizationNeeded: indicates the event that is triggered when cost optimization is required.
        # *   DiskSpecNotMatchedWithInstance: indicates the event that is triggered because the specifications of a disk do not match the instance to which the disk is attached.
        # *   DiskIONo4kAligned: indicates the event that is triggered because the physical and logical sectors involved in a read or write operation are not 4K aligned.
        # *   DiskIOHang: indicates the event that is triggered when an I/O hang occurs on a disk.
        # *   InstanceIOPSExceedInstanceMaxLimit: indicates the event that is triggered when the number of IOPS on an instance reaches the upper limit.
        # *   InstanceBPSExceedInstanceMaxLimit: indicates the event that is triggered when the number of BPS on an instance reaches the upper limit.
        # *   DiskIOPSExceedInstanceMaxLimit: indicates the event that is triggered when the number of IOPS on a disk reaches the upper limit for the associated instance.
        # *   DiskBPSExceedInstanceMaxLimit: indicates the event that is triggered when the number of BPS on a disk reaches the upper limit for the associated instance.
        # *   DiskIOPSExceedDiskMaxLimit: indicates the event that is triggered when the number of IOPS on a disk reaches the upper limit for the disk.
        # *   DiskBPSExceedDiskMaxLimit: indicates the event that is triggered when the number of BPS on a disk reaches the upper limit for the disk.
        self.event_name = event_name
        # The type of the event. Valid values:
        # 
        # 1.  Notification
        # 2.  SystemException
        # 3.  Alert
        self.event_type = event_type
        # Extra attributes of event, possible fields are:
        # 
        # - EcsInstanceId: ECS instance ID where the cloud disk is mounted;
        # - Adapter: cloud disk mount point.
        self.extra_attributes = extra_attributes
        # The recommended action after the event occurred. Valid values:
        # 
        # *   ModifyDiskSpec
        # *   CreateSnapshot
        # *   ResizeDisk
        # *   AdjustProvision
        # *   ModifyInstanceSpec
        self.recommend_action = recommend_action
        # The codes of the parameters for the recommended action after the event occurred.
        self.recommend_params = recommend_params
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type
        # The start time of the event, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.
        self.start_time = start_time
        # The status of the event. Valid values:
        # 
        # 1.  WillExecute
        # 2.  Executing
        # 3.  Executed
        # 4.  Ignore
        # 5.  Expired
        # 6.  Deleted
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

