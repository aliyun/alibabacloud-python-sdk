# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeZonesRequest(DaraModel):
    def __init__(
        self,
        file_system_type: str = None,
        region_id: str = None,
    ):
        # The file system type.
        # 
        # Valid values:
        # 
        # - standard (default): General-purpose NAS.
        # - extreme: Extreme NAS file system.
        # - cpfs: Cloud Parallel File Storage.
        self.file_system_type = file_system_type
        # The ID of the region where the zones reside.
        # 
        # You can call DescribeRegions to query the latest region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

