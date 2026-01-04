# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePrePaidInstanceStockRequest(DaraModel):
    def __init__(
        self,
        data_disk_size: int = None,
        ens_region_id: str = None,
        instance_spec: str = None,
        system_disk_size: int = None,
    ):
        # The size of the data disk. Unit: GB.
        # 
        # This parameter is required.
        self.data_disk_size = data_disk_size
        # The ID of the edge node.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The specification of the instance.
        # 
        # This parameter is required.
        self.instance_spec = instance_spec
        # The size of the system disk. Unit: GB.
        # 
        # This parameter is required.
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

