# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeReservedInstancesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        reserved_instances: main_models.DescribeReservedInstancesResponseBodyReservedInstances = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Details about the reserved instances.
        self.reserved_instances = reserved_instances
        # The total number of reserved instances.
        self.total_count = total_count

    def validate(self):
        if self.reserved_instances:
            self.reserved_instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.reserved_instances is not None:
            result['ReservedInstances'] = self.reserved_instances.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ReservedInstances') is not None:
            temp_model = main_models.DescribeReservedInstancesResponseBodyReservedInstances()
            self.reserved_instances = temp_model.from_map(m.get('ReservedInstances'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeReservedInstancesResponseBodyReservedInstances(DaraModel):
    def __init__(
        self,
        reserved_instance: List[main_models.DescribeReservedInstancesResponseBodyReservedInstancesReservedInstance] = None,
    ):
        self.reserved_instance = reserved_instance

    def validate(self):
        if self.reserved_instance:
            for v1 in self.reserved_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReservedInstance'] = []
        if self.reserved_instance is not None:
            for k1 in self.reserved_instance:
                result['ReservedInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.reserved_instance = []
        if m.get('ReservedInstance') is not None:
            for k1 in m.get('ReservedInstance'):
                temp_model = main_models.DescribeReservedInstancesResponseBodyReservedInstancesReservedInstance()
                self.reserved_instance.append(temp_model.from_map(k1))

        return self

class DescribeReservedInstancesResponseBodyReservedInstancesReservedInstance(DaraModel):
    def __init__(
        self,
        allocation_status: str = None,
        creation_time: str = None,
        description: str = None,
        expired_time: str = None,
        instance_amount: int = None,
        instance_type: str = None,
        offering_type: str = None,
        operation_locks: main_models.DescribeReservedInstancesResponseBodyReservedInstancesReservedInstanceOperationLocks = None,
        platform: str = None,
        region_id: str = None,
        reserved_instance_id: str = None,
        reserved_instance_name: str = None,
        resource_group_id: str = None,
        scope: str = None,
        start_time: str = None,
        status: str = None,
        tags: main_models.DescribeReservedInstancesResponseBodyReservedInstancesReservedInstanceTags = None,
        zone_id: str = None,
    ):
        # Indicates the sharing status of the reserved instance when the AllocationType parameter is set to Shared. Valid values:
        # 
        # *   allocated: The reserved instance is allocated to another account.
        # *   beAllocated: The reserved instance is allocated by another account.
        self.allocation_status = allocation_status
        # The creation time.
        self.creation_time = creation_time
        # The description.
        self.description = description
        # The expiration time.
        self.expired_time = expired_time
        # The number of pay-as-you-go instances that are of the same instance type as the reserved instance and can be matched to the reserved instance.
        self.instance_amount = instance_amount
        # The instance type of the pay-as-you-go instances that can be matched to the reserved instance.
        self.instance_type = instance_type
        # The payment option.
        self.offering_type = offering_type
        # Details about the lock status of the reserved instance.
        self.operation_locks = operation_locks
        # The operating system of the image used by the instance. Valid values:
        # 
        # *   Windows
        # *   Linux
        self.platform = platform
        # The region ID.
        self.region_id = region_id
        # The reserved instance ID.
        self.reserved_instance_id = reserved_instance_id
        # The name.
        self.reserved_instance_name = reserved_instance_name
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The scope.
        self.scope = scope
        # The effective time.
        self.start_time = start_time
        # The status.
        self.status = status
        # The tags of the reserved instance.
        self.tags = tags
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.operation_locks:
            self.operation_locks.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.instance_amount is not None:
            result['InstanceAmount'] = self.instance_amount

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.offering_type is not None:
            result['OfferingType'] = self.offering_type

        if self.operation_locks is not None:
            result['OperationLocks'] = self.operation_locks.to_map()

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserved_instance_id is not None:
            result['ReservedInstanceId'] = self.reserved_instance_id

        if self.reserved_instance_name is not None:
            result['ReservedInstanceName'] = self.reserved_instance_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('InstanceAmount') is not None:
            self.instance_amount = m.get('InstanceAmount')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OfferingType') is not None:
            self.offering_type = m.get('OfferingType')

        if m.get('OperationLocks') is not None:
            temp_model = main_models.DescribeReservedInstancesResponseBodyReservedInstancesReservedInstanceOperationLocks()
            self.operation_locks = temp_model.from_map(m.get('OperationLocks'))

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReservedInstanceId') is not None:
            self.reserved_instance_id = m.get('ReservedInstanceId')

        if m.get('ReservedInstanceName') is not None:
            self.reserved_instance_name = m.get('ReservedInstanceName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeReservedInstancesResponseBodyReservedInstancesReservedInstanceTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeReservedInstancesResponseBodyReservedInstancesReservedInstanceTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeReservedInstancesResponseBodyReservedInstancesReservedInstanceTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeReservedInstancesResponseBodyReservedInstancesReservedInstanceTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeReservedInstancesResponseBodyReservedInstancesReservedInstanceTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeReservedInstancesResponseBodyReservedInstancesReservedInstanceOperationLocks(DaraModel):
    def __init__(
        self,
        operation_lock: List[main_models.DescribeReservedInstancesResponseBodyReservedInstancesReservedInstanceOperationLocksOperationLock] = None,
    ):
        self.operation_lock = operation_lock

    def validate(self):
        if self.operation_lock:
            for v1 in self.operation_lock:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperationLock'] = []
        if self.operation_lock is not None:
            for k1 in self.operation_lock:
                result['OperationLock'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operation_lock = []
        if m.get('OperationLock') is not None:
            for k1 in m.get('OperationLock'):
                temp_model = main_models.DescribeReservedInstancesResponseBodyReservedInstancesReservedInstanceOperationLocksOperationLock()
                self.operation_lock.append(temp_model.from_map(k1))

        return self

class DescribeReservedInstancesResponseBodyReservedInstancesReservedInstanceOperationLocksOperationLock(DaraModel):
    def __init__(
        self,
        lock_reason: str = None,
    ):
        # The reason why the instance is locked.
        self.lock_reason = lock_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        return self

