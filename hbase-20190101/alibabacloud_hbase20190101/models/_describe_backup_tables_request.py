# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupTablesRequest(DaraModel):
    def __init__(
        self,
        backup_record_id: str = None,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The backup record ID. You can call the DescribeBackupSummary operation to obtain the ID.
        # 
        # This parameter is required.
        self.backup_record_id = backup_record_id
        # The ID of the backup cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_record_id is not None:
            result['BackupRecordId'] = self.backup_record_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRecordId') is not None:
            self.backup_record_id = m.get('BackupRecordId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

