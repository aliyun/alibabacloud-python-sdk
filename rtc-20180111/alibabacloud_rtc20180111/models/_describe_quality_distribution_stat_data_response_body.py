# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeQualityDistributionStatDataResponseBody(DaraModel):
    def __init__(
        self,
        quality_stat_data_list: List[main_models.DescribeQualityDistributionStatDataResponseBodyQualityStatDataList] = None,
        request_id: str = None,
    ):
        self.quality_stat_data_list = quality_stat_data_list
        self.request_id = request_id

    def validate(self):
        if self.quality_stat_data_list:
            for v1 in self.quality_stat_data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['QualityStatDataList'] = []
        if self.quality_stat_data_list is not None:
            for k1 in self.quality_stat_data_list:
                result['QualityStatDataList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quality_stat_data_list = []
        if m.get('QualityStatDataList') is not None:
            for k1 in m.get('QualityStatDataList'):
                temp_model = main_models.DescribeQualityDistributionStatDataResponseBodyQualityStatDataList()
                self.quality_stat_data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeQualityDistributionStatDataResponseBodyQualityStatDataList(DaraModel):
    def __init__(
        self,
        audio_delay: int = None,
        audio_high_quality_transmission_rate: str = None,
        audio_stuck_rate: str = None,
        call_duration_ratio: str = None,
        join_channel_suc_five_sec_rate: str = None,
        join_channel_suc_rate: str = None,
        name: str = None,
        video_delay: int = None,
        video_first_pic_duration: int = None,
        video_high_quality_transmission_rate: str = None,
        video_stuck_rate: str = None,
    ):
        self.audio_delay = audio_delay
        self.audio_high_quality_transmission_rate = audio_high_quality_transmission_rate
        self.audio_stuck_rate = audio_stuck_rate
        self.call_duration_ratio = call_duration_ratio
        self.join_channel_suc_five_sec_rate = join_channel_suc_five_sec_rate
        self.join_channel_suc_rate = join_channel_suc_rate
        self.name = name
        self.video_delay = video_delay
        self.video_first_pic_duration = video_first_pic_duration
        self.video_high_quality_transmission_rate = video_high_quality_transmission_rate
        self.video_stuck_rate = video_stuck_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_delay is not None:
            result['AudioDelay'] = self.audio_delay

        if self.audio_high_quality_transmission_rate is not None:
            result['AudioHighQualityTransmissionRate'] = self.audio_high_quality_transmission_rate

        if self.audio_stuck_rate is not None:
            result['AudioStuckRate'] = self.audio_stuck_rate

        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio

        if self.join_channel_suc_five_sec_rate is not None:
            result['JoinChannelSucFiveSecRate'] = self.join_channel_suc_five_sec_rate

        if self.join_channel_suc_rate is not None:
            result['JoinChannelSucRate'] = self.join_channel_suc_rate

        if self.name is not None:
            result['Name'] = self.name

        if self.video_delay is not None:
            result['VideoDelay'] = self.video_delay

        if self.video_first_pic_duration is not None:
            result['VideoFirstPicDuration'] = self.video_first_pic_duration

        if self.video_high_quality_transmission_rate is not None:
            result['VideoHighQualityTransmissionRate'] = self.video_high_quality_transmission_rate

        if self.video_stuck_rate is not None:
            result['VideoStuckRate'] = self.video_stuck_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioDelay') is not None:
            self.audio_delay = m.get('AudioDelay')

        if m.get('AudioHighQualityTransmissionRate') is not None:
            self.audio_high_quality_transmission_rate = m.get('AudioHighQualityTransmissionRate')

        if m.get('AudioStuckRate') is not None:
            self.audio_stuck_rate = m.get('AudioStuckRate')

        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')

        if m.get('JoinChannelSucFiveSecRate') is not None:
            self.join_channel_suc_five_sec_rate = m.get('JoinChannelSucFiveSecRate')

        if m.get('JoinChannelSucRate') is not None:
            self.join_channel_suc_rate = m.get('JoinChannelSucRate')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VideoDelay') is not None:
            self.video_delay = m.get('VideoDelay')

        if m.get('VideoFirstPicDuration') is not None:
            self.video_first_pic_duration = m.get('VideoFirstPicDuration')

        if m.get('VideoHighQualityTransmissionRate') is not None:
            self.video_high_quality_transmission_rate = m.get('VideoHighQualityTransmissionRate')

        if m.get('VideoStuckRate') is not None:
            self.video_stuck_rate = m.get('VideoStuckRate')

        return self

