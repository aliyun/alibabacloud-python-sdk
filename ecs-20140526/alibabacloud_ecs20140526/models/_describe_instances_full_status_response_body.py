# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesFullStatusResponseBody(DaraModel):
    def __init__(
        self,
        instance_full_status_set: main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSet = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried instances.
        # 
        # >  If no instances exist, this parameter is empty.
        self.instance_full_status_set = instance_full_status_set
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instance_full_status_set:
            self.instance_full_status_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_full_status_set is not None:
            result['InstanceFullStatusSet'] = self.instance_full_status_set.to_map()

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
        if m.get('InstanceFullStatusSet') is not None:
            temp_model = main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSet()
            self.instance_full_status_set = temp_model.from_map(m.get('InstanceFullStatusSet'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstancesFullStatusResponseBodyInstanceFullStatusSet(DaraModel):
    def __init__(
        self,
        instance_full_status_type: List[main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusType] = None,
    ):
        self.instance_full_status_type = instance_full_status_type

    def validate(self):
        if self.instance_full_status_type:
            for v1 in self.instance_full_status_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceFullStatusType'] = []
        if self.instance_full_status_type is not None:
            for k1 in self.instance_full_status_type:
                result['InstanceFullStatusType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_full_status_type = []
        if m.get('InstanceFullStatusType') is not None:
            for k1 in m.get('InstanceFullStatusType'):
                temp_model = main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusType()
                self.instance_full_status_type.append(temp_model.from_map(k1))

        return self

class DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusType(DaraModel):
    def __init__(
        self,
        health_status: main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeHealthStatus = None,
        instance_id: str = None,
        scheduled_system_event_set: main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSet = None,
        status: main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeStatus = None,
    ):
        # The health state of the instance.
        self.health_status = health_status
        # The instance ID.
        self.instance_id = instance_id
        # The system events that are in the Scheduled or Inquiring state.
        self.scheduled_system_event_set = scheduled_system_event_set
        # The lifecycle state of the instance.
        self.status = status

    def validate(self):
        if self.health_status:
            self.health_status.validate()
        if self.scheduled_system_event_set:
            self.scheduled_system_event_set.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.scheduled_system_event_set is not None:
            result['ScheduledSystemEventSet'] = self.scheduled_system_event_set.to_map()

        if self.status is not None:
            result['Status'] = self.status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthStatus') is not None:
            temp_model = main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeHealthStatus()
            self.health_status = temp_model.from_map(m.get('HealthStatus'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScheduledSystemEventSet') is not None:
            temp_model = main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSet()
            self.scheduled_system_event_set = temp_model.from_map(m.get('ScheduledSystemEventSet'))

        if m.get('Status') is not None:
            temp_model = main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeStatus()
            self.status = temp_model.from_map(m.get('Status'))

        return self

class DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeStatus(DaraModel):
    def __init__(
        self,
        code: int = None,
        name: str = None,
    ):
        # The code of the instance lifecycle state.
        self.code = code
        # The name of the instance lifecycle state.
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

class DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSet(DaraModel):
    def __init__(
        self,
        scheduled_system_event_type: List[main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventType] = None,
    ):
        self.scheduled_system_event_type = scheduled_system_event_type

    def validate(self):
        if self.scheduled_system_event_type:
            for v1 in self.scheduled_system_event_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ScheduledSystemEventType'] = []
        if self.scheduled_system_event_type is not None:
            for k1 in self.scheduled_system_event_type:
                result['ScheduledSystemEventType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scheduled_system_event_type = []
        if m.get('ScheduledSystemEventType') is not None:
            for k1 in m.get('ScheduledSystemEventType'):
                temp_model = main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventType()
                self.scheduled_system_event_type.append(temp_model.from_map(k1))

        return self

class DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventType(DaraModel):
    def __init__(
        self,
        event_cycle_status: main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeEventCycleStatus = None,
        event_id: str = None,
        event_publish_time: str = None,
        event_type: main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeEventType = None,
        extended_attribute: main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeExtendedAttribute = None,
        impact_level: str = None,
        not_before: str = None,
        reason: str = None,
    ):
        # The state of the system event.
        self.event_cycle_status = event_cycle_status
        # The system event ID.
        self.event_id = event_id
        # The time when the system event was published. The time is displayed in UTC.
        self.event_publish_time = event_publish_time
        # The type of the system event.
        self.event_type = event_type
        # The extended attributes of system events generated for instances that have local disks attached.
        # 
        # The return values vary based on the system event type.
        # 
        # If the system event type is not one of the following types, this parameter is empty:
        # 
        # *   SystemMaintenance.StopAndRepair
        # *   SystemMaintenance.CleanInactiveDisks
        # *   SecurityPunish.Locked
        # *   SecurityPunish.WebsiteBanned
        # *   SystemUpgrade.Migrate
        # *   SystemMaintenance.RebootAndIsolateErrorDisk
        # *   SystemMaintenance.RebootAndReInitErrorDisk
        # *   SystemMaintenance.ReInitErrorDisk
        # *   SystemMaintenance.IsolateErrorDisk
        self.extended_attribute = extended_attribute
        # The impact level of the system event.
        # 
        # >  If the user is not in a whitelist, this parameter is empty.
        self.impact_level = impact_level
        # The scheduled time at which to execute the O\\&M task related to the system event. The time is displayed in UTC.
        self.not_before = not_before
        # The reason why the system event was scheduled.
        # 
        # >  If the exception cause is not detected, this parameter is empty.
        self.reason = reason

    def validate(self):
        if self.event_cycle_status:
            self.event_cycle_status.validate()
        if self.event_type:
            self.event_type.validate()
        if self.extended_attribute:
            self.extended_attribute.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_cycle_status is not None:
            result['EventCycleStatus'] = self.event_cycle_status.to_map()

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_publish_time is not None:
            result['EventPublishTime'] = self.event_publish_time

        if self.event_type is not None:
            result['EventType'] = self.event_type.to_map()

        if self.extended_attribute is not None:
            result['ExtendedAttribute'] = self.extended_attribute.to_map()

        if self.impact_level is not None:
            result['ImpactLevel'] = self.impact_level

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCycleStatus') is not None:
            temp_model = main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeEventCycleStatus()
            self.event_cycle_status = temp_model.from_map(m.get('EventCycleStatus'))

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventPublishTime') is not None:
            self.event_publish_time = m.get('EventPublishTime')

        if m.get('EventType') is not None:
            temp_model = main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeEventType()
            self.event_type = temp_model.from_map(m.get('EventType'))

        if m.get('ExtendedAttribute') is not None:
            temp_model = main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeExtendedAttribute()
            self.extended_attribute = temp_model.from_map(m.get('ExtendedAttribute'))

        if m.get('ImpactLevel') is not None:
            self.impact_level = m.get('ImpactLevel')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

class DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeExtendedAttribute(DaraModel):
    def __init__(
        self,
        device: str = None,
        disk_id: str = None,
        inactive_disks: main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeExtendedAttributeInactiveDisks = None,
    ):
        # The device name of the local disk.
        self.device = device
        # The ID of the local disk.
        self.disk_id = disk_id
        # The inactive disks that have been released and must be cleared.
        self.inactive_disks = inactive_disks

    def validate(self):
        if self.inactive_disks:
            self.inactive_disks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device is not None:
            result['Device'] = self.device

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.inactive_disks is not None:
            result['InactiveDisks'] = self.inactive_disks.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('InactiveDisks') is not None:
            temp_model = main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeExtendedAttributeInactiveDisks()
            self.inactive_disks = temp_model.from_map(m.get('InactiveDisks'))

        return self

class DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeExtendedAttributeInactiveDisks(DaraModel):
    def __init__(
        self,
        inactive_disk: List[main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeExtendedAttributeInactiveDisksInactiveDisk] = None,
    ):
        self.inactive_disk = inactive_disk

    def validate(self):
        if self.inactive_disk:
            for v1 in self.inactive_disk:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InactiveDisk'] = []
        if self.inactive_disk is not None:
            for k1 in self.inactive_disk:
                result['InactiveDisk'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inactive_disk = []
        if m.get('InactiveDisk') is not None:
            for k1 in m.get('InactiveDisk'):
                temp_model = main_models.DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeExtendedAttributeInactiveDisksInactiveDisk()
                self.inactive_disk.append(temp_model.from_map(k1))

        return self

class DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeExtendedAttributeInactiveDisksInactiveDisk(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        device_category: str = None,
        device_size: str = None,
        device_type: str = None,
        release_time: str = None,
    ):
        # The time when the disk was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The category of the disk. Valid values:
        # 
        # *   cloud: basic disk
        # *   cloud_efficiency: ultra disk
        # *   cloud_ssd: standard SSD
        # *   cloud_essd: Enterprise SSD (ESSD)
        # *   local_ssd_pro: I/O-intensive local disk
        # *   local_hdd_pro: throughput-intensive local disk
        # *   ephemeral: retired local disk
        # *   ephemeral_ssd: retired local SSD
        self.device_category = device_category
        # The size of the disk. Unit: GiB.
        self.device_size = device_size
        # The type of the disk. Valid values:
        # 
        # *   system
        # *   data
        self.device_type = device_type
        # The time when the disk was released. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.release_time = release_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.device_category is not None:
            result['DeviceCategory'] = self.device_category

        if self.device_size is not None:
            result['DeviceSize'] = self.device_size

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeviceCategory') is not None:
            self.device_category = m.get('DeviceCategory')

        if m.get('DeviceSize') is not None:
            self.device_size = m.get('DeviceSize')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        return self

class DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeEventType(DaraModel):
    def __init__(
        self,
        code: int = None,
        name: str = None,
    ):
        # The code of the system event type.
        self.code = code
        # The name of the system event type.
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

class DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeScheduledSystemEventSetScheduledSystemEventTypeEventCycleStatus(DaraModel):
    def __init__(
        self,
        code: int = None,
        name: str = None,
    ):
        # The code of the system event state.
        self.code = code
        # The name of the system event state.
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

class DescribeInstancesFullStatusResponseBodyInstanceFullStatusSetInstanceFullStatusTypeHealthStatus(DaraModel):
    def __init__(
        self,
        code: int = None,
        name: str = None,
    ):
        # The code of the health state.
        self.code = code
        # The name of the health state.
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

