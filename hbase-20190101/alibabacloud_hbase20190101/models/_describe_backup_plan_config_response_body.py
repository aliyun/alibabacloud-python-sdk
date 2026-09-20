# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupPlanConfigResponseBody(DaraModel):
    def __init__(
        self,
        full_backup_cycle: int = None,
        min_hfile_backup_count: int = None,
        next_full_backup_date: str = None,
        request_id: str = None,
        tables: main_models.DescribeBackupPlanConfigResponseBodyTables = None,
    ):
        # The full backup cycle.
        self.full_backup_cycle = full_backup_cycle
        # The number of full backups to retain.
        self.min_hfile_backup_count = min_hfile_backup_count
        # The date of the next full backup.
        self.next_full_backup_date = next_full_backup_date
        # The request ID.
        self.request_id = request_id
        self.tables = tables

    def validate(self):
        if self.tables:
            self.tables.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full_backup_cycle is not None:
            result['FullBackupCycle'] = self.full_backup_cycle

        if self.min_hfile_backup_count is not None:
            result['MinHFileBackupCount'] = self.min_hfile_backup_count

        if self.next_full_backup_date is not None:
            result['NextFullBackupDate'] = self.next_full_backup_date

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tables is not None:
            result['Tables'] = self.tables.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullBackupCycle') is not None:
            self.full_backup_cycle = m.get('FullBackupCycle')

        if m.get('MinHFileBackupCount') is not None:
            self.min_hfile_backup_count = m.get('MinHFileBackupCount')

        if m.get('NextFullBackupDate') is not None:
            self.next_full_backup_date = m.get('NextFullBackupDate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Tables') is not None:
            temp_model = main_models.DescribeBackupPlanConfigResponseBodyTables()
            self.tables = temp_model.from_map(m.get('Tables'))

        return self

class DescribeBackupPlanConfigResponseBodyTables(DaraModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

