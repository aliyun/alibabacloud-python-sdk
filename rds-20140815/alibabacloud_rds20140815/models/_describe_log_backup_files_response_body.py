# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeLogBackupFilesResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeLogBackupFilesResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_file_size: int = None,
        total_record_count: int = None,
    ):
        # The details of log files.
        self.items = items
        # The page number of the page returned.
        self.page_number = page_number
        # The number of log files on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total size of log files. Unit: bytes.
        self.total_file_size = total_file_size
        # The total number of log files.
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

        if self.total_file_size is not None:
            result['TotalFileSize'] = self.total_file_size

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeLogBackupFilesResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalFileSize') is not None:
            self.total_file_size = m.get('TotalFileSize')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeLogBackupFilesResponseBodyItems(DaraModel):
    def __init__(
        self,
        bin_log_file: List[main_models.DescribeLogBackupFilesResponseBodyItemsBinLogFile] = None,
    ):
        self.bin_log_file = bin_log_file

    def validate(self):
        if self.bin_log_file:
            for v1 in self.bin_log_file:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BinLogFile'] = []
        if self.bin_log_file is not None:
            for k1 in self.bin_log_file:
                result['BinLogFile'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bin_log_file = []
        if m.get('BinLogFile') is not None:
            for k1 in m.get('BinLogFile'):
                temp_model = main_models.DescribeLogBackupFilesResponseBodyItemsBinLogFile()
                self.bin_log_file.append(temp_model.from_map(k1))

        return self

class DescribeLogBackupFilesResponseBodyItemsBinLogFile(DaraModel):
    def __init__(
        self,
        download_link: str = None,
        file_size: int = None,
        intranet_download_link: str = None,
        link_expired_time: str = None,
        log_begin_time: str = None,
        log_end_time: str = None,
    ):
        # The HTTP-based download URL of the log file. If the log file cannot be downloaded, an empty string is returned.
        self.download_link = download_link
        # The size of the log file. Unit: bytes.
        self.file_size = file_size
        # The URL that is used to download the log file over an internal network. If the log file cannot be downloaded, an empty string is returned. This URL is valid for one hour.
        self.intranet_download_link = intranet_download_link
        # The expiration time of the URL. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.link_expired_time = link_expired_time
        # The start time of the log file. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.log_begin_time = log_begin_time
        # The end time of the log file. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.log_end_time = log_end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.intranet_download_link is not None:
            result['IntranetDownloadLink'] = self.intranet_download_link

        if self.link_expired_time is not None:
            result['LinkExpiredTime'] = self.link_expired_time

        if self.log_begin_time is not None:
            result['LogBeginTime'] = self.log_begin_time

        if self.log_end_time is not None:
            result['LogEndTime'] = self.log_end_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('IntranetDownloadLink') is not None:
            self.intranet_download_link = m.get('IntranetDownloadLink')

        if m.get('LinkExpiredTime') is not None:
            self.link_expired_time = m.get('LinkExpiredTime')

        if m.get('LogBeginTime') is not None:
            self.log_begin_time = m.get('LogBeginTime')

        if m.get('LogEndTime') is not None:
            self.log_end_time = m.get('LogEndTime')

        return self

