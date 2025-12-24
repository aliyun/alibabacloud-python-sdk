# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDisksFullStatusRequest(DaraModel):
    def __init__(
        self,
        event_time: main_models.DescribeDisksFullStatusRequestEventTime = None,
        disk_id: List[str] = None,
        event_id: List[str] = None,
        event_type: str = None,
        health_status: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        tag: List[main_models.DescribeDisksFullStatusRequestTag] = None,
    ):
        self.event_time = event_time
        # The ID of EBS device N. Valid values of N: 1 to 100.
        self.disk_id = disk_id
        # The ID of event N. Valid values of N: 1 to 100.
        self.event_id = event_id
        # The event type of the EBS device. Valid values:
        # 
        # *   Degraded: The performance of the EBS device is degraded.
        # *   SeverelyDegraded: The performance of the EBS device is severely degraded.
        # *   Stalled: The performance of the EBS device is severely affected.
        # *   ErrorDetected: The local disk is damaged.
        self.event_type = event_type
        # The health status of the EBS device. Valid values:
        # 
        # *   Impaired: The EBS device is damaged.
        # *   Warning: The performance of the EBS device is degraded.
        # *   Initializing: The EBS device is being initialized.
        # *   InsufficientData: The status cannot be determined due to insufficient data.
        # *   NotApplicable: The EBS device cannot be used.
        self.health_status = health_status
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from page 1. The value must be a positive integer.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the EBS device. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the EBS device belongs. If you configure this parameter to query resources, up to 1,000 resources that belong to the specified resource group can be displayed in the response.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The lifecycle status of the EBS device. For more information, see [Disk status](https://help.aliyun.com/document_detail/25689.html). Valid values:
        # 
        # *   In_use: The EBS device is in use.
        # *   Available: The EBS device can be attached.
        # *   Attaching: The EBS device is being attached.
        # *   Detaching: The EBS device is being detached.
        # *   Creating: The EBS device is being created.
        # *   ReIniting: The EBS device is being initialized.
        self.status = status
        # The tags to add to the EBS device.
        self.tag = tag

    def validate(self):
        if self.event_time:
            self.event_time.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_time is not None:
            result['EventTime'] = self.event_time.to_map()

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

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

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTime') is not None:
            temp_model = main_models.DescribeDisksFullStatusRequestEventTime()
            self.event_time = temp_model.from_map(m.get('EventTime'))

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDisksFullStatusRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeDisksFullStatusRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the EBS device. A key-value pair consists of a key specified by the Tag.N.Key parameter and a value specified by the `Tag.N.Value` parameter. The two parameters are associated with each other. Valid values of N: 1 to 20.
        # 
        # Up to 1,000 resources with the specified tags can be returned in the response.
        self.key = key
        # The value of tag N to add to the EBS device. A key-value pair consists of a key specified by the `Tag.N.Key` parameter and a value specified by the Tag.N.Value parameter. The two parameters are associated with each other. Valid values of N: 1 to 20.
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

class DescribeDisksFullStatusRequestEventTime(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        # The end of the time range to query occurred events.
        # 
        # Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.end = end
        # The beginning of the time range to query occurred events.
        # 
        # Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
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

