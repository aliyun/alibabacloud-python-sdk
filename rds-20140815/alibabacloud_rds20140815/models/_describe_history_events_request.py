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
        # The event status. Valid values:
        # - **Archived**: archived.
        # - **UnArchived**: not archived.
        # - **All**: all.
        self.archive_status = archive_status
        # The system event categorization. Valid values:
        # - **Exception**: abnormal event.
        # - **Optimize**: optimization events.
        # - **Notification**: notification event.
        # - **Maintenance**: scheduled maintenance event.
        self.event_category = event_category
        # The event ID.
        self.event_id = event_id
        # The event level. Valid values:
        # - **INFO**: notification.
        # - **WARN**: warning.
        # - **CRITICAL**: critical.
        self.event_level = event_level
        # The event status. Valid values:
        # - **Inquiring**: inquiring.
        # - **Scheduled**: scheduled.
        # - **Running**: running.
        # - **Succeed**: completed.
        # - **Failed**: failed.
        # - **Canceled**: canceled.
        # > To query multiple statuses, separate them with commas (,).
        self.event_status = event_status
        # The system event type. This parameter takes effect only when InstanceEventType.N is not specified. Valid values: 
        # - **SystemMaintenance.Reboot**: The instance is restarted due to system maintenance.
        # - **SystemMaintenance.Redeploy**: The instance is redeployed due to system maintenance.
        # - **SystemFailure.Reboot**: The instance is restarted due to a system error.
        # - **SystemFailure.Redeploy**: The instance is redeployed due to a system error.
        # - **SystemFailure.Delete**: The instance is released due to an instance creation failure.
        # - **InstanceFailure.Reboot**: The instance is restarted due to an instance error.
        # - **InstanceExpiration.Stop**: The instance is stopped due to subscription expiration.
        # - **InstanceExpiration.Delete**: The instance is released due to subscription expiration.
        # - **AccountUnbalanced.Stop**: The pay-as-you-go instance is stopped due to an overdue payment.
        # - **AccountUnbalanced.Delete**: The pay-as-you-go instance is released due to an overdue payment.
        # > The value of this parameter can only be an instance system event, not a cloud disk system event.
        self.event_type = event_type
        # The beginning of the time range for the task start time. Tasks whose start time is later than this time are queried. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in `UTC +0`. The earliest supported time is 30 days before the current time. If the specified time is more than 30 days before the current time, it is automatically converted to 30 days before the current time.
        # 
        # This parameter is required.
        self.from_start_time = from_start_time
        # The ApsaraDB RDS instance ID.
        self.instance_id = instance_id
        # The page number. The value must be greater than 0 and cannot exceed the maximum value of the integer type. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **30**.
        self.page_size = page_size
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/610399.html) to query the most recent region list.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource type. Valid values:
        # - **Instance**: instance resource.
        # - **Host**: host resource.
        # - **User**: user resource.
        # > If this parameter is not specified, all resource types are queried.
        self.resource_type = resource_type
        self.security_token = security_token
        # The task ID. Specify this parameter to retrieve data for a specific task.
        self.task_id = task_id
        # The end of the time range for the task start time. Tasks whose start time is earlier than this time are queried. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in `UTC +0`.
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

