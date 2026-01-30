# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeRecordsResponseBody(DaraModel):
    def __init__(
        self,
        next_start_time: str = None,
        page_count: int = None,
        page_num: int = None,
        page_size: int = None,
        records: List[main_models.DescribeRecordsResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.next_start_time = next_start_time
        self.page_count = page_count
        self.page_num = page_num
        self.page_size = page_size
        self.records = records
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_start_time is not None:
            result['NextStartTime'] = self.next_start_time

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextStartTime') is not None:
            self.next_start_time = m.get('NextStartTime')

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.DescribeRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRecordsResponseBodyRecords(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        file_format: str = None,
        height: int = None,
        id: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object: str = None,
        start_time: str = None,
        stream_id: str = None,
        template_id: str = None,
        type: str = None,
        url: str = None,
        width: int = None,
    ):
        self.end_time = end_time
        self.file_format = file_format
        self.height = height
        self.id = id
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        self.oss_object = oss_object
        self.start_time = start_time
        self.stream_id = stream_id
        self.template_id = template_id
        self.type = type
        self.url = url
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.file_format is not None:
            result['FileFormat'] = self.file_format

        if self.height is not None:
            result['Height'] = self.height

        if self.id is not None:
            result['Id'] = self.id

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_object is not None:
            result['OssObject'] = self.oss_object

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_id is not None:
            result['StreamId'] = self.stream_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

