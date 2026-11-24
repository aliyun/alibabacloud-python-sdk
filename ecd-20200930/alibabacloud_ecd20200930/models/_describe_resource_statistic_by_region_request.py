# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResourceStatisticByRegionRequest(DaraModel):
    def __init__(
        self,
        include_group_desktops: bool = None,
        region_id: str = None,
        search_region_id: str = None,
    ):
        # Specifies whether the statistics include the number of shared cloud desktops.
        self.include_group_desktops = include_group_desktops
        # The ID of the service region. Valid values: China (Shanghai) and Singapore.
        self.region_id = region_id
        # The ID of the region to search. This parameter is used to filter cloud desktops in the specified region.
        self.search_region_id = search_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_group_desktops is not None:
            result['IncludeGroupDesktops'] = self.include_group_desktops

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_region_id is not None:
            result['SearchRegionId'] = self.search_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeGroupDesktops') is not None:
            self.include_group_desktops = m.get('IncludeGroupDesktops')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchRegionId') is not None:
            self.search_region_id = m.get('SearchRegionId')

        return self

