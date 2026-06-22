# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        count: int = None,
        performance_level: str = None,
        size: int = None,
    ):
        # The disk type. Valid values:
        # 
        # - `cloud_efficiency`: Ultra Disk.
        # 
        # - `cloud_ssd`: Standard SSD.
        # 
        # - `cloud_essd`: ESSD.
        # 
        # - `cloud`: Basic Disk.
        # 
        # This parameter is required.
        self.category = category
        # The number of data disks.
        self.count = count
        # The performance level of an ESSD. This parameter applies only when the `Category` parameter is set to `cloud_essd`. Valid values:
        # 
        # - PL0: A maximum of 10,000 random read/write IOPS per disk.
        # 
        # - PL1: A maximum of 50,000 random read/write IOPS per disk.
        # 
        # - PL2: A maximum of 100,000 random read/write IOPS per disk.
        # 
        # - PL3: A maximum of 1,000,000 random read/write IOPS per disk.
        # 
        # Default value: PL1.
        self.performance_level = performance_level
        # The size of each data disk, in GB.
        # 
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.count is not None:
            result['Count'] = self.count

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

