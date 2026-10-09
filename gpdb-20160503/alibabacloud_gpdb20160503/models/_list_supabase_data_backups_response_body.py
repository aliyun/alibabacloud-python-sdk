# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListSupabaseDataBackupsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListSupabaseDataBackupsResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_backup_size: int = None,
        total_count: int = None,
    ):
        # The list of backup sets.
        self.items = items
        # The maximum number of entries to return for the current request.
        self.max_results = max_results
        # The pagination token for the next page. You can use this value as the NextToken parameter in the next request.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of backup sets on the current page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total size of the backup sets. Unit: bytes.
        self.total_backup_size = total_backup_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_backup_size is not None:
            result['TotalBackupSize'] = self.total_backup_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListSupabaseDataBackupsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalBackupSize') is not None:
            self.total_backup_size = m.get('TotalBackupSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSupabaseDataBackupsResponseBodyItems(DaraModel):
    def __init__(
        self,
        backup_end_time: str = None,
        backup_end_time_local: str = None,
        backup_method: str = None,
        backup_mode: str = None,
        backup_set_id: str = None,
        backup_size: int = None,
        backup_start_time: str = None,
        backup_start_time_local: str = None,
        backup_status: str = None,
        bakset_name: str = None,
        consistent_time: int = None,
        data_type: str = None,
    ):
        # The end time of the backup. Format: yyyy-MM-ddTHH:mm:ssZ (UTC).
        self.backup_end_time = backup_end_time
        # The local time representation of the backup end time. Format: yyyy-MM-ddTHH:mm:ssZ. The current return value is in Beijing time (UTC+8). The trailing Z is a fixed character in the compatibility format and does not indicate the zero time zone. To parse the time in a standard format, use BackupEndTime.
        self.backup_end_time_local = backup_end_time_local
        # The backup method. Valid values: Physical: physical backup; Snapshot: snapshot backup.
        self.backup_method = backup_method
        # The backup mode.
        # 
        # Valid values for automatic backups:
        # 
        # - **Automated**: automatic system backup.
        # - **Manual**: manual backup.
        # 
        # Valid values for restorable points:
        # 
        # - **Automated**: the restorable point after a automatic backup.
        # - **Manual**: the restorable point manually triggered by the user.
        # - **Period**: the restorable point triggered periodically based on the backup policy.
        self.backup_mode = backup_mode
        # The ID of the backup set.
        self.backup_set_id = backup_set_id
        # The size of the backup file. Unit: bytes.
        self.backup_size = backup_size
        # The start time of the backup. Format: yyyy-MM-ddTHH:mm:ssZ (UTC).
        self.backup_start_time = backup_start_time
        # The local time representation of the backup start time. Format: yyyy-MM-ddTHH:mm:ssZ. The current return value is in Beijing time (UTC+8). The trailing Z is a fixed character in the compatibility format and does not indicate the zero time zone. To parse the time in a standard format, use BackupStartTime.
        self.backup_start_time_local = backup_start_time_local
        # The status of the backup set. Valid values:
        # 
        # - **Success**: successful.
        # - **Failure**: failed.
        self.backup_status = backup_status
        # The name of the restorable point or the full backup set.
        self.bakset_name = bakset_name
        # The consistency point in time. The value is a UNIX timestamp in seconds. For a full backup, this parameter indicates the consistency point in time of the backup. For a restorable point, this parameter indicates the point in time to which data can be restored.
        self.consistent_time = consistent_time
        # The backup type. Valid values:
        # 
        # - **DATA**: full backup.
        # - **RESTOREPOI**: restorable point.
        self.data_type = data_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_end_time_local is not None:
            result['BackupEndTimeLocal'] = self.backup_end_time_local

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_start_time_local is not None:
            result['BackupStartTimeLocal'] = self.backup_start_time_local

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.bakset_name is not None:
            result['BaksetName'] = self.bakset_name

        if self.consistent_time is not None:
            result['ConsistentTime'] = self.consistent_time

        if self.data_type is not None:
            result['DataType'] = self.data_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupEndTimeLocal') is not None:
            self.backup_end_time_local = m.get('BackupEndTimeLocal')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStartTimeLocal') is not None:
            self.backup_start_time_local = m.get('BackupStartTimeLocal')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('BaksetName') is not None:
            self.bakset_name = m.get('BaksetName')

        if m.get('ConsistentTime') is not None:
            self.consistent_time = m.get('ConsistentTime')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        return self

