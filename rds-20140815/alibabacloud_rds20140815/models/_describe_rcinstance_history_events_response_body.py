# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCInstanceHistoryEventsResponseBody(DaraModel):
    def __init__(
        self,
        instance_system_event_set: List[main_models.DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSet] = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the instance system event.
        self.instance_system_event_set = instance_system_event_set
        # The reserved parameter. This parameter is not supported.
        self.next_token = next_token
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of instance events.
        self.total_count = total_count

    def validate(self):
        if self.instance_system_event_set:
            for v1 in self.instance_system_event_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceSystemEventSet'] = []
        if self.instance_system_event_set is not None:
            for k1 in self.instance_system_event_set:
                result['InstanceSystemEventSet'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        self.instance_system_event_set = []
        if m.get('InstanceSystemEventSet') is not None:
            for k1 in m.get('InstanceSystemEventSet'):
                temp_model = main_models.DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSet()
                self.instance_system_event_set.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSet(DaraModel):
    def __init__(
        self,
        event_cycle_status: main_models.DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSetEventCycleStatus = None,
        event_finish_time: str = None,
        event_id: str = None,
        event_publish_time: str = None,
        event_type: main_models.DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSetEventType = None,
        extended_attribute: main_models.DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSetExtendedAttribute = None,
        impact_level: str = None,
        instance_id: str = None,
        not_before: str = None,
        reason: str = None,
        reason_code: str = None,
        resource_type: str = None,
    ):
        # The lifecycle state of the system event.
        self.event_cycle_status = event_cycle_status
        # The time when the system event ended. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.event_finish_time = event_finish_time
        # The ID of the system event.
        self.event_id = event_id
        # The time when the system event was published. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.event_publish_time = event_publish_time
        # The type of the system event.
        self.event_type = event_type
        # The extended attribute of the system event.
        self.extended_attribute = extended_attribute
        # The impact level of the event.
        self.impact_level = impact_level
        # The instance ID.
        self.instance_id = instance_id
        # The start time of the scheduled execution of the system event. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.not_before = not_before
        # The reason why the system event occurred.
        self.reason = reason
        # The reason code category for the system event.
        self.reason_code = reason_code
        # The resource type. The value is fixed to INSTANCE.
        self.resource_type = resource_type

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

        if self.event_finish_time is not None:
            result['EventFinishTime'] = self.event_finish_time

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCycleStatus') is not None:
            temp_model = main_models.DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSetEventCycleStatus()
            self.event_cycle_status = temp_model.from_map(m.get('EventCycleStatus'))

        if m.get('EventFinishTime') is not None:
            self.event_finish_time = m.get('EventFinishTime')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventPublishTime') is not None:
            self.event_publish_time = m.get('EventPublishTime')

        if m.get('EventType') is not None:
            temp_model = main_models.DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSetEventType()
            self.event_type = temp_model.from_map(m.get('EventType'))

        if m.get('ExtendedAttribute') is not None:
            temp_model = main_models.DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSetExtendedAttribute()
            self.extended_attribute = temp_model.from_map(m.get('ExtendedAttribute'))

        if m.get('ImpactLevel') is not None:
            self.impact_level = m.get('ImpactLevel')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSetExtendedAttribute(DaraModel):
    def __init__(
        self,
        can_accept: str = None,
        code: str = None,
        device: str = None,
        disk_id: str = None,
        host_id: str = None,
        host_type: str = None,
        inactive_disks: List[main_models.DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSetExtendedAttributeInactiveDisks] = None,
        migration_options: List[str] = None,
        online_repair_policy: str = None,
        punish_domain: str = None,
        punish_type: str = None,
        punish_url: str = None,
        rack: str = None,
        response_result: str = None,
    ):
        # Indicates whether the event can be handled.
        self.can_accept = can_accept
        # The code of the security violation.
        self.code = code
        # The device name of the local disk.
        self.device = device
        # The ID of the local disk.
        self.disk_id = disk_id
        # The ID of the host.
        self.host_id = host_id
        # The type of the host. Valid values:
        # 
        # *   **ddh**: dedicated host
        # *   **managehost**: physical machine in a smart hosting pool
        self.host_type = host_type
        # The inactive disks that have been released and whose data must be cleared.
        self.inactive_disks = inactive_disks
        # The migration solutions of the instance.
        self.migration_options = migration_options
        # The online repair policy for the damaged disk. Valid value: IsolateOnly, which indicates that damaged disks are isolated but not repaired.
        self.online_repair_policy = online_repair_policy
        # The illegal domain name.
        self.punish_domain = punish_domain
        # The type of the penalty.
        self.punish_type = punish_type
        # The illegal URL.
        self.punish_url = punish_url
        # The rack number of the cloud box.
        self.rack = rack
        # The response result of the event. Valid values:
        # 
        # *   **true**: the event was handled.
        # *   **false**: the event failed to be handled.
        self.response_result = response_result

    def validate(self):
        if self.inactive_disks:
            for v1 in self.inactive_disks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_accept is not None:
            result['CanAccept'] = self.can_accept

        if self.code is not None:
            result['Code'] = self.code

        if self.device is not None:
            result['Device'] = self.device

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.host_type is not None:
            result['HostType'] = self.host_type

        result['InactiveDisks'] = []
        if self.inactive_disks is not None:
            for k1 in self.inactive_disks:
                result['InactiveDisks'].append(k1.to_map() if k1 else None)

        if self.migration_options is not None:
            result['MigrationOptions'] = self.migration_options

        if self.online_repair_policy is not None:
            result['OnlineRepairPolicy'] = self.online_repair_policy

        if self.punish_domain is not None:
            result['PunishDomain'] = self.punish_domain

        if self.punish_type is not None:
            result['PunishType'] = self.punish_type

        if self.punish_url is not None:
            result['PunishUrl'] = self.punish_url

        if self.rack is not None:
            result['Rack'] = self.rack

        if self.response_result is not None:
            result['ResponseResult'] = self.response_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanAccept') is not None:
            self.can_accept = m.get('CanAccept')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')

        self.inactive_disks = []
        if m.get('InactiveDisks') is not None:
            for k1 in m.get('InactiveDisks'):
                temp_model = main_models.DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSetExtendedAttributeInactiveDisks()
                self.inactive_disks.append(temp_model.from_map(k1))

        if m.get('MigrationOptions') is not None:
            self.migration_options = m.get('MigrationOptions')

        if m.get('OnlineRepairPolicy') is not None:
            self.online_repair_policy = m.get('OnlineRepairPolicy')

        if m.get('PunishDomain') is not None:
            self.punish_domain = m.get('PunishDomain')

        if m.get('PunishType') is not None:
            self.punish_type = m.get('PunishType')

        if m.get('PunishUrl') is not None:
            self.punish_url = m.get('PunishUrl')

        if m.get('Rack') is not None:
            self.rack = m.get('Rack')

        if m.get('ResponseResult') is not None:
            self.response_result = m.get('ResponseResult')

        return self

class DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSetExtendedAttributeInactiveDisks(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        device_category: str = None,
        device_size: str = None,
        device_type: str = None,
        release_time: str = None,
    ):
        # The time when the disk was created. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.creation_time = creation_time
        # The category of the cloud disk or local disk. Valid values:
        # 
        # *   **cloud_efficiency**: ultra disk
        # *   **cloud_ssd**: standard SSD
        # *   **cloud_essd**: ESSD
        # *   **cloud_auto**: Premium ESSD
        self.device_category = device_category
        # The size of the disk. Unit: GiB.
        self.device_size = device_size
        # The disk type. Valid values:
        # 
        # *   **system**: system disk.
        # *   **data**: data disk.
        self.device_type = device_type
        # The time when the disk was released. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
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

class DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSetEventType(DaraModel):
    def __init__(
        self,
        code: str = None,
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

class DescribeRCInstanceHistoryEventsResponseBodyInstanceSystemEventSetEventCycleStatus(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # The state code of the system event.
        self.code = code
        # The state name of the system event.
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

