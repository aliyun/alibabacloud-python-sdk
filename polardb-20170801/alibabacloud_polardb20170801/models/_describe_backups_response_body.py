# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupsResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeBackupsResponseBodyItems = None,
        page_number: str = None,
        page_record_count: str = None,
        request_id: str = None,
        total_level_2backup_size: str = None,
        total_record_count: str = None,
    ):
        # The queried backup sets.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        self.total_level_2backup_size = total_level_2backup_size
        # The total number of returned entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_level_2backup_size is not None:
            result['TotalLevel2BackupSize'] = self.total_level_2backup_size

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeBackupsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalLevel2BackupSize') is not None:
            self.total_level_2backup_size = m.get('TotalLevel2BackupSize')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeBackupsResponseBodyItems(DaraModel):
    def __init__(
        self,
        backup: List[main_models.DescribeBackupsResponseBodyItemsBackup] = None,
    ):
        self.backup = backup

    def validate(self):
        if self.backup:
            for v1 in self.backup:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Backup'] = []
        if self.backup is not None:
            for k1 in self.backup:
                result['Backup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup = []
        if m.get('Backup') is not None:
            for k1 in m.get('Backup'):
                temp_model = main_models.DescribeBackupsResponseBodyItemsBackup()
                self.backup.append(temp_model.from_map(k1))

        return self

class DescribeBackupsResponseBodyItemsBackup(DaraModel):
    def __init__(
        self,
        backup_end_time: str = None,
        backup_id: str = None,
        backup_method: str = None,
        backup_mode: str = None,
        backup_set_size: str = None,
        backup_start_time: str = None,
        backup_status: str = None,
        backup_type: str = None,
        backups_level: str = None,
        consistent_time: str = None,
        dbcluster_id: str = None,
        expect_expire_time: str = None,
        expect_expire_type: str = None,
        is_avail: str = None,
    ):
        # The end time of the backup task. The time is displayed in UTC.
        self.backup_end_time = backup_end_time
        # The ID of the backup set.
        self.backup_id = backup_id
        # The backup method. Only **Snapshot** may be returned.
        self.backup_method = backup_method
        # The backup mode. Valid values:
        # 
        # *   **Automated**
        # *   **Manual**
        self.backup_mode = backup_mode
        # The size of the backup set. Unit: bytes.
        # 
        # > After you delete the target snapshot backups, the storage space that is consumed by the backups is released. The released storage space is smaller than the size of the backup file, because the snapshots share specific data blocks. For more information, see [FAQ about backup](https://help.aliyun.com/document_detail/164881.html).
        self.backup_set_size = backup_set_size
        # The start time of the backup task. The time is displayed in UTC. Unit: seconds.
        self.backup_start_time = backup_start_time
        # The status of the backup set. Valid values:
        # 
        # *   **Success**
        # *   **Failed**
        self.backup_status = backup_status
        # The type of the backup. Only **FullBackup** may be returned.
        self.backup_type = backup_type
        # The level of the backup set. Valid values:
        # 
        # *   **Level-1**
        # *   **Level-2**
        self.backups_level = backups_level
        # The snapshot checkpoint time. The value follows the Unix time format. Unit: seconds.
        self.consistent_time = consistent_time
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The expected expiration time of the backup set (This parameter is supported only for clusters for which sparse backup is enabled).
        self.expect_expire_time = expect_expire_time
        # The expected expiration type of the backup set (This parameter is supported only for instances that are enabled with sparse backup).
        # 
        # Valid values:
        # 
        # *   NEVER
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   EXPIRED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DELAY
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.expect_expire_type = expect_expire_type
        # Indicates whether the backup set is available. Valid values:
        # 
        # *   **0**: The backup set is unavailable.
        # *   **1**: The backup set is available.
        self.is_avail = is_avail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_set_size is not None:
            result['BackupSetSize'] = self.backup_set_size

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.backups_level is not None:
            result['BackupsLevel'] = self.backups_level

        if self.consistent_time is not None:
            result['ConsistentTime'] = self.consistent_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.expect_expire_time is not None:
            result['ExpectExpireTime'] = self.expect_expire_time

        if self.expect_expire_type is not None:
            result['ExpectExpireType'] = self.expect_expire_type

        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupSetSize') is not None:
            self.backup_set_size = m.get('BackupSetSize')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('BackupsLevel') is not None:
            self.backups_level = m.get('BackupsLevel')

        if m.get('ConsistentTime') is not None:
            self.consistent_time = m.get('ConsistentTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ExpectExpireTime') is not None:
            self.expect_expire_time = m.get('ExpectExpireTime')

        if m.get('ExpectExpireType') is not None:
            self.expect_expire_type = m.get('ExpectExpireType')

        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')

        return self

