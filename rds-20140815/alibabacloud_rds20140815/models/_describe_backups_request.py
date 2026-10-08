# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupsRequest(DaraModel):
    def __init__(
        self,
        backup_id: str = None,
        backup_mode: str = None,
        backup_status: str = None,
        backup_type: str = None,
        dbinstance_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # The backup set ID.
        self.backup_id = backup_id
        # The backup mode. Valid values:
        # * **Automated**: automatic backup
        # * **Manual**: manual backup
        self.backup_mode = backup_mode
        # The status of the backup set. Valid values:
        # * **Success**: The backup is complete.
        # * **Failed**: The backup failed.
        self.backup_status = backup_status
        # The backup type. Valid values:
        # * **FullBackup**: full backup
        # * **IncrementalBackup**: incremental backup
        self.backup_type = backup_type
        # The instance ID. You can call DescribeDBInstances to obtain the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The end time of the query. The end time must be later than the start time. Format: <i>yyyy-MM-dd</i>T<i>HH:mm</i>Z (UTC).
        # 
        # > Narrow down the time range when you use this operation to query backup sets. A large time range may cause a timeout.
        self.end_time = end_time
        # The page number. The value must be a positive integer that does not exceed the maximum value of the Integer data type.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # * **30**
        # * **50**
        # * **100**
        # 
        # Default value: **30**.
        self.page_size = page_size
        self.resource_owner_id = resource_owner_id
        # The start time of the query. Format: <i>yyyy-MM-dd</i>T<i>HH:mm</i>Z (UTC).
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

