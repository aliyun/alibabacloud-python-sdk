# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHistoryEventsRequest(DaraModel):
    def __init__(
        self,
        archive_status: str = None,
        event_category: str = None,
        event_id: str = None,
        event_level: str = None,
        event_status: str = None,
        event_type: str = None,
        from_start_time: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        security_token: str = None,
        task_id: str = None,
        to_start_time: str = None,
    ):
        # The resource status. Valid values: **importing**, failed, checksuccess, and deleted.
        self.archive_status = archive_status
        # The system event category. For more information, see [View the event history of an ApsaraDB RDS instance](https://help.aliyun.com/document_detail/129759.html).
        self.event_category = event_category
        # The event ID.
        self.event_id = event_id
        # The event level. Valid values: ***high***, **medium**, and **low**.
        self.event_level = event_level
        # The status of the exception. Valid values:
        # 
        # *   1: pending
        # *   2: ignored
        # *   4: confirmed
        # *   8: marked as false positive
        # *   16: handling
        # *   32: handled
        # *   64: expired
        self.event_status = event_status
        # The system event type. This parameter takes effect only when InstanceEventType.N is not specified. Valid values:
        # 
        # *   SystemMaintenance.Reboot: The instance is restarted due to system maintenance.
        # *   SystemMaintenance.Redeploy: The instance is redeployed due to system maintenance.
        # *   SystemFailure.Reboot: The instance is restarted due to a system error.
        # *   SystemFailure.Redeploy: The instance is redeployed due to a system error.
        # *   SystemFailure.Delete: The instance is released due to an instance creation failure.
        # *   InstanceFailure.Reboot: The instance is restarted due to an instance error.
        # *   InstanceExpiration.Stop: The subscription instance is stopped due to expiration.
        # *   InstanceExpiration.Delete: The subscription instance is released due to expiration.
        # *   AccountUnbalanced.Stop: The pay-as-you-go instance is stopped due to an overdue payment.
        # *   AccountUnbalanced.Delete: The pay-as-you-go instance is released due to an overdue payment.
        # 
        # >  For more information, see Overview. The values of this parameter are applicable only to instance system events, but not to disk system events.
        self.event_type = event_type
        # The beginning of the time range to query. Only tasks that have a start time later than or equal to the time specified by this parameter are queried. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The start time can be up to 30 days earlier than the current time. If you set this parameter to a time more than 30 days earlier than the current time, this time is automatically converted to a time that is exactly 30 days earlier than the current time.
        # 
        # This parameter is required.
        self.from_start_time = from_start_time
        # The instance ID.
        self.instance_id = instance_id
        # The page number. Pages start from page 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: 30.
        self.page_size = page_size
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/610399.html) operation to query the most recent region list.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource type. Set the value to **INSTANCE**.
        self.resource_type = resource_type
        self.security_token = security_token
        # The task ID. This value is used to query the data of a specific task.
        self.task_id = task_id
        # The end of the time range to query. Only tasks that have a start time earlier than or equal to the time specified by this parameter are queried. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.to_start_time = to_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_status is not None:
            result['ArchiveStatus'] = self.archive_status

        if self.event_category is not None:
            result['EventCategory'] = self.event_category

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_status is not None:
            result['EventStatus'] = self.event_status

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.from_start_time is not None:
            result['FromStartTime'] = self.from_start_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.to_start_time is not None:
            result['ToStartTime'] = self.to_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveStatus') is not None:
            self.archive_status = m.get('ArchiveStatus')

        if m.get('EventCategory') is not None:
            self.event_category = m.get('EventCategory')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('FromStartTime') is not None:
            self.from_start_time = m.get('FromStartTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('ToStartTime') is not None:
            self.to_start_time = m.get('ToStartTime')

        return self

