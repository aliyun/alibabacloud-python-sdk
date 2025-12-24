# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamHistoryUserNumResponseBody(DaraModel):
    def __init__(
        self,
        live_stream_user_num_infos: main_models.DescribeLiveStreamHistoryUserNumResponseBodyLiveStreamUserNumInfos = None,
        request_id: str = None,
    ):
        # The number of historical online users for the live stream.
        self.live_stream_user_num_infos = live_stream_user_num_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_stream_user_num_infos:
            self.live_stream_user_num_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_stream_user_num_infos is not None:
            result['LiveStreamUserNumInfos'] = self.live_stream_user_num_infos.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveStreamUserNumInfos') is not None:
            temp_model = main_models.DescribeLiveStreamHistoryUserNumResponseBodyLiveStreamUserNumInfos()
            self.live_stream_user_num_infos = temp_model.from_map(m.get('LiveStreamUserNumInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveStreamHistoryUserNumResponseBodyLiveStreamUserNumInfos(DaraModel):
    def __init__(
        self,
        live_stream_user_num_info: List[main_models.DescribeLiveStreamHistoryUserNumResponseBodyLiveStreamUserNumInfosLiveStreamUserNumInfo] = None,
    ):
        self.live_stream_user_num_info = live_stream_user_num_info

    def validate(self):
        if self.live_stream_user_num_info:
            for v1 in self.live_stream_user_num_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveStreamUserNumInfo'] = []
        if self.live_stream_user_num_info is not None:
            for k1 in self.live_stream_user_num_info:
                result['LiveStreamUserNumInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_stream_user_num_info = []
        if m.get('LiveStreamUserNumInfo') is not None:
            for k1 in m.get('LiveStreamUserNumInfo'):
                temp_model = main_models.DescribeLiveStreamHistoryUserNumResponseBodyLiveStreamUserNumInfosLiveStreamUserNumInfo()
                self.live_stream_user_num_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamHistoryUserNumResponseBodyLiveStreamUserNumInfosLiveStreamUserNumInfo(DaraModel):
    def __init__(
        self,
        stream_time: str = None,
        user_num: str = None,
    ):
        # The time when the stream started. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.stream_time = stream_time
        # The number of users at the current point in time.
        self.user_num = user_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stream_time is not None:
            result['StreamTime'] = self.stream_time

        if self.user_num is not None:
            result['UserNum'] = self.user_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StreamTime') is not None:
            self.stream_time = m.get('StreamTime')

        if m.get('UserNum') is not None:
            self.user_num = m.get('UserNum')

        return self

