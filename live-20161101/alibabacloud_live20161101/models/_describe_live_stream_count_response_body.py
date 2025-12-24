# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamCountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stream_count_infos: main_models.DescribeLiveStreamCountResponseBodyStreamCountInfos = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The statistics of the live streams.
        self.stream_count_infos = stream_count_infos

    def validate(self):
        if self.stream_count_infos:
            self.stream_count_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stream_count_infos is not None:
            result['StreamCountInfos'] = self.stream_count_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamCountInfos') is not None:
            temp_model = main_models.DescribeLiveStreamCountResponseBodyStreamCountInfos()
            self.stream_count_infos = temp_model.from_map(m.get('StreamCountInfos'))

        return self

class DescribeLiveStreamCountResponseBodyStreamCountInfos(DaraModel):
    def __init__(
        self,
        stream_count_info: List[main_models.DescribeLiveStreamCountResponseBodyStreamCountInfosStreamCountInfo] = None,
    ):
        self.stream_count_info = stream_count_info

    def validate(self):
        if self.stream_count_info:
            for v1 in self.stream_count_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StreamCountInfo'] = []
        if self.stream_count_info is not None:
            for k1 in self.stream_count_info:
                result['StreamCountInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stream_count_info = []
        if m.get('StreamCountInfo') is not None:
            for k1 in m.get('StreamCountInfo'):
                temp_model = main_models.DescribeLiveStreamCountResponseBodyStreamCountInfosStreamCountInfo()
                self.stream_count_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamCountResponseBodyStreamCountInfosStreamCountInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        limit: int = None,
        stream_count_details: main_models.DescribeLiveStreamCountResponseBodyStreamCountInfosStreamCountInfoStreamCountDetails = None,
        type: str = None,
    ):
        # The number of online streams.
        self.count = count
        # The maximum allowed number of concurrently ingested streams. This parameter is available only to users in the whitelist.
        self.limit = limit
        # The information about the live streams.
        self.stream_count_details = stream_count_details
        # The type of the live stream. Valid values:
        # 
        # *   **raw**: source streams
        # *   **trans**: transcoded streams
        self.type = type

    def validate(self):
        if self.stream_count_details:
            self.stream_count_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.stream_count_details is not None:
            result['StreamCountDetails'] = self.stream_count_details.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('StreamCountDetails') is not None:
            temp_model = main_models.DescribeLiveStreamCountResponseBodyStreamCountInfosStreamCountInfoStreamCountDetails()
            self.stream_count_details = temp_model.from_map(m.get('StreamCountDetails'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeLiveStreamCountResponseBodyStreamCountInfosStreamCountInfoStreamCountDetails(DaraModel):
    def __init__(
        self,
        stream_count_detail: List[main_models.DescribeLiveStreamCountResponseBodyStreamCountInfosStreamCountInfoStreamCountDetailsStreamCountDetail] = None,
    ):
        self.stream_count_detail = stream_count_detail

    def validate(self):
        if self.stream_count_detail:
            for v1 in self.stream_count_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StreamCountDetail'] = []
        if self.stream_count_detail is not None:
            for k1 in self.stream_count_detail:
                result['StreamCountDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stream_count_detail = []
        if m.get('StreamCountDetail') is not None:
            for k1 in m.get('StreamCountDetail'):
                temp_model = main_models.DescribeLiveStreamCountResponseBodyStreamCountInfosStreamCountInfoStreamCountDetailsStreamCountDetail()
                self.stream_count_detail.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamCountResponseBodyStreamCountInfosStreamCountInfoStreamCountDetailsStreamCountDetail(DaraModel):
    def __init__(
        self,
        count: int = None,
        format: str = None,
        video_data_rate: int = None,
    ):
        # The number of online streams.
        self.count = count
        # The video codec. Valid values:
        # 
        # *   **h264**
        # *   **h265**
        self.format = format
        # The video bitrate. This parameter is returned only for transcoded streams.
        self.video_data_rate = video_data_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.format is not None:
            result['Format'] = self.format

        if self.video_data_rate is not None:
            result['VideoDataRate'] = self.video_data_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('VideoDataRate') is not None:
            self.video_data_rate = m.get('VideoDataRate')

        return self

