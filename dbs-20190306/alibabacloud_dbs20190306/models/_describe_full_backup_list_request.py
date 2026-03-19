# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFullBackupListRequest(DaraModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        backup_set_id: str = None,
        backup_set_status: str = None,
        client_token: str = None,
        end_timestamp: int = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        show_progress: str = None,
        show_storage_type: bool = None,
        start_timestamp: int = None,
    ):
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.backup_plan_id = backup_plan_id
        # The ID of the backup set.
        self.backup_set_id = backup_set_id
        self.backup_set_status = backup_set_status
        # A token that ensures idempotence and prevents duplicate requests.
        self.client_token = client_token
        # The end time of the backup, in UNIX timestamp format.
        self.end_timestamp = end_timestamp
        self.owner_id = owner_id
        # The page number. Valid values: integers from 0 to the maximum integer value. Default value: 0.
        self.page_num = page_num
        # The number of entries per page. Valid values:
        # 
        # - 30
        # 
        # - 50
        # 
        # - 100
        # 
        # Default value: 30.
        self.page_size = page_size
        self.show_progress = show_progress
        # Specifies whether to return the storage class.
        self.show_storage_type = show_storage_type
        # The start time of the backup.
        self.start_timestamp = start_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.backup_set_status is not None:
            result['BackupSetStatus'] = self.backup_set_status

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.show_progress is not None:
            result['ShowProgress'] = self.show_progress

        if self.show_storage_type is not None:
            result['ShowStorageType'] = self.show_storage_type

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('BackupSetStatus') is not None:
            self.backup_set_status = m.get('BackupSetStatus')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ShowProgress') is not None:
            self.show_progress = m.get('ShowProgress')

        if m.get('ShowStorageType') is not None:
            self.show_storage_type = m.get('ShowStorageType')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        return self

