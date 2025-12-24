# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDisksFullStatusResponseBody(DaraModel):
    def __init__(
        self,
        disk_full_status_set: main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSet = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The collection of full status information of the EBS devices.
        self.disk_full_status_set = disk_full_status_set
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of EBS devices for which full status information is returned.
        self.total_count = total_count

    def validate(self):
        if self.disk_full_status_set:
            self.disk_full_status_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_full_status_set is not None:
            result['DiskFullStatusSet'] = self.disk_full_status_set.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskFullStatusSet') is not None:
            temp_model = main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSet()
            self.disk_full_status_set = temp_model.from_map(m.get('DiskFullStatusSet'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDisksFullStatusResponseBodyDiskFullStatusSet(DaraModel):
    def __init__(
        self,
        disk_full_status_type: List[main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusType] = None,
    ):
        self.disk_full_status_type = disk_full_status_type

    def validate(self):
        if self.disk_full_status_type:
            for v1 in self.disk_full_status_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DiskFullStatusType'] = []
        if self.disk_full_status_type is not None:
            for k1 in self.disk_full_status_type:
                result['DiskFullStatusType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disk_full_status_type = []
        if m.get('DiskFullStatusType') is not None:
            for k1 in m.get('DiskFullStatusType'):
                temp_model = main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusType()
                self.disk_full_status_type.append(temp_model.from_map(k1))

        return self

class DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusType(DaraModel):
    def __init__(
        self,
        device: str = None,
        disk_event_set: main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeDiskEventSet = None,
        disk_id: str = None,
        health_status: main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeHealthStatus = None,
        instance_id: str = None,
        status: main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeStatus = None,
    ):
        # The name of the EBS device that is attached to an instance. Example: /dev/xvdb.
        # 
        # This parameter has a value only when the value of `Status` is `In_use`.
        # 
        # > This parameter will be deprecated in the future. To ensure future compatibility, we recommend that you do not use this parameter.
        self.device = device
        # The events about the EBS device.
        self.disk_event_set = disk_event_set
        # The EBS device ID.
        self.disk_id = disk_id
        # The health status of the EBS device.
        self.health_status = health_status
        # The instance ID.
        self.instance_id = instance_id
        # The lifecycle status of the EBS device.
        self.status = status

    def validate(self):
        if self.disk_event_set:
            self.disk_event_set.validate()
        if self.health_status:
            self.health_status.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device is not None:
            result['Device'] = self.device

        if self.disk_event_set is not None:
            result['DiskEventSet'] = self.disk_event_set.to_map()

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskEventSet') is not None:
            temp_model = main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeDiskEventSet()
            self.disk_event_set = temp_model.from_map(m.get('DiskEventSet'))

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('HealthStatus') is not None:
            temp_model = main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeHealthStatus()
            self.health_status = temp_model.from_map(m.get('HealthStatus'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            temp_model = main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeStatus()
            self.status = temp_model.from_map(m.get('Status'))

        return self

class DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeStatus(DaraModel):
    def __init__(
        self,
        code: int = None,
        name: str = None,
    ):
        # The code of the lifecycle status of the EBS device.
        self.code = code
        # The name of the lifecycle status of the EBS device.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeHealthStatus(DaraModel):
    def __init__(
        self,
        code: int = None,
        name: str = None,
    ):
        # The code of the health status of the EBS device.
        self.code = code
        # The name of the health status of the EBS device.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeDiskEventSet(DaraModel):
    def __init__(
        self,
        disk_event_type: List[main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeDiskEventSetDiskEventType] = None,
    ):
        self.disk_event_type = disk_event_type

    def validate(self):
        if self.disk_event_type:
            for v1 in self.disk_event_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DiskEventType'] = []
        if self.disk_event_type is not None:
            for k1 in self.disk_event_type:
                result['DiskEventType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disk_event_type = []
        if m.get('DiskEventType') is not None:
            for k1 in m.get('DiskEventType'):
                temp_model = main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeDiskEventSetDiskEventType()
                self.disk_event_type.append(temp_model.from_map(k1))

        return self

class DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeDiskEventSetDiskEventType(DaraModel):
    def __init__(
        self,
        event_end_time: str = None,
        event_id: str = None,
        event_time: str = None,
        event_type: main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeDiskEventSetDiskEventTypeEventType = None,
        impact_level: str = None,
    ):
        # The time when the event ended.
        self.event_end_time = event_end_time
        # The ID of the event.
        self.event_id = event_id
        # The time when the event occurred.
        self.event_time = event_time
        # The type of the event.
        self.event_type = event_type
        # The impact level of the event.
        self.impact_level = impact_level

    def validate(self):
        if self.event_type:
            self.event_type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_end_time is not None:
            result['EventEndTime'] = self.event_end_time

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.event_type is not None:
            result['EventType'] = self.event_type.to_map()

        if self.impact_level is not None:
            result['ImpactLevel'] = self.impact_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventEndTime') is not None:
            self.event_end_time = m.get('EventEndTime')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('EventType') is not None:
            temp_model = main_models.DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeDiskEventSetDiskEventTypeEventType()
            self.event_type = temp_model.from_map(m.get('EventType'))

        if m.get('ImpactLevel') is not None:
            self.impact_level = m.get('ImpactLevel')

        return self

class DescribeDisksFullStatusResponseBodyDiskFullStatusSetDiskFullStatusTypeDiskEventSetDiskEventTypeEventType(DaraModel):
    def __init__(
        self,
        code: int = None,
        name: str = None,
    ):
        # The code of the event type.
        self.code = code
        # The name of the event type. Valid values:
        # 
        # *   Degraded: The performance of the EBS device is degraded.
        # *   SeverelyDegraded: The performance of the EBS device is severely degraded.
        # *   Stalled: The performance of the EBS device is severely affected.
        # *   ErrorDetected: The local disk is damaged.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

