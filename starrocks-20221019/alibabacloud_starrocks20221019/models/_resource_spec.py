# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResourceSpec(DaraModel):
    def __init__(
        self,
        cu: int = None,
        disk_number: int = None,
        local_storage_instance_type: str = None,
        node_number: int = None,
        spec_type: str = None,
        storage_performance_level: str = None,
        storage_size: int = None,
    ):
        # The number of CUs. A compute unit (CU) is the basic metering unit of a service. 1 CU = 1 CPU core + 4 GiB of memory.
        self.cu = cu
        # The number of disk blocks.
        self.disk_number = disk_number
        # Local SSD Instance Specification for the node group. This parameter is applicable only when the node group is based on ECS instances and the SpecType is set to \\"Local SSD / Large-capacity Storage\\"
        self.local_storage_instance_type = local_storage_instance_type
        # The number of nodes.
        self.node_number = node_number
        # The type of the node group. The following types are included:
        # 
        # *   standard, Standard Edition, ECS + cloud disk.
        # *   localSSD , local SSD.
        # *   bigData, which stores large specifications.
        self.spec_type = spec_type
        # The performance level of the disks. Valid values:
        # 
        # *   PL0: A single disk can achieve up to 10,000 random read/write IOPS.
        # *   PL1: A single disk can achieve up to 50,000 random read/write IOPS.
        # *   PL2: A single disk can achieve up to 100,000 random read/write IOPS.
        # *   PL3: A single disk can achieve up to 1 million random read/write IOPS.
        self.storage_performance_level = storage_performance_level
        # The storage size.
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        if self.disk_number is not None:
            result['diskNumber'] = self.disk_number

        if self.local_storage_instance_type is not None:
            result['localStorageInstanceType'] = self.local_storage_instance_type

        if self.node_number is not None:
            result['nodeNumber'] = self.node_number

        if self.spec_type is not None:
            result['specType'] = self.spec_type

        if self.storage_performance_level is not None:
            result['storagePerformanceLevel'] = self.storage_performance_level

        if self.storage_size is not None:
            result['storageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('diskNumber') is not None:
            self.disk_number = m.get('diskNumber')

        if m.get('localStorageInstanceType') is not None:
            self.local_storage_instance_type = m.get('localStorageInstanceType')

        if m.get('nodeNumber') is not None:
            self.node_number = m.get('nodeNumber')

        if m.get('specType') is not None:
            self.spec_type = m.get('specType')

        if m.get('storagePerformanceLevel') is not None:
            self.storage_performance_level = m.get('storagePerformanceLevel')

        if m.get('storageSize') is not None:
            self.storage_size = m.get('storageSize')

        return self

