# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupPlanConfigRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        full_backup_cycle: str = None,
        min_hfile_backup_count: str = None,
        next_full_backup_date: str = None,
        tables: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The full backup cycle, in days. Valid values: 3 to 9.
        # 
        # This parameter is required.
        self.full_backup_cycle = full_backup_cycle
        # The number of full backups to retain. Valid values: 3 to 8.
        # 
        # This parameter is required.
        self.min_hfile_backup_count = min_hfile_backup_count
        # The time of the next full backup. The specified time must be at least 6 minutes later than the current time.
        # 
        # This parameter is required.
        self.next_full_backup_date = next_full_backup_date
        # The tables to back up. Specify one table name per line. Wildcards are supported. An asterisk (*) indicates all tables.
        # 
        # This parameter is required.
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.full_backup_cycle is not None:
            result['FullBackupCycle'] = self.full_backup_cycle

        if self.min_hfile_backup_count is not None:
            result['MinHFileBackupCount'] = self.min_hfile_backup_count

        if self.next_full_backup_date is not None:
            result['NextFullBackupDate'] = self.next_full_backup_date

        if self.tables is not None:
            result['Tables'] = self.tables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('FullBackupCycle') is not None:
            self.full_backup_cycle = m.get('FullBackupCycle')

        if m.get('MinHFileBackupCount') is not None:
            self.min_hfile_backup_count = m.get('MinHFileBackupCount')

        if m.get('NextFullBackupDate') is not None:
            self.next_full_backup_date = m.get('NextFullBackupDate')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        return self

