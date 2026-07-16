# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestoreBranchRequest(DaraModel):
    def __init__(
        self,
        branch_id: str = None,
        client_token: str = None,
        preserve_under_name: str = None,
        project_id: str = None,
        region_id: str = None,
        source_branch_id: str = None,
        source_branch_lsn: str = None,
        source_branch_timestamp: str = None,
    ):
        # The branch ID that uniquely identifies a Supabase branch.
        # 
        # This parameter is required.
        self.branch_id = branch_id
        # The client idempotency token that ensures the idempotence of retry requests.
        self.client_token = client_token
        # The backup branch name. If specified, automatic creation of a backup branch is performed before recovery.
        self.preserve_under_name = preserve_under_name
        # The Supabase project ID associated with the primary branch.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID. This parameter is required when you create a primary branch. When you create a sub-branch, the region is inherited from the primary branch by default.
        self.region_id = region_id
        # The ID of the source branch from which to recover.
        # 
        # This parameter is required.
        self.source_branch_id = source_branch_id
        # The LSN of the source branch to recover to.
        self.source_branch_lsn = source_branch_lsn
        # The point in time of the source branch to recover to. The value must be within the recoverable time window.
        self.source_branch_timestamp = source_branch_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.preserve_under_name is not None:
            result['PreserveUnderName'] = self.preserve_under_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_branch_id is not None:
            result['SourceBranchId'] = self.source_branch_id

        if self.source_branch_lsn is not None:
            result['SourceBranchLsn'] = self.source_branch_lsn

        if self.source_branch_timestamp is not None:
            result['SourceBranchTimestamp'] = self.source_branch_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('PreserveUnderName') is not None:
            self.preserve_under_name = m.get('PreserveUnderName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceBranchId') is not None:
            self.source_branch_id = m.get('SourceBranchId')

        if m.get('SourceBranchLsn') is not None:
            self.source_branch_lsn = m.get('SourceBranchLsn')

        if m.get('SourceBranchTimestamp') is not None:
            self.source_branch_timestamp = m.get('SourceBranchTimestamp')

        return self

