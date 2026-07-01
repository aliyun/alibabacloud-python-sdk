# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAgenticDBBranchLineageRequest(DaraModel):
    def __init__(
        self,
        branch_id: str = None,
        dbcluster_id: str = None,
        include_destroying: bool = None,
        max_view_depth: int = None,
        project_id: str = None,
        region_id: str = None,
        tenant_id: str = None,
    ):
        # The anchor branch ID. If this parameter is not specified, the primary branch of the project is used by default.
        self.branch_id = branch_id
        # The AgenticDB cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to include branches in the Destroying state. Default value: false.
        self.include_destroying = include_destroying
        self.max_view_depth = max_view_depth
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The tenant ID.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.include_destroying is not None:
            result['IncludeDestroying'] = self.include_destroying

        if self.max_view_depth is not None:
            result['MaxViewDepth'] = self.max_view_depth

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('IncludeDestroying') is not None:
            self.include_destroying = m.get('IncludeDestroying')

        if m.get('MaxViewDepth') is not None:
            self.max_view_depth = m.get('MaxViewDepth')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

