# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceHistoryEventsResponseBody(DaraModel):
    def __init__(
        self,
        instance_system_event_set: main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSet = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the instance system events.
        self.instance_system_event_set = instance_system_event_set
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        # 
        # >  If the NextToken parameter is not returned when you use the MaxResults and NextToken parameters to perform a paged query, no more data is returned.
        self.next_token = next_token
        # The page number.
        # 
        # > 
        # 
        # *   If MaxResults and NextToken are used to query results by page, ignore this parameter.
        # 
        # *   This parameter will be removed in the future. We recommend that you use the NextToken and MaxResults parameters for a paged query.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # > 
        # 
        # *   If MaxResults and NextToken are used to query results by page, ignore this parameter.
        # 
        # *   This parameter will be removed in the future. We recommend that you use the NextToken and MaxResults parameters for a paged query.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of instances.
        # 
        # >  If you specify the MaxResults and NextToken request parameters to perform a paged query, the value of the TotalCount response parameter is invalid.
        self.total_count = total_count

    def validate(self):
        if self.instance_system_event_set:
            self.instance_system_event_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_system_event_set is not None:
            result['InstanceSystemEventSet'] = self.instance_system_event_set.to_map()

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
        if m.get('InstanceSystemEventSet') is not None:
            temp_model = main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSet()
            self.instance_system_event_set = temp_model.from_map(m.get('InstanceSystemEventSet'))

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

class DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSet(DaraModel):
    def __init__(
        self,
        instance_system_event_type: List[main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventType] = None,
    ):
        self.instance_system_event_type = instance_system_event_type

    def validate(self):
        if self.instance_system_event_type:
            for v1 in self.instance_system_event_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceSystemEventType'] = []
        if self.instance_system_event_type is not None:
            for k1 in self.instance_system_event_type:
                result['InstanceSystemEventType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_system_event_type = []
        if m.get('InstanceSystemEventType') is not None:
            for k1 in m.get('InstanceSystemEventType'):
                temp_model = main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventType()
                self.instance_system_event_type.append(temp_model.from_map(k1))

        return self

class DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventType(DaraModel):
    def __init__(
        self,
        event_cycle_status: main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeEventCycleStatus = None,
        event_finish_time: str = None,
        event_id: str = None,
        event_publish_time: str = None,
        event_type: main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeEventType = None,
        extended_attribute: main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeExtendedAttribute = None,
        impact_level: str = None,
        instance_id: str = None,
        not_before: str = None,
        reason: str = None,
        reason_code: str = None,
        resource_type: str = None,
    ):
        # The lifecycle status of the system event.
        self.event_cycle_status = event_cycle_status
        # The time when the system event ended. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.event_finish_time = event_finish_time
        # The ID of the system event.
        self.event_id = event_id
        # The time when the system event was published. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.event_publish_time = event_publish_time
        # The type of the system event.
        self.event_type = event_type
        # The extended attribute of the system event.
        self.extended_attribute = extended_attribute
        # The impact level of the system event.
        self.impact_level = impact_level
        # The ID of the instance.
        self.instance_id = instance_id
        # The scheduled start time of the system event. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.not_before = not_before
        # The reason why the system event occurred.
        self.reason = reason
        # The reason code category for the system event.
        self.reason_code = reason_code
        # The type of the resource. Valid values:
        # 
        # *   instance: ECS instance
        # *   ddh: dedicated host
        # *   managehost: physical machine in a smart hosting pool
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
            temp_model = main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeEventCycleStatus()
            self.event_cycle_status = temp_model.from_map(m.get('EventCycleStatus'))

        if m.get('EventFinishTime') is not None:
            self.event_finish_time = m.get('EventFinishTime')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventPublishTime') is not None:
            self.event_publish_time = m.get('EventPublishTime')

        if m.get('EventType') is not None:
            temp_model = main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeEventType()
            self.event_type = temp_model.from_map(m.get('EventType'))

        if m.get('ExtendedAttribute') is not None:
            temp_model = main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeExtendedAttribute()
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

class DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeExtendedAttribute(DaraModel):
    def __init__(
        self,
        can_accept: str = None,
        code: str = None,
        device: str = None,
        disk_id: str = None,
        host_id: str = None,
        host_type: str = None,
        inactive_disks: main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeExtendedAttributeInactiveDisks = None,
        metric_name: str = None,
        metric_value: str = None,
        migration_options: main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeExtendedAttributeMigrationOptions = None,
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
        # *   ddh: dedicated host
        # *   managehost: physical machine in a smart hosting pool
        self.host_type = host_type
        # The inactive disks that were released and whose data must be cleared.
        self.inactive_disks = inactive_disks
        self.metric_name = metric_name
        self.metric_value = metric_value
        # The migration solution of the instance. Valid value: MigrationPlan. Instances can be migrated only by using migration plans.
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
        # *   true: The event was handled.
        # *   false: The event failed to be handled.
        self.response_result = response_result

    def validate(self):
        if self.inactive_disks:
            self.inactive_disks.validate()
        if self.migration_options:
            self.migration_options.validate()

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

        if self.inactive_disks is not None:
            result['InactiveDisks'] = self.inactive_disks.to_map()

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_value is not None:
            result['MetricValue'] = self.metric_value

        if self.migration_options is not None:
            result['MigrationOptions'] = self.migration_options.to_map()

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

        if m.get('InactiveDisks') is not None:
            temp_model = main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeExtendedAttributeInactiveDisks()
            self.inactive_disks = temp_model.from_map(m.get('InactiveDisks'))

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricValue') is not None:
            self.metric_value = m.get('MetricValue')

        if m.get('MigrationOptions') is not None:
            temp_model = main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeExtendedAttributeMigrationOptions()
            self.migration_options = temp_model.from_map(m.get('MigrationOptions'))

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

class DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeExtendedAttributeMigrationOptions(DaraModel):
    def __init__(
        self,
        migration_option: List[str] = None,
    ):
        self.migration_option = migration_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.migration_option is not None:
            result['MigrationOption'] = self.migration_option

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationOption') is not None:
            self.migration_option = m.get('MigrationOption')

        return self

class DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeExtendedAttributeInactiveDisks(DaraModel):
    def __init__(
        self,
        inactive_disk: List[main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeExtendedAttributeInactiveDisksInactiveDisk] = None,
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
                temp_model = main_models.DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeExtendedAttributeInactiveDisksInactiveDisk()
                self.inactive_disk.append(temp_model.from_map(k1))

        return self

class DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeExtendedAttributeInactiveDisksInactiveDisk(DaraModel):
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
        # *   system: system disk
        # *   data: data disk
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

class DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeEventType(DaraModel):
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

class DescribeInstanceHistoryEventsResponseBodyInstanceSystemEventSetInstanceSystemEventTypeEventCycleStatus(DaraModel):
    def __init__(
        self,
        code: int = None,
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

