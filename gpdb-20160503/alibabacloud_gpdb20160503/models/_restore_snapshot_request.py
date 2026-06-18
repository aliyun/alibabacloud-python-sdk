# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestoreSnapshotRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        finalize_restore: bool = None,
        project_id: str = None,
        region_id: str = None,
        restored_branch_name: str = None,
        restored_lsn: str = None,
        target_branch_id: str = None,
    ):
        # The idempotence token. Ensures that repeated requests do not execute the same operation more than once.
        self.client_token = client_token
        # Specifies whether to complete the restoration immediately. Default value: false.
        self.finalize_restore = finalize_restore
        # The Supabase project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The region ID. Specifies the region in which to query or perform the operation.
        self.region_id = region_id
        # The name of the restored branch. If not specified, the backend generates a name automatically.
        self.restored_branch_name = restored_branch_name
        # The snapshot LSN used for restoration.
        # 
        # This parameter is required.
        self.restored_lsn = restored_lsn
        # The target branch ID. If not specified, the backend selects the target branch based on the restoration process.
        self.target_branch_id = target_branch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.finalize_restore is not None:
            result['FinalizeRestore'] = self.finalize_restore

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.restored_branch_name is not None:
            result['RestoredBranchName'] = self.restored_branch_name

        if self.restored_lsn is not None:
            result['RestoredLsn'] = self.restored_lsn

        if self.target_branch_id is not None:
            result['TargetBranchId'] = self.target_branch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FinalizeRestore') is not None:
            self.finalize_restore = m.get('FinalizeRestore')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RestoredBranchName') is not None:
            self.restored_branch_name = m.get('RestoredBranchName')

        if m.get('RestoredLsn') is not None:
            self.restored_lsn = m.get('RestoredLsn')

        if m.get('TargetBranchId') is not None:
            self.target_branch_id = m.get('TargetBranchId')

        return self

