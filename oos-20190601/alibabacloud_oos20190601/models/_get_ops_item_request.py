# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOpsItemRequest(DaraModel):
    def __init__(
        self,
        ops_item_id: str = None,
        region_id: str = None,
    ):
        # The O\\&M item ID.
        # 
        # This parameter is required.
        self.ops_item_id = ops_item_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

