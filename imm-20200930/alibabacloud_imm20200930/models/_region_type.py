# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegionType(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        # The name of the region.
        self.local_name = local_name
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

