# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        event_level: str = None,
        event_name: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The end time of the event. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The event level. Valid values:
        # - **INFO**: Notification.
        # - **WARN**: Warning.
        # - **CRITICAL**: Critical.
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
        # The maximum number of entries per page for a paged query. If you specify this parameter, the `MaxResults` and `NextToken` parameters are used together for the query.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous API call.
        self.next_token = next_token
        # The region ID. You can call DescribeRegions to query the list of regions supported by EBS Lens.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource ID.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # - disk: cloud disk
        self.resource_type = resource_type
        # The start time of the event. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The event status. Valid values:
        # - WillExecute: pending 
        # - Executing: processing
        # - Executed: processed
        # - Ignore: ignored
        # - Expired: expired
        # - Deleted: deleted
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

