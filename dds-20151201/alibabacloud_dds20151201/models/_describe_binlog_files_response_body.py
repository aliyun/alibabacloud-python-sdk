# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeBinlogFilesResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeBinlogFilesResponseBodyItems = None,
        max_records_per_page: int = None,
        page_number: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        self.max_records_per_page = max_records_per_page
        self.page_number = page_number
        self.request_id = request_id
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

        if self.max_records_per_page is not None:
            result['MaxRecordsPerPage'] = self.max_records_per_page

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeBinlogFilesResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('MaxRecordsPerPage') is not None:
            self.max_records_per_page = m.get('MaxRecordsPerPage')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeBinlogFilesResponseBodyItems(DaraModel):
    def __init__(
        self,
        log_file: List[main_models.DescribeBinlogFilesResponseBodyItemsLogFile] = None,
    ):
        self.log_file = log_file

    def validate(self):
        if self.log_file:
            for v1 in self.log_file:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogFile'] = []
        if self.log_file is not None:
            for k1 in self.log_file:
                result['LogFile'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_file = []
        if m.get('LogFile') is not None:
            for k1 in m.get('LogFile'):
                temp_model = main_models.DescribeBinlogFilesResponseBodyItemsLogFile()
                self.log_file.append(temp_model.from_map(k1))

        return self

class DescribeBinlogFilesResponseBodyItemsLogFile(DaraModel):
    def __init__(
        self,
        bin_log_id: str = None,
        download_link: str = None,
        dump_bucket: str = None,
        dump_download_url: str = None,
        dump_state: int = None,
        file_id: str = None,
        file_size: str = None,
        link_expired_time: str = None,
        log_begin_time: str = None,
        log_end_time: str = None,
        log_file_name: str = None,
        log_status: str = None,
        ossendpoint: str = None,
    ):
        self.bin_log_id = bin_log_id
        self.download_link = download_link
        self.dump_bucket = dump_bucket
        self.dump_download_url = dump_download_url
        self.dump_state = dump_state
        self.file_id = file_id
        self.file_size = file_size
        self.link_expired_time = link_expired_time
        self.log_begin_time = log_begin_time
        self.log_end_time = log_end_time
        self.log_file_name = log_file_name
        self.log_status = log_status
        self.ossendpoint = ossendpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bin_log_id is not None:
            result['BinLogId'] = self.bin_log_id

        if self.download_link is not None:
            result['DownloadLink'] = self.download_link

        if self.dump_bucket is not None:
            result['DumpBucket'] = self.dump_bucket

        if self.dump_download_url is not None:
            result['DumpDownloadURL'] = self.dump_download_url

        if self.dump_state is not None:
            result['DumpState'] = self.dump_state

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.link_expired_time is not None:
            result['LinkExpiredTime'] = self.link_expired_time

        if self.log_begin_time is not None:
            result['LogBeginTime'] = self.log_begin_time

        if self.log_end_time is not None:
            result['LogEndTime'] = self.log_end_time

        if self.log_file_name is not None:
            result['LogFileName'] = self.log_file_name

        if self.log_status is not None:
            result['LogStatus'] = self.log_status

        if self.ossendpoint is not None:
            result['OSSEndpoint'] = self.ossendpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BinLogId') is not None:
            self.bin_log_id = m.get('BinLogId')

        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')

        if m.get('DumpBucket') is not None:
            self.dump_bucket = m.get('DumpBucket')

        if m.get('DumpDownloadURL') is not None:
            self.dump_download_url = m.get('DumpDownloadURL')

        if m.get('DumpState') is not None:
            self.dump_state = m.get('DumpState')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('LinkExpiredTime') is not None:
            self.link_expired_time = m.get('LinkExpiredTime')

        if m.get('LogBeginTime') is not None:
            self.log_begin_time = m.get('LogBeginTime')

        if m.get('LogEndTime') is not None:
            self.log_end_time = m.get('LogEndTime')

        if m.get('LogFileName') is not None:
            self.log_file_name = m.get('LogFileName')

        if m.get('LogStatus') is not None:
            self.log_status = m.get('LogStatus')

        if m.get('OSSEndpoint') is not None:
            self.ossendpoint = m.get('OSSEndpoint')

        return self

