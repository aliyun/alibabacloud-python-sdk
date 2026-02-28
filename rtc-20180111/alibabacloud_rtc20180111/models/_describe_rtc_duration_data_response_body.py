# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeRtcDurationDataResponseBody(DaraModel):
    def __init__(
        self,
        duration_data_per_interval: main_models.DescribeRtcDurationDataResponseBodyDurationDataPerInterval = None,
        request_id: str = None,
    ):
        self.duration_data_per_interval = duration_data_per_interval
        self.request_id = request_id

    def validate(self):
        if self.duration_data_per_interval:
            self.duration_data_per_interval.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration_data_per_interval is not None:
            result['DurationDataPerInterval'] = self.duration_data_per_interval.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationDataPerInterval') is not None:
            temp_model = main_models.DescribeRtcDurationDataResponseBodyDurationDataPerInterval()
            self.duration_data_per_interval = temp_model.from_map(m.get('DurationDataPerInterval'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRtcDurationDataResponseBodyDurationDataPerInterval(DaraModel):
    def __init__(
        self,
        duration_module: List[main_models.DescribeRtcDurationDataResponseBodyDurationDataPerIntervalDurationModule] = None,
    ):
        self.duration_module = duration_module

    def validate(self):
        if self.duration_module:
            for v1 in self.duration_module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DurationModule'] = []
        if self.duration_module is not None:
            for k1 in self.duration_module:
                result['DurationModule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.duration_module = []
        if m.get('DurationModule') is not None:
            for k1 in m.get('DurationModule'):
                temp_model = main_models.DescribeRtcDurationDataResponseBodyDurationDataPerIntervalDurationModule()
                self.duration_module.append(temp_model.from_map(k1))

        return self

class DescribeRtcDurationDataResponseBodyDurationDataPerIntervalDurationModule(DaraModel):
    def __init__(
        self,
        audio_duration: int = None,
        content_duration: int = None,
        time_stamp: str = None,
        total_duration: int = None,
        v_1080duration: int = None,
        v_360duration: int = None,
        v_720duration: int = None,
    ):
        self.audio_duration = audio_duration
        self.content_duration = content_duration
        self.time_stamp = time_stamp
        self.total_duration = total_duration
        self.v_1080duration = v_1080duration
        self.v_360duration = v_360duration
        self.v_720duration = v_720duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_duration is not None:
            result['AudioDuration'] = self.audio_duration

        if self.content_duration is not None:
            result['ContentDuration'] = self.content_duration

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration

        if self.v_1080duration is not None:
            result['V1080Duration'] = self.v_1080duration

        if self.v_360duration is not None:
            result['V360Duration'] = self.v_360duration

        if self.v_720duration is not None:
            result['V720Duration'] = self.v_720duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioDuration') is not None:
            self.audio_duration = m.get('AudioDuration')

        if m.get('ContentDuration') is not None:
            self.content_duration = m.get('ContentDuration')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')

        if m.get('V1080Duration') is not None:
            self.v_1080duration = m.get('V1080Duration')

        if m.get('V360Duration') is not None:
            self.v_360duration = m.get('V360Duration')

        if m.get('V720Duration') is not None:
            self.v_720duration = m.get('V720Duration')

        return self

