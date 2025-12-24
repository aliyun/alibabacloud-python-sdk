# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeRTSNativeSDKFirstFrameCostResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        end_time: str = None,
        first_frame_cost_data: List[main_models.DescribeRTSNativeSDKFirstFrameCostResponseBodyFirstFrameCostData] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The time granularity.
        self.data_interval = data_interval
        # The end of the time range for which the data was queried.
        self.end_time = end_time
        # The average latency of first frames at each interval. Unit: milliseconds.
        self.first_frame_cost_data = first_frame_cost_data
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range for which the data was queried.
        self.start_time = start_time

    def validate(self):
        if self.first_frame_cost_data:
            for v1 in self.first_frame_cost_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['FirstFrameCostData'] = []
        if self.first_frame_cost_data is not None:
            for k1 in self.first_frame_cost_data:
                result['FirstFrameCostData'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.first_frame_cost_data = []
        if m.get('FirstFrameCostData') is not None:
            for k1 in m.get('FirstFrameCostData'):
                temp_model = main_models.DescribeRTSNativeSDKFirstFrameCostResponseBodyFirstFrameCostData()
                self.first_frame_cost_data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeRTSNativeSDKFirstFrameCostResponseBodyFirstFrameCostData(DaraModel):
    def __init__(
        self,
        connected: str = None,
        finish_get_stream_info: str = None,
        first_frame_complete: str = None,
        first_packet: str = None,
        initialized: str = None,
        time_stamp: str = None,
    ):
        # The time elapsed from initialization to connection establishment.
        self.connected = connected
        # The time elapsed from connection establishment to subscription.
        self.finish_get_stream_info = finish_get_stream_info
        # The time elapsed from first packet processing to display of the first frame.
        self.first_frame_complete = first_frame_complete
        # The time elapsed from subscription to first packet processing.
        self.first_packet = first_packet
        # The time consumed by initialization.
        self.initialized = initialized
        # The timestamp of the returned data.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connected is not None:
            result['Connected'] = self.connected

        if self.finish_get_stream_info is not None:
            result['FinishGetStreamInfo'] = self.finish_get_stream_info

        if self.first_frame_complete is not None:
            result['FirstFrameComplete'] = self.first_frame_complete

        if self.first_packet is not None:
            result['FirstPacket'] = self.first_packet

        if self.initialized is not None:
            result['Initialized'] = self.initialized

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Connected') is not None:
            self.connected = m.get('Connected')

        if m.get('FinishGetStreamInfo') is not None:
            self.finish_get_stream_info = m.get('FinishGetStreamInfo')

        if m.get('FirstFrameComplete') is not None:
            self.first_frame_complete = m.get('FirstFrameComplete')

        if m.get('FirstPacket') is not None:
            self.first_packet = m.get('FirstPacket')

        if m.get('Initialized') is not None:
            self.initialized = m.get('Initialized')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

