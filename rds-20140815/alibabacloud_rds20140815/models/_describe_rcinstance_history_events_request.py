# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCInstanceHistoryEventsRequest(DaraModel):
    def __init__(
        self,
        event_publish_time: main_models.DescribeRCInstanceHistoryEventsRequestEventPublishTime = None,
        not_before: main_models.DescribeRCInstanceHistoryEventsRequestNotBefore = None,
        event_cycle_status: str = None,
        event_id: List[str] = None,
        event_type: str = None,
        impact_level: str = None,
        instance_event_cycle_status: List[str] = None,
        instance_event_type: List[str] = None,
        instance_id: str = None,
        max_results: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: List[str] = None,
        tag: List[main_models.DescribeRCInstanceHistoryEventsRequestTag] = None,
    ):
        self.event_publish_time = event_publish_time
        self.not_before = not_before
        # The lifecycle state of the system event. This parameter is valid only when the **InstanceEventCycleStatus.N** parameter is not specified. Valid values:
        # 
        # *   **Scheduled**
        # *   **Avoided**
        # *   **Executing**
        # *   **Executed**
        # *   **Canceled**
        # *   **Failed**
        # *   **Inquiring**
        self.event_cycle_status = event_cycle_status
        # The IDs of one or more system events.
        self.event_id = event_id
        # The system event type. This parameter is valid only when the **InstanceEventType.N** parameter is not specified. Valid values:
        # 
        # *   **SystemMaintenance.Reboot**: The instance was restarted due to system maintenance.
        # *   **SystemMaintenance.Redeploy**: The instance was redeployed due to system maintenance.
        # *   **SystemFailure.Reboot**: The instance was restarted due to system failures.
        # *   **SystemFailure.Redeploy**: The instance was redeployed due to system failures.
        # *   **SystemFailure.Delete**: The instance was released due to an instance creation failure.
        # *   **InstanceFailure.Reboot**: The instance was restarted due to an instance error.
        # *   **InstanceExpiration.Stop**: The subscription instance was stopped due to expiration.
        # *   **InstanceExpiration.Delete**: The subscription instance was released due to expiration.
        # *   **AccountUnbalanced.Stop**: The pay-as-you-go instance is stopped due to an overdue payment.
        # *   **AccountUnbalanced.Delete**: The pay-as-you-go instance was released due to an overdue payment.
        # 
        # >  The values of this parameter are applicable only to instance system events, but not to disk system events.
        self.event_type = event_type
        # The reserved parameter. This parameter is not supported.
        self.impact_level = impact_level
        # The lifecycle states of system events.
        self.instance_event_cycle_status = instance_event_cycle_status
        # The type of system event N.
        self.instance_event_type = instance_event_type
        # The instance ID. If you do not specify an instance ID, system events of all instances in the specified region are queried.
        self.instance_id = instance_id
        # The reserved parameter. This parameter is not supported.
        self.max_results = max_results
        # The page number of the returned page.
        self.page_number = page_number
        # The maximum number of entries returned per page.
        self.page_size = page_size
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group that you want to query.
        self.resource_group_id = resource_group_id
        # The ID of resource N.
        self.resource_id = resource_id
        # An array that consists of the tags that are supported by system events.
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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventPublishTime') is not None:
            temp_model = main_models.DescribeRCInstanceHistoryEventsRequestEventPublishTime()
            self.event_publish_time = temp_model.from_map(m.get('EventPublishTime'))

        if m.get('NotBefore') is not None:
            temp_model = main_models.DescribeRCInstanceHistoryEventsRequestNotBefore()
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

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeRCInstanceHistoryEventsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeRCInstanceHistoryEventsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag that is added to the resource.
        self.key = key
        # The value of tag N of the port list.
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

class DescribeRCInstanceHistoryEventsRequestNotBefore(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        # The end time of the scheduled execution period for the system event. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.end = end
        # The start time of the scheduled execution period for the system event. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
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

class DescribeRCInstanceHistoryEventsRequestEventPublishTime(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        # The end of the time range in which to query published system events. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.end = end
        # The beginning of the time range in which to query published system events. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
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

