# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PreloadRegionSDGShrinkRequest(DaraModel):
    def __init__(
        self,
        destination_region_ids_shrink: str = None,
        disk_type: str = None,
        namespaces_shrink: str = None,
        redundant_num: int = None,
        sdgid: str = None,
    ):
        # The list of destination edge zones.
        # 
        # This parameter is required.
        self.destination_region_ids_shrink = destination_region_ids_shrink
        # The type of the shared cloud disk to be created. Valid values:
        # 
        # - standard: standard cloud disk.
        # 
        # - rbd: rbd cloud disk.
        # 
        # >
        # >- If you do not specify the shared cloud disk type, a standard cloud disk is created by default.
        self.disk_type = disk_type
        # The list of namespaces.
        self.namespaces_shrink = namespaces_shrink
        # The redundancy count to support fast deployment.
        # 
        # This parameter is required.
        self.redundant_num = redundant_num
        # The ID of the SDG that you want to preload.
        # 
        # This parameter is required.
        self.sdgid = sdgid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_region_ids_shrink is not None:
            result['DestinationRegionIds'] = self.destination_region_ids_shrink

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.namespaces_shrink is not None:
            result['Namespaces'] = self.namespaces_shrink

        if self.redundant_num is not None:
            result['RedundantNum'] = self.redundant_num

        if self.sdgid is not None:
            result['SDGId'] = self.sdgid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRegionIds') is not None:
            self.destination_region_ids_shrink = m.get('DestinationRegionIds')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Namespaces') is not None:
            self.namespaces_shrink = m.get('Namespaces')

        if m.get('RedundantNum') is not None:
            self.redundant_num = m.get('RedundantNum')

        if m.get('SDGId') is not None:
            self.sdgid = m.get('SDGId')

        return self

