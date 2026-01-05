# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupLogsResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeBackupLogsResponseBodyItems = None,
        page_number: str = None,
        page_record_count: str = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        # The details of the backup logs.
        self.items = items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
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

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeBackupLogsResponseBodyItems()
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

class DescribeBackupLogsResponseBodyItems(DaraModel):
    def __init__(
        self,
        backup_log: List[main_models.DescribeBackupLogsResponseBodyItemsBackupLog] = None,
    ):
        self.backup_log = backup_log

    def validate(self):
        if self.backup_log:
            for v1 in self.backup_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupLog'] = []
        if self.backup_log is not None:
            for k1 in self.backup_log:
                result['BackupLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_log = []
        if m.get('BackupLog') is not None:
            for k1 in m.get('BackupLog'):
                temp_model = main_models.DescribeBackupLogsResponseBodyItemsBackupLog()
                self.backup_log.append(temp_model.from_map(k1))

        return self

class DescribeBackupLogsResponseBodyItemsBackupLog(DaraModel):
    def __init__(
        self,
        backup_log_end_time: str = None,
        backup_log_id: str = None,
        backup_log_name: str = None,
        backup_log_size: str = None,
        backup_log_start_time: str = None,
        download_link: str = None,
        intranet_download_link: str = None,
        link_expired_time: str = None,
    ):
        # The time when the backup task ended. The time follows the ISO 8601 standard in the `YYYY-MM-DD\\"T\\"HH:mm:ssZ` format. The time is displayed in UTC.
        self.backup_log_end_time = backup_log_end_time
        # The ID of the backup log.
        self.backup_log_id = backup_log_id
        # The name of the backup log.
        self.backup_log_name = backup_log_name
        # The size of the backup log. Unit: bytes.
        self.backup_log_size = backup_log_size
        # The time when the backup task started. The time follows the ISO 8601 standard in the `YYYY-MM-DD\\"T\\"HH:mm:ssZ` format. The time is displayed in UTC.
        self.backup_log_start_time = backup_log_start_time
        # The public URL used to download the backup log.
        self.download_link = download_link
        # The internal URL used to download the backup log.
        self.intranet_download_link = intranet_download_link
        # The time when the download URL expires.
        self.link_expired_time = link_expired_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_log_end_time is not None:
            result['BackupLogEndTime'] = self.backup_log_end_time

        if self.backup_log_id is not None:
            result['BackupLogId'] = self.backup_log_id

        if self.backup_log_name is not None:
            result['BackupLogName'] = self.backup_log_name

        if self.backup_log_size is not None:
            result['BackupLogSize'] = self.backup_log_size

        if self.backup_log_start_time is not None:
            result['BackupLogStartTime'] = self.backup_log_start_time

        if self.download_link is not None:
            result['DownloadLink'] = self.download_link

        if self.intranet_download_link is not None:
            result['IntranetDownloadLink'] = self.intranet_download_link

        if self.link_expired_time is not None:
            result['LinkExpiredTime'] = self.link_expired_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupLogEndTime') is not None:
            self.backup_log_end_time = m.get('BackupLogEndTime')

        if m.get('BackupLogId') is not None:
            self.backup_log_id = m.get('BackupLogId')

        if m.get('BackupLogName') is not None:
            self.backup_log_name = m.get('BackupLogName')

        if m.get('BackupLogSize') is not None:
            self.backup_log_size = m.get('BackupLogSize')

        if m.get('BackupLogStartTime') is not None:
            self.backup_log_start_time = m.get('BackupLogStartTime')

        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')

        if m.get('IntranetDownloadLink') is not None:
            self.intranet_download_link = m.get('IntranetDownloadLink')

        if m.get('LinkExpiredTime') is not None:
            self.link_expired_time = m.get('LinkExpiredTime')

        return self

