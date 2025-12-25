# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeCrossRegionBackupsResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        items: main_models.DescribeCrossRegionBackupsResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        region_id: str = None,
        request_id: str = None,
        start_time: str = None,
        total_record_count: int = None,
    ):
        # The end of the time range to query.
        self.end_time = end_time
        # The cross-region data backup files.
        self.items = items
        # The page number. Pages start from page 1.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of cross-region data backup files on the current page.
        self.page_record_count = page_record_count
        # The region ID of the instance.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range to query.
        self.start_time = start_time
        # The total number of entries that are returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeCrossRegionBackupsResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeCrossRegionBackupsResponseBodyItems(DaraModel):
    def __init__(
        self,
        item: List[main_models.DescribeCrossRegionBackupsResponseBodyItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.DescribeCrossRegionBackupsResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k1))

        return self

class DescribeCrossRegionBackupsResponseBodyItemsItem(DaraModel):
    def __init__(
        self,
        backup_end_time: str = None,
        backup_method: str = None,
        backup_set_scale: int = None,
        backup_set_status: int = None,
        backup_start_time: str = None,
        backup_type: str = None,
        category: str = None,
        consistent_time: str = None,
        cross_backup_download_link: str = None,
        cross_backup_id: int = None,
        cross_backup_region: str = None,
        cross_backup_set_file: str = None,
        cross_backup_set_location: str = None,
        cross_backup_set_size: int = None,
        dbinstance_storage_type: str = None,
        engine: str = None,
        engine_version: str = None,
        instance_id: int = None,
        restore_regions: main_models.DescribeCrossRegionBackupsResponseBodyItemsItemRestoreRegions = None,
    ):
        # The time when the cross-region data backup file was generated.
        self.backup_end_time = backup_end_time
        # The method that is used to generate the cross-region data backup file. Valid values:
        # 
        # *   **L**: logical backup
        # *   **P**: physical backup
        self.backup_method = backup_method
        # The level at which the cross-region data backup file is generated.
        # 
        # *   **0**: instance-level backup
        # *   **1**: database-level backup
        self.backup_set_scale = backup_set_scale
        # The status of the cross-region data backup. Valid values:
        # 
        # *   **0**: The cross-region data backup is successful.
        # *   **1**: The cross-region data backup failed.
        self.backup_set_status = backup_set_status
        # The time when the cross-region data backup started.
        self.backup_start_time = backup_start_time
        # The type of the cross-region data backup. Valid values:
        # 
        # *   **F**: full data backup
        # *   **I**: incremental data backup
        self.backup_type = backup_type
        # The RDS edition of the instance. Valid values:
        # 
        # *   **Basic**: RDS Basic Edition.
        # *   **HighAvailability**: RDS High-availability Edition.
        # *   **Finance**: RDS Enterprise Edition. This edition is available only for the China site (aliyun.com).
        self.category = category
        # The point in time that is indicated by the data in the cross-region data backup file.
        self.consistent_time = consistent_time
        # The external URL from which you can download the cross-region data backup file.
        self.cross_backup_download_link = cross_backup_download_link
        # The ID of the cross-region data backup file.
        self.cross_backup_id = cross_backup_id
        # The ID of the region in which the cross-region backup files of the instance are stored.
        self.cross_backup_region = cross_backup_region
        # The name of the compressed package that contains the cross-region data backup file.
        self.cross_backup_set_file = cross_backup_set_file
        # The location where the cross-region data backup file is stored.
        self.cross_backup_set_location = cross_backup_set_location
        # The size of the cross-region data backup file. Unit: bytes.
        self.cross_backup_set_size = cross_backup_set_size
        # The storage type. Valid values:
        # 
        # *   **local_ssd**: local SSDs. This is the recommended storage type.
        # *   **cloud_ssd**: standard SSD.
        # *   **cloud_essd**: enhanced SSD (ESSD).
        self.dbinstance_storage_type = dbinstance_storage_type
        # The database engine of the instance.
        self.engine = engine
        # The database engine version.
        self.engine_version = engine_version
        # The instance ID. This parameter is used to determine whether the instance that generates the cross-region data backup file is a primary or secondary instance.
        self.instance_id = instance_id
        # The regions to which the cross-region data backup file can be restored.
        self.restore_regions = restore_regions

    def validate(self):
        if self.restore_regions:
            self.restore_regions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_set_scale is not None:
            result['BackupSetScale'] = self.backup_set_scale

        if self.backup_set_status is not None:
            result['BackupSetStatus'] = self.backup_set_status

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.category is not None:
            result['Category'] = self.category

        if self.consistent_time is not None:
            result['ConsistentTime'] = self.consistent_time

        if self.cross_backup_download_link is not None:
            result['CrossBackupDownloadLink'] = self.cross_backup_download_link

        if self.cross_backup_id is not None:
            result['CrossBackupId'] = self.cross_backup_id

        if self.cross_backup_region is not None:
            result['CrossBackupRegion'] = self.cross_backup_region

        if self.cross_backup_set_file is not None:
            result['CrossBackupSetFile'] = self.cross_backup_set_file

        if self.cross_backup_set_location is not None:
            result['CrossBackupSetLocation'] = self.cross_backup_set_location

        if self.cross_backup_set_size is not None:
            result['CrossBackupSetSize'] = self.cross_backup_set_size

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.restore_regions is not None:
            result['RestoreRegions'] = self.restore_regions.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupSetScale') is not None:
            self.backup_set_scale = m.get('BackupSetScale')

        if m.get('BackupSetStatus') is not None:
            self.backup_set_status = m.get('BackupSetStatus')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ConsistentTime') is not None:
            self.consistent_time = m.get('ConsistentTime')

        if m.get('CrossBackupDownloadLink') is not None:
            self.cross_backup_download_link = m.get('CrossBackupDownloadLink')

        if m.get('CrossBackupId') is not None:
            self.cross_backup_id = m.get('CrossBackupId')

        if m.get('CrossBackupRegion') is not None:
            self.cross_backup_region = m.get('CrossBackupRegion')

        if m.get('CrossBackupSetFile') is not None:
            self.cross_backup_set_file = m.get('CrossBackupSetFile')

        if m.get('CrossBackupSetLocation') is not None:
            self.cross_backup_set_location = m.get('CrossBackupSetLocation')

        if m.get('CrossBackupSetSize') is not None:
            self.cross_backup_set_size = m.get('CrossBackupSetSize')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RestoreRegions') is not None:
            temp_model = main_models.DescribeCrossRegionBackupsResponseBodyItemsItemRestoreRegions()
            self.restore_regions = temp_model.from_map(m.get('RestoreRegions'))

        return self

class DescribeCrossRegionBackupsResponseBodyItemsItemRestoreRegions(DaraModel):
    def __init__(
        self,
        restore_region: List[str] = None,
    ):
        self.restore_region = restore_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.restore_region is not None:
            result['RestoreRegion'] = self.restore_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RestoreRegion') is not None:
            self.restore_region = m.get('RestoreRegion')

        return self

