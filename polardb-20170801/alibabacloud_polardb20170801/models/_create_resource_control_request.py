# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResourceControlRequest(DaraModel):
    def __init__(
        self,
        cpu_count: int = None,
        dbcluster_id: str = None,
        max_cpu: int = None,
        region_id: str = None,
        resource_control_name: str = None,
    ):
        # The maximum number of CPU cores that the resource control rule can use. The minimum value is 1. The maximum value is determined by the cluster kernel parameter resource_control_cpu_count_limit. You must specify one and only one of this parameter and MaxCpu.
        self.cpu_count = cpu_count
        # The PolarDB cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The maximum CPU quota percentage that the resource control rule can use. Valid values: 1 to 100. You must specify one and only one of this parameter and CpuCount.
        self.max_cpu = max_cpu
        # The region ID of the PolarDB cluster.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query available regions.
        self.region_id = region_id
        # The name of the resource control rule. The name must be 1 to 63 ASCII bytes in length, start with a letter, and can contain only letters, digits, and underscores.
        # 
        # This parameter is required.
        self.resource_control_name = resource_control_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.max_cpu is not None:
            result['MaxCpu'] = self.max_cpu

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_control_name is not None:
            result['ResourceControlName'] = self.resource_control_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('MaxCpu') is not None:
            self.max_cpu = m.get('MaxCpu')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceControlName') is not None:
            self.resource_control_name = m.get('ResourceControlName')

        return self

