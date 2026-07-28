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
        # The total number of CPU cores.
        self.cpu_count = cpu_count
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The maximum number of CPUs. Unit: 0.001 CPU. A value of 1000 indicates one CPU. If you specify this parameter, instances whose CPU count is less than the specified value are returned.
        self.max_cpu = max_cpu
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query available regions.
        self.region_id = region_id
        # The resource control name.
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

