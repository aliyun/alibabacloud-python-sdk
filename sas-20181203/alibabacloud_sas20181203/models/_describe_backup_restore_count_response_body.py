# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupRestoreCountResponseBody(DaraModel):
    def __init__(
        self,
        backup_restore_count: main_models.DescribeBackupRestoreCountResponseBodyBackupRestoreCount = None,
        request_id: str = None,
    ):
        # The statistics of restoration tasks.
        self.backup_restore_count = backup_restore_count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.backup_restore_count:
            self.backup_restore_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_restore_count is not None:
            result['BackupRestoreCount'] = self.backup_restore_count.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRestoreCount') is not None:
            temp_model = main_models.DescribeBackupRestoreCountResponseBodyBackupRestoreCount()
            self.backup_restore_count = temp_model.from_map(m.get('BackupRestoreCount'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackupRestoreCountResponseBodyBackupRestoreCount(DaraModel):
    def __init__(
        self,
        recovering: int = None,
        total: int = None,
    ):
        # The number of the restoration tasks that are in the **being restored** state.
        self.recovering = recovering
        # The total number of the restoration tasks that you create.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.recovering is not None:
            result['Recovering'] = self.recovering

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Recovering') is not None:
            self.recovering = m.get('Recovering')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

