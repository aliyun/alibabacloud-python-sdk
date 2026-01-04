# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PreloadRegionSDGRequest(DaraModel):
    def __init__(
        self,
        destination_region_ids: List[str] = None,
        disk_type: str = None,
        namespaces: List[str] = None,
        redundant_num: int = None,
        sdgid: str = None,
    ):
        # The IDs of the destination nodes.
        # 
        # This parameter is required.
        self.destination_region_ids = destination_region_ids
        self.disk_type = disk_type
        # An array that consists of queried namespaces.
        self.namespaces = namespaces
        # The number of redundant replicas to support rapid deployment.
        # 
        # This parameter is required.
        self.redundant_num = redundant_num
        # The ID of the SDG for which data is preloaded.
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
        if self.destination_region_ids is not None:
            result['DestinationRegionIds'] = self.destination_region_ids

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces

        if self.redundant_num is not None:
            result['RedundantNum'] = self.redundant_num

        if self.sdgid is not None:
            result['SDGId'] = self.sdgid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRegionIds') is not None:
            self.destination_region_ids = m.get('DestinationRegionIds')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')

        if m.get('RedundantNum') is not None:
            self.redundant_num = m.get('RedundantNum')

        if m.get('SDGId') is not None:
            self.sdgid = m.get('SDGId')

        return self

