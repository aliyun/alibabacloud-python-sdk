# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamRecordContentResponseBody(DaraModel):
    def __init__(
        self,
        record_content_info_list: main_models.DescribeLiveStreamRecordContentResponseBodyRecordContentInfoList = None,
        request_id: str = None,
    ):
        # The ID of the request.
        self.record_content_info_list = record_content_info_list
        # The end of the time range to query. The time range that is specified by the StartTime and EndTime parameters cannot exceed 4 days. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.request_id = request_id

    def validate(self):
        if self.record_content_info_list:
            self.record_content_info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_content_info_list is not None:
            result['RecordContentInfoList'] = self.record_content_info_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordContentInfoList') is not None:
            temp_model = main_models.DescribeLiveStreamRecordContentResponseBodyRecordContentInfoList()
            self.record_content_info_list = temp_model.from_map(m.get('RecordContentInfoList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveStreamRecordContentResponseBodyRecordContentInfoList(DaraModel):
    def __init__(
        self,
        record_content_info: List[main_models.DescribeLiveStreamRecordContentResponseBodyRecordContentInfoListRecordContentInfo] = None,
    ):
        self.record_content_info = record_content_info

    def validate(self):
        if self.record_content_info:
            for v1 in self.record_content_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecordContentInfo'] = []
        if self.record_content_info is not None:
            for k1 in self.record_content_info:
                result['RecordContentInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record_content_info = []
        if m.get('RecordContentInfo') is not None:
            for k1 in m.get('RecordContentInfo'):
                temp_model = main_models.DescribeLiveStreamRecordContentResponseBodyRecordContentInfoListRecordContentInfo()
                self.record_content_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamRecordContentResponseBodyRecordContentInfoListRecordContentInfo(DaraModel):
    def __init__(
        self,
        duration: float = None,
        end_time: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object_prefix: str = None,
        start_time: str = None,
    ):
        # The beginning of the time range for which the recordings were queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.duration = duration
        # The recordings.
        self.end_time = end_time
        # The recording length. Unit: seconds.
        self.oss_bucket = oss_bucket
        # The naming rule of recordings in OSS.
        self.oss_endpoint = oss_endpoint
        # The name of the Object Storage Service (OSS) bucket.
        self.oss_object_prefix = oss_object_prefix
        # The end of the time range for which the recordings were queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_object_prefix is not None:
            result['OssObjectPrefix'] = self.oss_object_prefix

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssObjectPrefix') is not None:
            self.oss_object_prefix = m.get('OssObjectPrefix')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

