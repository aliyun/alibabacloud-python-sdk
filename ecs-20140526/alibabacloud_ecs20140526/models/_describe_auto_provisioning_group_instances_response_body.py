# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoProvisioningGroupInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: main_models.DescribeAutoProvisioningGroupInstancesResponseBodyInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the instances in the auto provisioning group.
        self.instances = instances
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of queried instances in the auto provisioning group.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

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
        if m.get('Instances') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAutoProvisioningGroupInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        instance: List[main_models.DescribeAutoProvisioningGroupInstancesResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.DescribeAutoProvisioningGroupInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class DescribeAutoProvisioningGroupInstancesResponseBodyInstancesInstance(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        creation_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        io_optimized: bool = None,
        is_spot: bool = None,
        memory: int = None,
        network_type: str = None,
        os_type: str = None,
        region_id: str = None,
        status: str = None,
        zone_id: str = None,
    ):
        # The number of vCPU cores of the instance.
        self.cpu = cpu
        # The time when the instance was created.
        self.creation_time = creation_time
        # The instance ID.
        self.instance_id = instance_id
        # The ECS instance type.
        self.instance_type = instance_type
        # Indicates whether the instance is an I/O optimized instance.
        self.io_optimized = io_optimized
        # Indicates whether the instance is a spot instance.
        self.is_spot = is_spot
        # The memory capacity of the instance. Unit: MiB.
        self.memory = memory
        # The network type of the instance. Valid values:
        # 
        # *   vpc: Virtual Private Cloud (VPC)
        # *   classic: classic network
        self.network_type = network_type
        # The operating system type of the instance. Valid values:
        # 
        # *   windows
        # *   linux
        self.os_type = os_type
        # The region ID of the container group.
        self.region_id = region_id
        # The status of the instance.
        self.status = status
        # The ID of the zone to which the instance belongs.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.is_spot is not None:
            result['IsSpot'] = self.is_spot

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('IsSpot') is not None:
            self.is_spot = m.get('IsSpot')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

