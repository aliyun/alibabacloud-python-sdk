# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeCrossRegionLogBackupFilesResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        items: main_models.DescribeCrossRegionLogBackupFilesResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        region_id: str = None,
        request_id: str = None,
        start_time: str = None,
        total_record_count: int = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The end of the time range to query. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The cross-region log backup files.
        self.items = items
        # The page number. Pages start from page 1.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of cross-region backup files on the current page.
        self.page_record_count = page_record_count
        # The region ID of the instance.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range to query. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

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
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeCrossRegionLogBackupFilesResponseBodyItems()
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

class DescribeCrossRegionLogBackupFilesResponseBodyItems(DaraModel):
    def __init__(
        self,
        item: List[main_models.DescribeCrossRegionLogBackupFilesResponseBodyItemsItem] = None,
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
                temp_model = main_models.DescribeCrossRegionLogBackupFilesResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k1))

        return self

class DescribeCrossRegionLogBackupFilesResponseBodyItemsItem(DaraModel):
    def __init__(
        self,
        cross_backup_region: str = None,
        cross_download_link: str = None,
        cross_intranet_download_link: str = None,
        cross_log_backup_id: int = None,
        cross_log_backup_size: int = None,
        instance_id: int = None,
        link_expired_time: str = None,
        log_begin_time: str = None,
        log_end_time: str = None,
        log_file_name: str = None,
    ):
        # The ID of the destination region within which the cross-region backup file is stored.
        self.cross_backup_region = cross_backup_region
        # The external URL from which you can download the cross-region log backup file.
        self.cross_download_link = cross_download_link
        # The internal URL from which you can download the cross-region log backup file.
        self.cross_intranet_download_link = cross_intranet_download_link
        # The ID of the cross-region log backup file.
        self.cross_log_backup_id = cross_log_backup_id
        # The size of the cross-region log backup file. Unit: bytes.
        self.cross_log_backup_size = cross_log_backup_size
        # The instance ID.
        self.instance_id = instance_id
        # The time when the URL expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.link_expired_time = link_expired_time
        # The start time of the cross-region log backup file. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.log_begin_time = log_begin_time
        # The end time of the cross-region log backup file. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.log_end_time = log_end_time
        # The name of the cross-region log backup file.
        self.log_file_name = log_file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_backup_region is not None:
            result['CrossBackupRegion'] = self.cross_backup_region

        if self.cross_download_link is not None:
            result['CrossDownloadLink'] = self.cross_download_link

        if self.cross_intranet_download_link is not None:
            result['CrossIntranetDownloadLink'] = self.cross_intranet_download_link

        if self.cross_log_backup_id is not None:
            result['CrossLogBackupId'] = self.cross_log_backup_id

        if self.cross_log_backup_size is not None:
            result['CrossLogBackupSize'] = self.cross_log_backup_size

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.link_expired_time is not None:
            result['LinkExpiredTime'] = self.link_expired_time

        if self.log_begin_time is not None:
            result['LogBeginTime'] = self.log_begin_time

        if self.log_end_time is not None:
            result['LogEndTime'] = self.log_end_time

        if self.log_file_name is not None:
            result['LogFileName'] = self.log_file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossBackupRegion') is not None:
            self.cross_backup_region = m.get('CrossBackupRegion')

        if m.get('CrossDownloadLink') is not None:
            self.cross_download_link = m.get('CrossDownloadLink')

        if m.get('CrossIntranetDownloadLink') is not None:
            self.cross_intranet_download_link = m.get('CrossIntranetDownloadLink')

        if m.get('CrossLogBackupId') is not None:
            self.cross_log_backup_id = m.get('CrossLogBackupId')

        if m.get('CrossLogBackupSize') is not None:
            self.cross_log_backup_size = m.get('CrossLogBackupSize')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LinkExpiredTime') is not None:
            self.link_expired_time = m.get('LinkExpiredTime')

        if m.get('LogBeginTime') is not None:
            self.log_begin_time = m.get('LogBeginTime')

        if m.get('LogEndTime') is not None:
            self.log_end_time = m.get('LogEndTime')

        if m.get('LogFileName') is not None:
            self.log_file_name = m.get('LogFileName')

        return self

