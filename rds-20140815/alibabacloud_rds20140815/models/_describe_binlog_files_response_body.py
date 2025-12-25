# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeBinlogFilesResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeBinlogFilesResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_file_size: int = None,
        total_record_count: int = None,
    ):
        # The details of the log file.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of log files on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total size of the log file.
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
            temp_model = main_models.DescribeBinlogFilesResponseBodyItems()
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

class DescribeBinlogFilesResponseBodyItems(DaraModel):
    def __init__(
        self,
        bin_log_file: List[main_models.DescribeBinlogFilesResponseBodyItemsBinLogFile] = None,
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
                temp_model = main_models.DescribeBinlogFilesResponseBodyItemsBinLogFile()
                self.bin_log_file.append(temp_model.from_map(k1))

        return self

class DescribeBinlogFilesResponseBodyItemsBinLogFile(DaraModel):
    def __init__(
        self,
        checksum: str = None,
        download_link: str = None,
        file_size: int = None,
        host_instance_id: str = None,
        intranet_download_link: str = None,
        link_expired_time: str = None,
        log_begin_time: str = None,
        log_end_time: str = None,
        log_file_name: str = None,
        remote_status: str = None,
    ):
        # The checksum. The value of this parameter is calculated by using the CRC64 algorithm.
        self.checksum = checksum
        # The HTTP-based download URL of the log file. If the return value of this parameter is NULL, ApsaraDB RDS does not provide a download URL for the log file.
        self.download_link = download_link
        # The size of the log file.
        # 
        # Unit: bytes.
        self.file_size = file_size
        # The ID of the instance to which the log file belongs. This parameter helps determine whether the log file is generated on the primary instance or the secondary instance.
        # 
        # >  You can log on to the ApsaraDB RDS console and go to the instance details page. In the left-side navigation pane, click **Service Availability** to view the values of **Primary Instance No.** and **Secondary Instance No.**.
        self.host_instance_id = host_instance_id
        # The URL that is used to download files over an internal network.
        self.intranet_download_link = intranet_download_link
        # The expiration time of the URL.
        # 
        # The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.link_expired_time = link_expired_time
        # The beginning of the time range to query.
        # 
        # The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.log_begin_time = log_begin_time
        # The end of the time range to query.
        # 
        # The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.log_end_time = log_end_time
        # The log file name.
        self.log_file_name = log_file_name
        # The status of the log file that is stored in the Object Storage Service (OSS) bucket.
        # 
        # Valid values:
        # 
        # *   **Uploading**
        # *   **Completed**
        self.remote_status = remote_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checksum is not None:
            result['Checksum'] = self.checksum

        if self.download_link is not None:
            result['DownloadLink'] = self.download_link

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.host_instance_id is not None:
            result['HostInstanceID'] = self.host_instance_id

        if self.intranet_download_link is not None:
            result['IntranetDownloadLink'] = self.intranet_download_link

        if self.link_expired_time is not None:
            result['LinkExpiredTime'] = self.link_expired_time

        if self.log_begin_time is not None:
            result['LogBeginTime'] = self.log_begin_time

        if self.log_end_time is not None:
            result['LogEndTime'] = self.log_end_time

        if self.log_file_name is not None:
            result['LogFileName'] = self.log_file_name

        if self.remote_status is not None:
            result['RemoteStatus'] = self.remote_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')

        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('HostInstanceID') is not None:
            self.host_instance_id = m.get('HostInstanceID')

        if m.get('IntranetDownloadLink') is not None:
            self.intranet_download_link = m.get('IntranetDownloadLink')

        if m.get('LinkExpiredTime') is not None:
            self.link_expired_time = m.get('LinkExpiredTime')

        if m.get('LogBeginTime') is not None:
            self.log_begin_time = m.get('LogBeginTime')

        if m.get('LogEndTime') is not None:
            self.log_end_time = m.get('LogEndTime')

        if m.get('LogFileName') is not None:
            self.log_file_name = m.get('LogFileName')

        if m.get('RemoteStatus') is not None:
            self.remote_status = m.get('RemoteStatus')

        return self

