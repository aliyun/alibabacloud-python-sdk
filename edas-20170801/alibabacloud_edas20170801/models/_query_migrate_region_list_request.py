# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMigrateRegionListRequest(DaraModel):
    def __init__(
        self,
        logical_region_id: str = None,
    ):
        # The ID of the namespace.
        self.logical_region_id = logical_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logical_region_id is not None:
            result['LogicalRegionId'] = self.logical_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalRegionId') is not None:
            self.logical_region_id = m.get('LogicalRegionId')

        return self

