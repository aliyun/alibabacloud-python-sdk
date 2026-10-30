# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetListGpuClusterRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        time_region: Any = None,
    ):
        # The ID of the region to query.
        self.region_id = region_id
        # The time range to query. Unit: milliseconds. Format: [start,end]. Example: [13254125000, 52451241000].
        self.time_region = time_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.time_region is not None:
            result['timeRegion'] = self.time_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('timeRegion') is not None:
            self.time_region = m.get('timeRegion')

        return self

