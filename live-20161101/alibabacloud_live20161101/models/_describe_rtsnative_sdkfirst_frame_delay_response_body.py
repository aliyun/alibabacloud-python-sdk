# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeRTSNativeSDKFirstFrameDelayResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        end_time: str = None,
        frame_delay_data: List[main_models.DescribeRTSNativeSDKFirstFrameDelayResponseBodyFrameDelayData] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The time granularity.
        self.data_interval = data_interval
        # The end of the time range for which the data was queried.
        self.end_time = end_time
        # The average latency of first frames at each interval. Unit: milliseconds.
        self.frame_delay_data = frame_delay_data
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range for which the data was queried.
        self.start_time = start_time

    def validate(self):
        if self.frame_delay_data:
            for v1 in self.frame_delay_data:
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

        result['FrameDelayData'] = []
        if self.frame_delay_data is not None:
            for k1 in self.frame_delay_data:
                result['FrameDelayData'].append(k1.to_map() if k1 else None)

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

        self.frame_delay_data = []
        if m.get('FrameDelayData') is not None:
            for k1 in m.get('FrameDelayData'):
                temp_model = main_models.DescribeRTSNativeSDKFirstFrameDelayResponseBodyFrameDelayData()
                self.frame_delay_data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeRTSNativeSDKFirstFrameDelayResponseBodyFrameDelayData(DaraModel):
    def __init__(
        self,
        frame_delay: str = None,
        time_stamp: str = None,
    ):
        # The average latency of first frames within the period of time.
        self.frame_delay = frame_delay
        # The timestamp of the returned data.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frame_delay is not None:
            result['FrameDelay'] = self.frame_delay

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameDelay') is not None:
            self.frame_delay = m.get('FrameDelay')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

