# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHanaRestoresRequest(DaraModel):
    def __init__(
        self,
        backup_id: int = None,
        cluster_id: str = None,
        database_name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        restore_id: str = None,
        restore_status: str = None,
        vault_id: str = None,
    ):
        # The backup ID.
        self.backup_id = backup_id
        # The ID of the SAP HANA instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The database name.
        self.database_name = database_name
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.\\`
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the restore job.
        self.restore_id = restore_id
        # The status of the restore job. Valid values:
        # 
        # *   **RUNNING**: The job is running.
        # *   **COMPLETE**: The job is completed.
        # *   **PARTIAL_COMPLETE**: The job is partially completed.
        # *   **FAILED**: The job failed.
        # *   **CANCELED**: The job is canceled.
        # *   **EXPIRED**: The job timed out.
        self.restore_status = restore_status
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.restore_id is not None:
            result['RestoreId'] = self.restore_id

        if self.restore_status is not None:
            result['RestoreStatus'] = self.restore_status

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RestoreId') is not None:
            self.restore_id = m.get('RestoreId')

        if m.get('RestoreStatus') is not None:
            self.restore_status = m.get('RestoreStatus')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

