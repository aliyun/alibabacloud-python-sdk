# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamsTotalCountResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stream_count_list: main_models.DescribeLiveStreamsTotalCountResponseBodyStreamCountList = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The statistics about the live streams.
        self.stream_count_list = stream_count_list

    def validate(self):
        if self.stream_count_list:
            self.stream_count_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stream_count_list is not None:
            result['StreamCountList'] = self.stream_count_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamCountList') is not None:
            temp_model = main_models.DescribeLiveStreamsTotalCountResponseBodyStreamCountList()
            self.stream_count_list = temp_model.from_map(m.get('StreamCountList'))

        return self

class DescribeLiveStreamsTotalCountResponseBodyStreamCountList(DaraModel):
    def __init__(
        self,
        stream_count_infos: List[main_models.DescribeLiveStreamsTotalCountResponseBodyStreamCountListStreamCountInfos] = None,
    ):
        self.stream_count_infos = stream_count_infos

    def validate(self):
        if self.stream_count_infos:
            for v1 in self.stream_count_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StreamCountInfos'] = []
        if self.stream_count_infos is not None:
            for k1 in self.stream_count_infos:
                result['StreamCountInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stream_count_infos = []
        if m.get('StreamCountInfos') is not None:
            for k1 in m.get('StreamCountInfos'):
                temp_model = main_models.DescribeLiveStreamsTotalCountResponseBodyStreamCountListStreamCountInfos()
                self.stream_count_infos.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamsTotalCountResponseBodyStreamCountListStreamCountInfos(DaraModel):
    def __init__(
        self,
        count: int = None,
        timestamp: str = None,
    ):
        # The total number of live streams.
        self.count = count
        # The timestamp.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

