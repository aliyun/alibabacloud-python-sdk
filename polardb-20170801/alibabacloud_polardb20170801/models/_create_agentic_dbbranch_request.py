# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgenticDBBranchRequest(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        dbcluster_id: str = None,
        description: str = None,
        parent_branch_id: str = None,
        parent_timestamp: str = None,
        project_id: str = None,
        region_id: str = None,
        tenant_id: str = None,
    ):
        # The name of the branch.
        # 
        # This parameter is required.
        self.branch_name = branch_name
        # The AgenticDB cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The description.
        self.description = description
        # The ID of the parent branch. By default, the branch is derived from the main branch.
        self.parent_branch_id = parent_branch_id
        # Creates the branch based on the data of the parent branch at the specified point in time. If you do not specify this parameter, the latest data is used. The value must be in RFC 3339 format with a time zone and support up to nine fractional digits for seconds. Empty strings and future times are not supported.
        self.parent_timestamp = parent_timestamp
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
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.parent_branch_id is not None:
            result['ParentBranchId'] = self.parent_branch_id

        if self.parent_timestamp is not None:
            result['ParentTimestamp'] = self.parent_timestamp

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ParentBranchId') is not None:
            self.parent_branch_id = m.get('ParentBranchId')

        if m.get('ParentTimestamp') is not None:
            self.parent_timestamp = m.get('ParentTimestamp')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

