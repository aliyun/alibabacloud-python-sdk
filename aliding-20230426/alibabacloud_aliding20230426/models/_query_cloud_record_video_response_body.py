# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryCloudRecordVideoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        video_list: List[main_models.QueryCloudRecordVideoResponseBodyVideoList] = None,
    ):
        # requestId
        self.request_id = request_id
        self.video_list = video_list

    def validate(self):
        if self.video_list:
            for v1 in self.video_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['videoList'] = []
        if self.video_list is not None:
            for k1 in self.video_list:
                result['videoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.video_list = []
        if m.get('videoList') is not None:
            for k1 in m.get('videoList'):
                temp_model = main_models.QueryCloudRecordVideoResponseBodyVideoList()
                self.video_list.append(temp_model.from_map(k1))

        return self

class QueryCloudRecordVideoResponseBodyVideoList(DaraModel):
    def __init__(
        self,
        duration: int = None,
        end_time: int = None,
        file_size: int = None,
        media_id: str = None,
        record_id: str = None,
        record_type: int = None,
        region_id: str = None,
        start_time: int = None,
        user_id: str = None,
    ):
        self.duration = duration
        self.end_time = end_time
        self.file_size = file_size
        self.media_id = media_id
        self.record_id = record_id
        self.record_type = record_type
        self.region_id = region_id
        self.start_time = start_time
        self.user_id = user_id

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

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

