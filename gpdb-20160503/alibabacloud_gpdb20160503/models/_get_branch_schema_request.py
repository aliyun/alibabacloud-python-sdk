# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBranchSchemaRequest(DaraModel):
    def __init__(
        self,
        branch_id: str = None,
        dbname: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        # The branch ID that uniquely identifies a Supabase branch.
        # 
        # This parameter is required.
        self.branch_id = branch_id
        # The database name. The system databases postgres, template0, and template1 do not support schema queries.
        # 
        # This parameter is required.
        self.dbname = dbname
        # The Supabase project ID that corresponds to the primary branch.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID. This parameter is required when you create a primary branch. When you create a sub-branch, the region of the primary branch is inherited by default.
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

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

