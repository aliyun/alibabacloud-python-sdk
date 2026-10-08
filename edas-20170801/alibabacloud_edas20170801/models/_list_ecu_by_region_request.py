# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEcuByRegionRequest(DaraModel):
    def __init__(
        self,
        act: str = None,
        logical_region_id: str = None,
    ):
        # Set the value to `pop-query`.
        # 
        # This parameter is required.
        self.act = act
        # The ID of the namespace.
        # 
        # - The ID of a custom namespace is in the `region ID:namespace identifier` format. Example: cn-beijing:tdy218.
        # 
        # - The ID of the default namespace is in the `region ID` format. Example: cn-beijing.
        self.logical_region_id = logical_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.act is not None:
            result['Act'] = self.act

        if self.logical_region_id is not None:
            result['LogicalRegionId'] = self.logical_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Act') is not None:
            self.act = m.get('Act')

        if m.get('LogicalRegionId') is not None:
            self.logical_region_id = m.get('LogicalRegionId')

        return self

