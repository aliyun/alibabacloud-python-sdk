# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBranchRequest(DaraModel):
    def __init__(
        self,
        branch_id: str = None,
        region_id: str = None,
    ):
        # The branch ID that uniquely identifies a Supabase branch.
        # 
        # This parameter is required.
        self.branch_id = branch_id
        # The region ID. This parameter is required when you create a primary branch. When you create a child branch, the region is inherited from the primary branch by default.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

