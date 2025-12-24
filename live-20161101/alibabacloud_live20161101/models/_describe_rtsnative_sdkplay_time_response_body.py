# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeRTSNativeSDKPlayTimeResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        end_time: str = None,
        play_time_data: List[main_models.DescribeRTSNativeSDKPlayTimeResponseBodyPlayTimeData] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The time granularity.
        self.data_interval = data_interval
        # The end of the time range for which the data was queried.
        self.end_time = end_time
        # The average playback duration and average stuttering duration at each interval. Unit: milliseconds.
        self.play_time_data = play_time_data
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range for which the data was queried.
        self.start_time = start_time

    def validate(self):
        if self.play_time_data:
            for v1 in self.play_time_data:
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

        result['PlayTimeData'] = []
        if self.play_time_data is not None:
            for k1 in self.play_time_data:
                result['PlayTimeData'].append(k1.to_map() if k1 else None)

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

        self.play_time_data = []
        if m.get('PlayTimeData') is not None:
            for k1 in m.get('PlayTimeData'):
                temp_model = main_models.DescribeRTSNativeSDKPlayTimeResponseBodyPlayTimeData()
                self.play_time_data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeRTSNativeSDKPlayTimeResponseBodyPlayTimeData(DaraModel):
    def __init__(
        self,
        play_time: str = None,
        stall_time: str = None,
        time_stamp: str = None,
    ):
        # The average playback duration within the period of time.
        self.play_time = play_time
        # The average stuttering duration within the period of time.
        self.stall_time = stall_time
        # The timestamp of the returned data.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.play_time is not None:
            result['PlayTime'] = self.play_time

        if self.stall_time is not None:
            result['StallTime'] = self.stall_time

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlayTime') is not None:
            self.play_time = m.get('PlayTime')

        if m.get('StallTime') is not None:
            self.stall_time = m.get('StallTime')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

