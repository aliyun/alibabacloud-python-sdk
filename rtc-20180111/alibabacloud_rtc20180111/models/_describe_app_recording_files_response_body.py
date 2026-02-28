# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeAppRecordingFilesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeAppRecordingFilesResponseBodyItems] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_cnt: int = None,
    ):
        self.items = items
        self.page_no = page_no
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.total_cnt = total_cnt

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAppRecordingFilesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')

        return self

class DescribeAppRecordingFilesResponseBodyItems(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        channel_id: str = None,
        file_create_ts: int = None,
        file_duration: int = None,
        file_path: str = None,
        file_size: int = None,
        region: int = None,
        start_ts: int = None,
        task_id: str = None,
        vendor: int = None,
    ):
        self.bucket = bucket
        self.channel_id = channel_id
        self.file_create_ts = file_create_ts
        self.file_duration = file_duration
        self.file_path = file_path
        self.file_size = file_size
        self.region = region
        self.start_ts = start_ts
        self.task_id = task_id
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.file_create_ts is not None:
            result['FileCreateTs'] = self.file_create_ts

        if self.file_duration is not None:
            result['FileDuration'] = self.file_duration

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.region is not None:
            result['Region'] = self.region

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('FileCreateTs') is not None:
            self.file_create_ts = m.get('FileCreateTs')

        if m.get('FileDuration') is not None:
            self.file_duration = m.get('FileDuration')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

