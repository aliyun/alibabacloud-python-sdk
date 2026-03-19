# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableBackupLogRequest(DaraModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        client_token: str = None,
        disable_mysql_physical_backup_binlog_only: str = None,
        owner_id: str = None,
    ):
        # The ID of the backup plan. Call [DescribeBackupPlanList](https://help.aliyun.com/document_detail/2869825.html) to query it.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # Ensures idempotence and prevents duplicate requests.
        self.client_token = client_token
        self.disable_mysql_physical_backup_binlog_only = disable_mysql_physical_backup_binlog_only
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.disable_mysql_physical_backup_binlog_only is not None:
            result['DisableMysqlPhysicalBackupBinlogOnly'] = self.disable_mysql_physical_backup_binlog_only

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DisableMysqlPhysicalBackupBinlogOnly') is not None:
            self.disable_mysql_physical_backup_binlog_only = m.get('DisableMysqlPhysicalBackupBinlogOnly')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

