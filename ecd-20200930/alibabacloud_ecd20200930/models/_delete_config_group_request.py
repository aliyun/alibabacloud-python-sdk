# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteConfigGroupRequest(DaraModel):
    def __init__(
        self,
        group_ids: List[str] = None,
        region_id: str = None,
    ):
        # The IDs of the configuration groups that you want to delete.
        self.group_ids = group_ids
        # The ID of the region. Set the value to `cn-shanghai`.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

