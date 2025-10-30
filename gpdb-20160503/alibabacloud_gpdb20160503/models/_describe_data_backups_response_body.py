# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDataBackupsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDataBackupsResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_backup_size: int = None,
        total_count: int = None,
    ):
        # The instance ID.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total backup set size. Unit: Byte.
        self.total_backup_size = total_backup_size
        # The total number of entries returned.
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
                temp_model = main_models.DescribeDataBackupsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

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

class DescribeDataBackupsResponseBodyItems(DaraModel):
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
        dbinstance_id: str = None,
        data_type: str = None,
    ):
        # The UTC time when the backup ended. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC.
        self.backup_end_time = backup_end_time
        # The local time when the backup ended. The time is in the yyyy-MM-dd HH:mm:ss format. The time is your local time.
        self.backup_end_time_local = backup_end_time_local
        # The method that is used to generate the backup set. Valid values:
        # 
        # *   **Logical**: logical backup
        # *   **Physical**: physical backup
        # *   **Snapshot**: snapshot backup
        self.backup_method = backup_method
        # The backup mode.
        # 
        # Valid values for full backup:
        # 
        # *   Automated: automatic backup
        # *   Manual: manual backup
        # 
        # Valid values for point-in-time backup:
        # 
        # *   Automated: point-in-time backup after full backup
        # *   Manual: manual point-in-time backup
        # *   Period: point-in-time backup that is triggered by a backup policy
        self.backup_mode = backup_mode
        # The ID of the backup set.
        self.backup_set_id = backup_set_id
        # The size of the backup file. Unit: bytes.
        self.backup_size = backup_size
        # The UTC time when the backup started. The time is in the yyyy-MM-ddTHH:mmZ format. The time is displayed in UTC.
        self.backup_start_time = backup_start_time
        # The local time when the backup started. The time is in the yyyy-MM-dd HH:mm:ss format. The time is your local time.
        self.backup_start_time_local = backup_start_time_local
        # The status of the backup set. Valid values:
        # 
        # *   Success
        # *   Failure
        self.backup_status = backup_status
        # The name of a point-in-time backup set or the full backup set.
        self.bakset_name = bakset_name
        # *   For full backup, this parameter indicates the point in time at which the data in the data backup file is consistent.
        # *   For point-in-time backup, this parameter indicates that the returned point in time is a timestamp.
        self.consistent_time = consistent_time
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The type of the backup. Valid values:
        # 
        # *   DATA: full backup
        # *   RESTOREPOI: point-in-time backup
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

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

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

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        return self

