# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEnsResourceUsageResponseBody(DaraModel):
    def __init__(
        self,
        ens_resource_usage: List[main_models.DescribeEnsResourceUsageResponseBodyEnsResourceUsage] = None,
        request_id: str = None,
    ):
        # The resource usage data.
        self.ens_resource_usage = ens_resource_usage
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.ens_resource_usage:
            for v1 in self.ens_resource_usage:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EnsResourceUsage'] = []
        if self.ens_resource_usage is not None:
            for k1 in self.ens_resource_usage:
                result['EnsResourceUsage'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_resource_usage = []
        if m.get('EnsResourceUsage') is not None:
            for k1 in m.get('EnsResourceUsage'):
                temp_model = main_models.DescribeEnsResourceUsageResponseBodyEnsResourceUsage()
                self.ens_resource_usage.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEnsResourceUsageResponseBodyEnsResourceUsage(DaraModel):
    def __init__(
        self,
        compute_resource_count: int = None,
        cpu_sum: int = None,
        disk_count: int = None,
        down_count: int = None,
        expired_count: int = None,
        expiring_count: int = None,
        gpu_sum: int = None,
        instance_count: int = None,
        running_count: int = None,
        service_type: str = None,
        storage_sum: int = None,
    ):
        # The number of edge services. This parameter is available only when you set the ServiceType parameter to 2.
        self.compute_resource_count = compute_resource_count
        # The CPU usage. Unit: cores.
        self.cpu_sum = cpu_sum
        # The number of data disks.
        self.disk_count = disk_count
        # The number of stopped VMs.
        self.down_count = down_count
        # The number of expired VM instances.
        self.expired_count = expired_count
        # The number of VM instances that are about to expire.
        self.expiring_count = expiring_count
        # The number of GPUs.
        self.gpu_sum = gpu_sum
        # The number of instances.
        self.instance_count = instance_count
        # The number of running instances.
        self.running_count = running_count
        # The type of the service. Valid values:
        # 
        # *   1: subscription instance.
        # *   2: edge service instance.
        # *   3: pay-as-you-go instance.
        self.service_type = service_type
        # The total disk size.
        self.storage_sum = storage_sum

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource_count is not None:
            result['ComputeResourceCount'] = self.compute_resource_count

        if self.cpu_sum is not None:
            result['CpuSum'] = self.cpu_sum

        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count

        if self.down_count is not None:
            result['DownCount'] = self.down_count

        if self.expired_count is not None:
            result['ExpiredCount'] = self.expired_count

        if self.expiring_count is not None:
            result['ExpiringCount'] = self.expiring_count

        if self.gpu_sum is not None:
            result['GpuSum'] = self.gpu_sum

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.running_count is not None:
            result['RunningCount'] = self.running_count

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.storage_sum is not None:
            result['StorageSum'] = self.storage_sum

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeResourceCount') is not None:
            self.compute_resource_count = m.get('ComputeResourceCount')

        if m.get('CpuSum') is not None:
            self.cpu_sum = m.get('CpuSum')

        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')

        if m.get('DownCount') is not None:
            self.down_count = m.get('DownCount')

        if m.get('ExpiredCount') is not None:
            self.expired_count = m.get('ExpiredCount')

        if m.get('ExpiringCount') is not None:
            self.expiring_count = m.get('ExpiringCount')

        if m.get('GpuSum') is not None:
            self.gpu_sum = m.get('GpuSum')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('RunningCount') is not None:
            self.running_count = m.get('RunningCount')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('StorageSum') is not None:
            self.storage_sum = m.get('StorageSum')

        return self

