# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDetachedBackupsResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDetachedBackupsResponseBodyItems = None,
        page_number: str = None,
        page_record_count: str = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        # The queried backup sets.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeDetachedBackupsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDetachedBackupsResponseBodyItems(DaraModel):
    def __init__(
        self,
        backup: List[main_models.DescribeDetachedBackupsResponseBodyItemsBackup] = None,
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
                temp_model = main_models.DescribeDetachedBackupsResponseBodyItemsBackup()
                self.backup.append(temp_model.from_map(k1))

        return self

class DescribeDetachedBackupsResponseBodyItemsBackup(DaraModel):
    def __init__(
        self,
        backup_download_url: str = None,
        backup_end_time: str = None,
        backup_id: str = None,
        backup_intranet_download_url: str = None,
        backup_method: str = None,
        backup_mode: str = None,
        backup_size: int = None,
        backup_start_time: str = None,
        backup_status: str = None,
        backup_type: str = None,
        consistent_time: int = None,
        dbinstance_comment: str = None,
        dbinstance_id: str = None,
        host_instance_id: str = None,
        is_avail: int = None,
        meta_status: str = None,
        store_status: str = None,
    ):
        # The URL that is used to download the diagnostic report over the Internet. If the diagnostic report cannot be downloaded, an empty string is returned.
        self.backup_download_url = backup_download_url
        # The end time of the backup task.
        # 
        # The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.backup_end_time = backup_end_time
        # The ID of the backup set.
        self.backup_id = backup_id
        # The URL that is used to download the log file over an internal network. If the log file cannot be downloaded, an empty string is returned.
        self.backup_intranet_download_url = backup_intranet_download_url
        # The method that is used to generate the data backup file. Valid values:
        # 
        # *   **Logical**: logical backup
        # *   **Physical**: physical backup
        self.backup_method = backup_method
        # The backup method. Valid values:
        # 
        # *   **Automated**
        # *   **Manual**
        self.backup_mode = backup_mode
        # The backup size. Unit: bytes.
        self.backup_size = backup_size
        # The start time of the backup task.
        # 
        # The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.backup_start_time = backup_start_time
        # The status of the backup set. Valid values:
        # 
        # *   **Success**
        # *   **Failed**
        self.backup_status = backup_status
        # The backup type of the backup file. Valid values:
        # 
        # *   **FullBackup**
        # *   **IncrementalBackup**
        self.backup_type = backup_type
        # The point in time at which the data in the backup set is consistent. The return value of this parameter is a timestamp.
        # 
        # >  If the instance runs MySQL 5.6, a timestamp is returned. Otherwise, the value 0 is returned.
        self.consistent_time = consistent_time
        # The description of the instance.
        self.dbinstance_comment = dbinstance_comment
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The ID of the instance that generates the backup set. This parameter is used to indicate whether the instance that generates the backup set is a primary instance or a secondary instance.
        self.host_instance_id = host_instance_id
        # Indicates whether the backup set is available. Valid values:
        # 
        # *   **0**: The backup set is unavailable.
        # *   **1**: The backup set is available.
        self.is_avail = is_avail
        # The status of the backup set that is used to restore individual databases or tables. Valid values:
        # 
        # *   **OK**: The backup set is normal.
        # *   **LARGE**: The backup set contains an abnormally large number of tables. It cannot be used to restore individual databases or tables.
        # *   **EMPTY**: The backup set is generated from a failed backup task.
        self.meta_status = meta_status
        # Indicates whether the data backup file can be deleted. Valid values:
        # 
        # *   **Enabled**
        # *   **Disabled**
        self.store_status = store_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_download_url is not None:
            result['BackupDownloadURL'] = self.backup_download_url

        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_intranet_download_url is not None:
            result['BackupIntranetDownloadURL'] = self.backup_intranet_download_url

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.consistent_time is not None:
            result['ConsistentTime'] = self.consistent_time

        if self.dbinstance_comment is not None:
            result['DBInstanceComment'] = self.dbinstance_comment

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.host_instance_id is not None:
            result['HostInstanceID'] = self.host_instance_id

        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail

        if self.meta_status is not None:
            result['MetaStatus'] = self.meta_status

        if self.store_status is not None:
            result['StoreStatus'] = self.store_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')

        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupIntranetDownloadURL') is not None:
            self.backup_intranet_download_url = m.get('BackupIntranetDownloadURL')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('ConsistentTime') is not None:
            self.consistent_time = m.get('ConsistentTime')

        if m.get('DBInstanceComment') is not None:
            self.dbinstance_comment = m.get('DBInstanceComment')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('HostInstanceID') is not None:
            self.host_instance_id = m.get('HostInstanceID')

        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')

        if m.get('MetaStatus') is not None:
            self.meta_status = m.get('MetaStatus')

        if m.get('StoreStatus') is not None:
            self.store_status = m.get('StoreStatus')

        return self

