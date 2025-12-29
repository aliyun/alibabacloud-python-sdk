# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteOpsItemsRequest(DaraModel):
    def __init__(
        self,
        ops_item_ids: List[str] = None,
        region_id: str = None,
    ):
        # The IDs of O\\&M items.
        self.ops_item_ids = ops_item_ids
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ops_item_ids is not None:
            result['OpsItemIds'] = self.ops_item_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpsItemIds') is not None:
            self.ops_item_ids = m.get('OpsItemIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

