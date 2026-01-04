# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePrePaidInstanceStockResponseBody(DaraModel):
    def __init__(
        self,
        avaliable_count: int = None,
        cores: int = None,
        data_disk_size: int = None,
        ens_region_id: str = None,
        instance_spec: str = None,
        memory: int = None,
        request_id: str = None,
        resource_gap: str = None,
        system_disk_size: int = None,
    ):
        # The number of resources that you can purchase.
        self.avaliable_count = avaliable_count
        # The number of CPU cores.
        self.cores = cores
        # The size of the data disk.
        self.data_disk_size = data_disk_size
        # The ID of the node.
        self.ens_region_id = ens_region_id
        # The specification of the instance.
        self.instance_spec = instance_spec
        # The memory size. Unit: GB.
        self.memory = memory
        # The request ID.
        self.request_id = request_id
        # The reason why resources are insufficient.
        self.resource_gap = resource_gap
        # The size of the system disk.
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avaliable_count is not None:
            result['AvaliableCount'] = self.avaliable_count

        if self.cores is not None:
            result['Cores'] = self.cores

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_gap is not None:
            result['ResourceGap'] = self.resource_gap

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvaliableCount') is not None:
            self.avaliable_count = m.get('AvaliableCount')

        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGap') is not None:
            self.resource_gap = m.get('ResourceGap')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

