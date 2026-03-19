# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRestoreRangeInfoRequest(DaraModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        begin_timestamp_for_restore: int = None,
        client_token: str = None,
        end_timestamp_for_restore: int = None,
        owner_id: str = None,
        recently_restore: bool = None,
    ):
        # The ID of the backup plan. Call [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) to get this value.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The start timestamp of the restorable time range. Call [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) to get this value.
        # 
        # This parameter is required.
        self.begin_timestamp_for_restore = begin_timestamp_for_restore
        # A client token that ensures the idempotence of requests and prevents duplicate submissions.
        self.client_token = client_token
        # The end timestamp of the restorable time range. Call [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) to get this value.
        # 
        # This parameter is required.
        self.end_timestamp_for_restore = end_timestamp_for_restore
        self.owner_id = owner_id
        # Whether to enable recent restore.
        self.recently_restore = recently_restore

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.begin_timestamp_for_restore is not None:
            result['BeginTimestampForRestore'] = self.begin_timestamp_for_restore

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.end_timestamp_for_restore is not None:
            result['EndTimestampForRestore'] = self.end_timestamp_for_restore

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.recently_restore is not None:
            result['RecentlyRestore'] = self.recently_restore

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('BeginTimestampForRestore') is not None:
            self.begin_timestamp_for_restore = m.get('BeginTimestampForRestore')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndTimestampForRestore') is not None:
            self.end_timestamp_for_restore = m.get('EndTimestampForRestore')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RecentlyRestore') is not None:
            self.recently_restore = m.get('RecentlyRestore')

        return self

