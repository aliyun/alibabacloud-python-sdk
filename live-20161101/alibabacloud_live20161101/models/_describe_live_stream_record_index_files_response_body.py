# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamRecordIndexFilesResponseBody(DaraModel):
    def __init__(
        self,
        order: str = None,
        page_num: int = None,
        page_size: int = None,
        record_index_info_list: main_models.DescribeLiveStreamRecordIndexFilesResponseBodyRecordIndexInfoList = None,
        request_id: str = None,
        total_num: int = None,
        total_page: int = None,
    ):
        # The sort order.
        self.order = order
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The index files.
        self.record_index_info_list = record_index_info_list
        # The request ID.
        self.request_id = request_id
        # The total number of entries that meet the specified conditions.
        self.total_num = total_num
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.record_index_info_list:
            self.record_index_info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order is not None:
            result['Order'] = self.order

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.record_index_info_list is not None:
            result['RecordIndexInfoList'] = self.record_index_info_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecordIndexInfoList') is not None:
            temp_model = main_models.DescribeLiveStreamRecordIndexFilesResponseBodyRecordIndexInfoList()
            self.record_index_info_list = temp_model.from_map(m.get('RecordIndexInfoList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeLiveStreamRecordIndexFilesResponseBodyRecordIndexInfoList(DaraModel):
    def __init__(
        self,
        record_index_info: List[main_models.DescribeLiveStreamRecordIndexFilesResponseBodyRecordIndexInfoListRecordIndexInfo] = None,
    ):
        self.record_index_info = record_index_info

    def validate(self):
        if self.record_index_info:
            for v1 in self.record_index_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecordIndexInfo'] = []
        if self.record_index_info is not None:
            for k1 in self.record_index_info:
                result['RecordIndexInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_index_info = []
        if m.get('RecordIndexInfo') is not None:
            for k1 in m.get('RecordIndexInfo'):
                temp_model = main_models.DescribeLiveStreamRecordIndexFilesResponseBodyRecordIndexInfoListRecordIndexInfo()
                self.record_index_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamRecordIndexFilesResponseBodyRecordIndexInfoListRecordIndexInfo(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        create_time: str = None,
        domain_name: str = None,
        duration: float = None,
        end_time: str = None,
        format: str = None,
        height: int = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object: str = None,
        record_id: str = None,
        record_url: str = None,
        start_time: str = None,
        stream_name: str = None,
        width: int = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The time when the index file was created.
        self.create_time = create_time
        # The main streaming domain.
        self.domain_name = domain_name
        # The recording length. Unit: seconds.
        self.duration = duration
        # The end time of the index file. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The video format.
        self.format = format
        # The video height.
        self.height = height
        # The name of the Object Storage Service (OSS) bucket.
        self.oss_bucket = oss_bucket
        # The endpoint of the OSS bucket.
        self.oss_endpoint = oss_endpoint
        # The name of the storage file in OSS.
        self.oss_object = oss_object
        # The ID of the index file.
        self.record_id = record_id
        # The URL of the index file.
        self.record_url = record_url
        # The start time of the index file. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time
        # The name of the live stream.
        self.stream_name = stream_name
        # The video width.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.format is not None:
            result['Format'] = self.format

        if self.height is not None:
            result['Height'] = self.height

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_object is not None:
            result['OssObject'] = self.oss_object

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.record_url is not None:
            result['RecordUrl'] = self.record_url

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RecordUrl') is not None:
            self.record_url = m.get('RecordUrl')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

