# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamsControlHistoryResponseBody(DaraModel):
    def __init__(
        self,
        control_info: main_models.DescribeLiveStreamsControlHistoryResponseBodyControlInfo = None,
        request_id: str = None,
    ):
        # The operation records.
        self.control_info = control_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.control_info:
            self.control_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_info is not None:
            result['ControlInfo'] = self.control_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlInfo') is not None:
            temp_model = main_models.DescribeLiveStreamsControlHistoryResponseBodyControlInfo()
            self.control_info = temp_model.from_map(m.get('ControlInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveStreamsControlHistoryResponseBodyControlInfo(DaraModel):
    def __init__(
        self,
        live_stream_control_info: List[main_models.DescribeLiveStreamsControlHistoryResponseBodyControlInfoLiveStreamControlInfo] = None,
    ):
        self.live_stream_control_info = live_stream_control_info

    def validate(self):
        if self.live_stream_control_info:
            for v1 in self.live_stream_control_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveStreamControlInfo'] = []
        if self.live_stream_control_info is not None:
            for k1 in self.live_stream_control_info:
                result['LiveStreamControlInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_stream_control_info = []
        if m.get('LiveStreamControlInfo') is not None:
            for k1 in m.get('LiveStreamControlInfo'):
                temp_model = main_models.DescribeLiveStreamsControlHistoryResponseBodyControlInfoLiveStreamControlInfo()
                self.live_stream_control_info.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamsControlHistoryResponseBodyControlInfoLiveStreamControlInfo(DaraModel):
    def __init__(
        self,
        action: str = None,
        client_ip: str = None,
        stream_name: str = None,
        time_stamp: str = None,
    ):
        # The name of the operation performed.
        self.action = action
        # The IP address that is used by the client for live streaming.
        self.client_ip = client_ip
        # The name of the live stream.
        self.stream_name = stream_name
        # The time when the operation was performed. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.client_ip is not None:
            result['ClientIP'] = self.client_ip

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ClientIP') is not None:
            self.client_ip = m.get('ClientIP')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

