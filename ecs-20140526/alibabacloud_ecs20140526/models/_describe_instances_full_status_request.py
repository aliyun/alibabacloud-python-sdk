# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesFullStatusRequest(DaraModel):
    def __init__(
        self,
        event_publish_time: main_models.DescribeInstancesFullStatusRequestEventPublishTime = None,
        not_before: main_models.DescribeInstancesFullStatusRequestNotBefore = None,
        event_id: List[str] = None,
        event_type: str = None,
        health_status: str = None,
        instance_event_type: List[str] = None,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
    ):
        self.event_publish_time = event_publish_time
        self.not_before = not_before
        # The IDs of the system events. You can specify up to 100 event IDs in a single request.
        self.event_id = event_id
        # The type of the system event. This parameter is valid only when InstanceEventType.N is not specified. Valid values:
        # 
        # *   SystemMaintenance.Reboot: The instance is restarted due to system maintenance.
        # *   SystemFailure.Reboot: The instance is restarted due to a system failure.
        # *   InstanceFailure.Reboot: The instance is restarted due to an instance failure.
        # *   InstanceExpiration.Stop: The subscription instance is stopped due to expiration.
        # *   InstanceExpiration.Delete: The subscription instance is released due to expiration.
        # *   AccountUnbalanced.Stop: The pay-as-you-go instance is stopped due to an overdue payment.
        # *   AccountUnbalanced.Delete: The pay-as-you-go instance is released due to an overdue payment.
        self.event_type = event_type
        # The health status of the instance. Valid values:
        # 
        # *   Impaired
        # *   Warning: The instance performance may be degraded due to maintenance or technical issues.
        # *   Maintaining
        # *   Initializing
        # *   InsufficientData
        # *   NotApplicable
        # 
        # All the values are case-sensitive.
        self.health_status = health_status
        # The types of system events. You can specify up to 30 event types in a single request.
        self.instance_event_type = instance_event_type
        # The IDs of the instances. You can specify up to 100 instance IDs in a single request.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be a positive integer.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The lifecycle status of the instance. Valid values:
        # 
        # *   Starting
        # *   Running
        # *   Stopped
        self.status = status

    def validate(self):
        if self.event_publish_time:
            self.event_publish_time.validate()
        if self.not_before:
            self.not_before.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_publish_time is not None:
            result['EventPublishTime'] = self.event_publish_time.to_map()

        if self.not_before is not None:
            result['NotBefore'] = self.not_before.to_map()

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.instance_event_type is not None:
            result['InstanceEventType'] = self.instance_event_type

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

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventPublishTime') is not None:
            temp_model = main_models.DescribeInstancesFullStatusRequestEventPublishTime()
            self.event_publish_time = temp_model.from_map(m.get('EventPublishTime'))

        if m.get('NotBefore') is not None:
            temp_model = main_models.DescribeInstancesFullStatusRequestNotBefore()
            self.not_before = temp_model.from_map(m.get('NotBefore'))

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('InstanceEventType') is not None:
            self.instance_event_type = m.get('InstanceEventType')

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

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeInstancesFullStatusRequestNotBefore(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        # The end of the time range during which O\\&M tasks related to scheduled system events are executed. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end = end
        # The beginning of the time range during which O\\&M tasks related to scheduled system events are executed. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class DescribeInstancesFullStatusRequestEventPublishTime(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        # The end of the time range during which system events are published. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end = end
        # The beginning of the time range during which system events are published. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

