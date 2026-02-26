# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupsResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeBackupsResponseBodyItems = None,
        page_number: str = None,
        page_record_count: str = None,
        request_id: str = None,
        total_ecs_snapshot_size: int = None,
        total_record_count: str = None,
    ):
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of backup sets on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The size of the snapshot chain of the instance. Unit: bytes.
        self.total_ecs_snapshot_size = total_ecs_snapshot_size
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

        if self.total_ecs_snapshot_size is not None:
            result['TotalEcsSnapshotSize'] = self.total_ecs_snapshot_size

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

        if m.get('TotalEcsSnapshotSize') is not None:
            self.total_ecs_snapshot_size = m.get('TotalEcsSnapshotSize')

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
        backup_download_link_by_db: main_models.DescribeBackupsResponseBodyItemsBackupBackupDownloadLinkByDB = None,
        backup_download_url: str = None,
        backup_end_time: str = None,
        backup_id: str = None,
        backup_initiator: str = None,
        backup_intranet_download_url: str = None,
        backup_method: str = None,
        backup_mode: str = None,
        backup_size: int = None,
        backup_start_time: str = None,
        backup_status: str = None,
        backup_type: str = None,
        checksum: str = None,
        consistent_time: int = None,
        copy_only_backup: str = None,
        dbinstance_id: str = None,
        encryption: str = None,
        engine: str = None,
        engine_version: str = None,
        expect_expire_time: str = None,
        host_instance_id: str = None,
        is_avail: int = None,
        meta_status: str = None,
        storage_class: str = None,
        store_status: str = None,
    ):
        self.backup_download_link_by_db = backup_download_link_by_db
        self.backup_download_url = backup_download_url
        self.backup_end_time = backup_end_time
        self.backup_id = backup_id
        self.backup_initiator = backup_initiator
        self.backup_intranet_download_url = backup_intranet_download_url
        self.backup_method = backup_method
        self.backup_mode = backup_mode
        self.backup_size = backup_size
        self.backup_start_time = backup_start_time
        self.backup_status = backup_status
        self.backup_type = backup_type
        self.checksum = checksum
        self.consistent_time = consistent_time
        self.copy_only_backup = copy_only_backup
        self.dbinstance_id = dbinstance_id
        self.encryption = encryption
        self.engine = engine
        self.engine_version = engine_version
        self.expect_expire_time = expect_expire_time
        self.host_instance_id = host_instance_id
        self.is_avail = is_avail
        self.meta_status = meta_status
        self.storage_class = storage_class
        self.store_status = store_status

    def validate(self):
        if self.backup_download_link_by_db:
            self.backup_download_link_by_db.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_download_link_by_db is not None:
            result['BackupDownloadLinkByDB'] = self.backup_download_link_by_db.to_map()

        if self.backup_download_url is not None:
            result['BackupDownloadURL'] = self.backup_download_url

        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_initiator is not None:
            result['BackupInitiator'] = self.backup_initiator

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

        if self.checksum is not None:
            result['Checksum'] = self.checksum

        if self.consistent_time is not None:
            result['ConsistentTime'] = self.consistent_time

        if self.copy_only_backup is not None:
            result['CopyOnlyBackup'] = self.copy_only_backup

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.encryption is not None:
            result['Encryption'] = self.encryption

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expect_expire_time is not None:
            result['ExpectExpireTime'] = self.expect_expire_time

        if self.host_instance_id is not None:
            result['HostInstanceID'] = self.host_instance_id

        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail

        if self.meta_status is not None:
            result['MetaStatus'] = self.meta_status

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.store_status is not None:
            result['StoreStatus'] = self.store_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupDownloadLinkByDB') is not None:
            temp_model = main_models.DescribeBackupsResponseBodyItemsBackupBackupDownloadLinkByDB()
            self.backup_download_link_by_db = temp_model.from_map(m.get('BackupDownloadLinkByDB'))

        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')

        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupInitiator') is not None:
            self.backup_initiator = m.get('BackupInitiator')

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

        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')

        if m.get('ConsistentTime') is not None:
            self.consistent_time = m.get('ConsistentTime')

        if m.get('CopyOnlyBackup') is not None:
            self.copy_only_backup = m.get('CopyOnlyBackup')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpectExpireTime') is not None:
            self.expect_expire_time = m.get('ExpectExpireTime')

        if m.get('HostInstanceID') is not None:
            self.host_instance_id = m.get('HostInstanceID')

        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')

        if m.get('MetaStatus') is not None:
            self.meta_status = m.get('MetaStatus')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('StoreStatus') is not None:
            self.store_status = m.get('StoreStatus')

        return self

class DescribeBackupsResponseBodyItemsBackupBackupDownloadLinkByDB(DaraModel):
    def __init__(
        self,
        backup_download_link_by_db: List[main_models.DescribeBackupsResponseBodyItemsBackupBackupDownloadLinkByDBBackupDownloadLinkByDB] = None,
    ):
        self.backup_download_link_by_db = backup_download_link_by_db

    def validate(self):
        if self.backup_download_link_by_db:
            for v1 in self.backup_download_link_by_db:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupDownloadLinkByDB'] = []
        if self.backup_download_link_by_db is not None:
            for k1 in self.backup_download_link_by_db:
                result['BackupDownloadLinkByDB'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_download_link_by_db = []
        if m.get('BackupDownloadLinkByDB') is not None:
            for k1 in m.get('BackupDownloadLinkByDB'):
                temp_model = main_models.DescribeBackupsResponseBodyItemsBackupBackupDownloadLinkByDBBackupDownloadLinkByDB()
                self.backup_download_link_by_db.append(temp_model.from_map(k1))

        return self

class DescribeBackupsResponseBodyItemsBackupBackupDownloadLinkByDBBackupDownloadLinkByDB(DaraModel):
    def __init__(
        self,
        data_base: str = None,
        download_link: str = None,
        intranet_download_link: str = None,
    ):
        self.data_base = data_base
        self.download_link = download_link
        self.intranet_download_link = intranet_download_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_base is not None:
            result['DataBase'] = self.data_base

        if self.download_link is not None:
            result['DownloadLink'] = self.download_link

        if self.intranet_download_link is not None:
            result['IntranetDownloadLink'] = self.intranet_download_link

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataBase') is not None:
            self.data_base = m.get('DataBase')

        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')

        if m.get('IntranetDownloadLink') is not None:
            self.intranet_download_link = m.get('IntranetDownloadLink')

        return self

