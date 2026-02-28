# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeRtcPeakChannelCntDataResponseBody(DaraModel):
    def __init__(
        self,
        peak_channel_cnt_data_per_interval: main_models.DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerInterval = None,
        request_id: str = None,
    ):
        self.peak_channel_cnt_data_per_interval = peak_channel_cnt_data_per_interval
        self.request_id = request_id

    def validate(self):
        if self.peak_channel_cnt_data_per_interval:
            self.peak_channel_cnt_data_per_interval.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.peak_channel_cnt_data_per_interval is not None:
            result['PeakChannelCntDataPerInterval'] = self.peak_channel_cnt_data_per_interval.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeakChannelCntDataPerInterval') is not None:
            temp_model = main_models.DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerInterval()
            self.peak_channel_cnt_data_per_interval = temp_model.from_map(m.get('PeakChannelCntDataPerInterval'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerInterval(DaraModel):
    def __init__(
        self,
        peak_channel_cnt_module: List[main_models.DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerIntervalPeakChannelCntModule] = None,
    ):
        self.peak_channel_cnt_module = peak_channel_cnt_module

    def validate(self):
        if self.peak_channel_cnt_module:
            for v1 in self.peak_channel_cnt_module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PeakChannelCntModule'] = []
        if self.peak_channel_cnt_module is not None:
            for k1 in self.peak_channel_cnt_module:
                result['PeakChannelCntModule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.peak_channel_cnt_module = []
        if m.get('PeakChannelCntModule') is not None:
            for k1 in m.get('PeakChannelCntModule'):
                temp_model = main_models.DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerIntervalPeakChannelCntModule()
                self.peak_channel_cnt_module.append(temp_model.from_map(k1))

        return self

class DescribeRtcPeakChannelCntDataResponseBodyPeakChannelCntDataPerIntervalPeakChannelCntModule(DaraModel):
    def __init__(
        self,
        active_channel_peak: int = None,
        active_channel_peak_time: str = None,
        time_stamp: str = None,
    ):
        self.active_channel_peak = active_channel_peak
        self.active_channel_peak_time = active_channel_peak_time
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_channel_peak is not None:
            result['ActiveChannelPeak'] = self.active_channel_peak

        if self.active_channel_peak_time is not None:
            result['ActiveChannelPeakTime'] = self.active_channel_peak_time

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveChannelPeak') is not None:
            self.active_channel_peak = m.get('ActiveChannelPeak')

        if m.get('ActiveChannelPeakTime') is not None:
            self.active_channel_peak_time = m.get('ActiveChannelPeakTime')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

