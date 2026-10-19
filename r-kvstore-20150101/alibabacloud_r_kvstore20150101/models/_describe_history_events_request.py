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
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        security_token: str = None,
        task_id: str = None,
        to_start_time: str = None,
    ):
        # The archive status of the event. Valid values:
        # - **Archived**: The event is archived.
        # - **UnArchived**: The event is not archived.
        # - **All**: All events.
        self.archive_status = archive_status
        # The category of the system event. Valid values:
        # - **Exception**: Exception events.
        # - **Optimize**: Optimization events.
        # - **Notification**: Notification events.
        # - **Maintenance**: Scheduled O&M events.
        self.event_category = event_category
        # The ID of the event.
        self.event_id = event_id
        # The event level. Valid values:
        # - **INFO**: Information.
        # - **WARN**: Warning.
        # - **CRITICAL**: Critical.
        self.event_level = event_level
        # The status of the event. Valid values:
        # - **Inquiring**: Inquiring.
        # - **Scheduled**: Scheduled.
        # - **Running**: Running.
        # - **Succeed**: Succeeded.
        # - **Failed**: Failed.
        # - **Canceled**: Canceled.
        # > To query events in multiple statuses, separate the statuses with commas (,).
        self.event_status = event_status
        # The type of the system event. The EventType parameter is valid only when the InstanceEventType.N parameter is not specified. Valid values: 
        # 
        # - SystemMaintenance.Reboot: The instance is restarted due to system maintenance.
        # - SystemMaintenance.Redeploy: The instance is redeployed due to system maintenance.
        # - SystemFailure.Reboot: The instance is restarted due to a system failure.
        # - SystemFailure.Redeploy: The instance is redeployed due to a system failure.
        # - SystemFailure.Delete: The instance is released due to a creation failure.
        # - InstanceFailure.Reboot: The instance is restarted due to an instance failure.
        # - InstanceExpiration.Stop: The subscription instance is stopped due to expiration.
        # - InstanceExpiration.Delete: The subscription instance is released due to expiration.
        # - AccountUnbalanced.Stop: The pay-as-you-go instance is stopped due to an overdue payment.
        # - AccountUnbalanced.Delete: The pay-as-you-go instance is released due to an overdue payment.
        # 
        # > For more information about event types, see [Overview of system events](https://help.aliyun.com/document_detail/66574.html). The value of this parameter can only be an instance system event, not a cloud disk system event.
        self.event_type = event_type
        # The earliest start time of the query task. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.from_start_time = from_start_time
        # The instance ID.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be greater than 0 and less than or equal to the maximum integer value. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/473763.html) operation to query the region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource. Valid values:
        # - **Instance**: Instance resources.
        # - **Host**: Host resources.
        # - **User**: User resources.
        # > If you do not specify this parameter, all resource types are queried.
        self.resource_type = resource_type
        self.security_token = security_token
        # The ID of the task.
        self.task_id = task_id
        # The latest start time of the query task. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC and later than the earliest start time of the task.
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

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

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

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('ToStartTime') is not None:
            self.to_start_time = m.get('ToStartTime')

        return self

