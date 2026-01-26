# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSyntheticMonitorsShrinkRequest(DaraModel):
    def __init__(
        self,
        filter_shrink: str = None,
        region_id: str = None,
    ):
        # The query conditions.
        # 
        # This parameter is required.
        self.filter_shrink = filter_shrink
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

