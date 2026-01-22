# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeBinaryLogListResponseBody(DaraModel):
    def __init__(
        self,
        log_list: List[main_models.DescribeBinaryLogListResponseBodyLogList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_number: int = None,
    ):
        self.log_list = log_list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_number = total_number

    def validate(self):
        if self.log_list:
            for v1 in self.log_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogList'] = []
        if self.log_list is not None:
            for k1 in self.log_list:
                result['LogList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_number is not None:
            result['TotalNumber'] = self.total_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k1 in m.get('LogList'):
                temp_model = main_models.DescribeBinaryLogListResponseBodyLogList()
                self.log_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')

        return self

class DescribeBinaryLogListResponseBodyLogList(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        created_time: str = None,
        download_link: str = None,
        end_time: str = None,
        file_name: str = None,
        id: int = None,
        log_size: int = None,
        modified_time: str = None,
        purge_status: int = None,
        upload_host: str = None,
        upload_status: int = None,
    ):
        self.begin_time = begin_time
        self.created_time = created_time
        self.download_link = download_link
        self.end_time = end_time
        self.file_name = file_name
        self.id = id
        self.log_size = log_size
        self.modified_time = modified_time
        self.purge_status = purge_status
        self.upload_host = upload_host
        self.upload_status = upload_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.download_link is not None:
            result['DownloadLink'] = self.download_link

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.id is not None:
            result['Id'] = self.id

        if self.log_size is not None:
            result['LogSize'] = self.log_size

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.purge_status is not None:
            result['PurgeStatus'] = self.purge_status

        if self.upload_host is not None:
            result['UploadHost'] = self.upload_host

        if self.upload_status is not None:
            result['UploadStatus'] = self.upload_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('PurgeStatus') is not None:
            self.purge_status = m.get('PurgeStatus')

        if m.get('UploadHost') is not None:
            self.upload_host = m.get('UploadHost')

        if m.get('UploadStatus') is not None:
            self.upload_status = m.get('UploadStatus')

        return self

