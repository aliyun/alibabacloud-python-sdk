# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgenticDBProjectRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        default_branch_name: str = None,
        description: str = None,
        project_name: str = None,
        region_id: str = None,
        tenant_id: str = None,
    ):
        # The AgenticDB cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The default branch name. Default value: main.
        self.default_branch_name = default_branch_name
        # The description of the project.
        self.description = description
        # The project name. The name must be unique within the same tenant.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the tenant to which the project belongs.
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.default_branch_name is not None:
            result['DefaultBranchName'] = self.default_branch_name

        if self.description is not None:
            result['Description'] = self.description

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DefaultBranchName') is not None:
            self.default_branch_name = m.get('DefaultBranchName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

