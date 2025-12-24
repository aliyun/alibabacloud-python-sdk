# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceHistoryEventsRequest(DaraModel):
    def __init__(
        self,
        event_publish_time: main_models.DescribeInstanceHistoryEventsRequestEventPublishTime = None,
        not_before: main_models.DescribeInstanceHistoryEventsRequestNotBefore = None,
        event_cycle_status: str = None,
        event_id: List[str] = None,
        event_type: str = None,
        impact_level: str = None,
        instance_event_cycle_status: List[str] = None,
        instance_event_type: List[str] = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[main_models.DescribeInstanceHistoryEventsRequestTag] = None,
    ):
        self.event_publish_time = event_publish_time
        self.not_before = not_before
        # The lifecycle state of the system event. This parameter takes effect only when InstanceEventCycleStatus.N is not specified. Valid values:
        # 
        # *   Scheduled
        # *   Avoided
        # *   Executing
        # *   Executed
        # *   Canceled
        # *   Failed
        # *   Inquiring
        self.event_cycle_status = event_cycle_status
        # The ID of system event N. Valid values of N: 1 to 100. You can repeat this parameter to pass multiple values.
        self.event_id = event_id
        # The type of the system event. This parameter takes effect only when InstanceEventType.N is not specified. Valid values:
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
        # >  For more information, see [Overview](https://help.aliyun.com/document_detail/66574.html). The values of this parameter are applicable only to instance system events, but not to disk system events.
        self.event_type = event_type
        # >  This parameter is not publicly available.
        self.impact_level = impact_level
        # The lifecycle state of system event N. Valid values of N: 1 to 7. You can repeat this parameter to pass multiple values. Valid values:
        # 
        # *   Scheduled
        # *   Avoided
        # *   Executing
        # *   Executed
        # *   Canceled
        # *   Failed
        # *   Inquiring
        self.instance_event_cycle_status = instance_event_cycle_status
        # The type of system event N. Valid values of N: 1 to 30. You can repeat this parameter to pass multiple values. Valid values:
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
        # >  For more information, see [Overview](https://help.aliyun.com/document_detail/66574.html). The values of this parameter are applicable only to instance system events, but not to disk system events.
        self.instance_event_type = instance_event_type
        # The ID of the instance. If this parameter is not specified, the system events of all instances in the specified region are queried.
        self.instance_id = instance_id
        # The number of entries to return on each page. Valid values: 10 to 100.
        # 
        # Default values:
        # 
        # *   If you set a value greater than 0 and less than 10, the default value is 10.
        # *   If you set this parameter to a value that is greater than 100, the default value is 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # >  This parameter is deprecated. We recommend that you specify MaxResults or NextToken for a paged query.
        self.page_number = page_number
        # >  This parameter is deprecated. We recommend that you specify MaxResults or NextToken for a paged query.
        self.page_size = page_size
        # The region ID of the resource. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the resource belongs.
        self.resource_group_id = resource_group_id
        # The ID of resource N. Valid values of N: 1 to 100. You can repeat this parameter to pass multiple values. Valid values:
        # 
        # *   When `ResourceType` is set to instance, ResourceId.N specifies the ID of instance N.
        # *   When `ResourceType` is set to ddh, ResourceId.N specifies the ID of dedicated host N.
        # *   When `ResourceType` is set to managedhost, ResourceId.N specifies the ID of physical machine N from a smart hosting pool.
        # 
        # If this parameter is not specified, the system events of all resources of the type specified by `ResourceType` in the region specified by `RegionId` are queried.
        # 
        # >  We recommend that you use `ResourceId.N` to specify one or more resource IDs. If you specify both `ResourceId.N` and `InstanceId`, `ResourceId.N` takes precedence by default.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the resource. Valid values:
        # 
        # *   instance: ECS instance
        # *   ddh: dedicated host
        # *   managehost: physical machine in a smart hosting pool
        # 
        # Default value: instance.
        self.resource_type = resource_type
        # The list of tags.
        self.tag = tag

    def validate(self):
        if self.event_publish_time:
            self.event_publish_time.validate()
        if self.not_before:
            self.not_before.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_publish_time is not None:
            result['EventPublishTime'] = self.event_publish_time.to_map()

        if self.not_before is not None:
            result['NotBefore'] = self.not_before.to_map()

        if self.event_cycle_status is not None:
            result['EventCycleStatus'] = self.event_cycle_status

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.impact_level is not None:
            result['ImpactLevel'] = self.impact_level

        if self.instance_event_cycle_status is not None:
            result['InstanceEventCycleStatus'] = self.instance_event_cycle_status

        if self.instance_event_type is not None:
            result['InstanceEventType'] = self.instance_event_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventPublishTime') is not None:
            temp_model = main_models.DescribeInstanceHistoryEventsRequestEventPublishTime()
            self.event_publish_time = temp_model.from_map(m.get('EventPublishTime'))

        if m.get('NotBefore') is not None:
            temp_model = main_models.DescribeInstanceHistoryEventsRequestNotBefore()
            self.not_before = temp_model.from_map(m.get('NotBefore'))

        if m.get('EventCycleStatus') is not None:
            self.event_cycle_status = m.get('EventCycleStatus')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('ImpactLevel') is not None:
            self.impact_level = m.get('ImpactLevel')

        if m.get('InstanceEventCycleStatus') is not None:
            self.instance_event_cycle_status = m.get('InstanceEventCycleStatus')

        if m.get('InstanceEventType') is not None:
            self.instance_event_type = m.get('InstanceEventType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

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

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeInstanceHistoryEventsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInstanceHistoryEventsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N of the resource.
        self.key = key
        # The value of tag N of the resource.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeInstanceHistoryEventsRequestNotBefore(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        # The latest scheduled end time for the system event. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end = end
        # The earliest scheduled start time for the system event. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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

class DescribeInstanceHistoryEventsRequestEventPublishTime(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        # The end of the time range in which to query published system events. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end = end
        # The beginning of the time range in which to query published system events. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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

