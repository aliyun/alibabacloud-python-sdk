# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeUsageDistributionStatDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        usage_stat_list: List[main_models.DescribeUsageDistributionStatDataResponseBodyUsageStatList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of usage statistics.
        self.usage_stat_list = usage_stat_list

    def validate(self):
        if self.usage_stat_list:
            for v1 in self.usage_stat_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UsageStatList'] = []
        if self.usage_stat_list is not None:
            for k1 in self.usage_stat_list:
                result['UsageStatList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.usage_stat_list = []
        if m.get('UsageStatList') is not None:
            for k1 in m.get('UsageStatList'):
                temp_model = main_models.DescribeUsageDistributionStatDataResponseBodyUsageStatList()
                self.usage_stat_list.append(temp_model.from_map(k1))

        return self

class DescribeUsageDistributionStatDataResponseBodyUsageStatList(DaraModel):
    def __init__(
        self,
        audio_call_duration: int = None,
        call_duration_ratio: str = None,
        name: str = None,
        total_call_duration: int = None,
        video_call_duration: int = None,
    ):
        # The duration of audio calls, in minutes.
        self.audio_call_duration = audio_call_duration
        # The ratio of the call duration, represented by four decimal places, such as 0.9782.
        self.call_duration_ratio = call_duration_ratio
        # The statistical dimension. Valid values:
        # - When StatDim is set to CHANNEL_ONLINE, valid values are **ONE_TO_FIVE** (1 to 5 users), **SIX_TO_TEN** (6 to 10 users), **ELEVEN_TO_TWENTY** (11 to 20 users), **TWENTY_ONE_TO_FIFTY** (21 to 50 users), and **ABOVE_FIFTY** (more than 50 users).  
        # - When StatDim is set to NETWORK, valid values are **WiFi**, **4G**, and others.  
        # - When StatDim is set to OS, valid values are **iOS**, **Android**, and others.
        self.name = name
        # The total duration of calls, in minutes.
        self.total_call_duration = total_call_duration
        # The duration of video calls, in minutes.
        self.video_call_duration = video_call_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_call_duration is not None:
            result['AudioCallDuration'] = self.audio_call_duration

        if self.call_duration_ratio is not None:
            result['CallDurationRatio'] = self.call_duration_ratio

        if self.name is not None:
            result['Name'] = self.name

        if self.total_call_duration is not None:
            result['TotalCallDuration'] = self.total_call_duration

        if self.video_call_duration is not None:
            result['VideoCallDuration'] = self.video_call_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioCallDuration') is not None:
            self.audio_call_duration = m.get('AudioCallDuration')

        if m.get('CallDurationRatio') is not None:
            self.call_duration_ratio = m.get('CallDurationRatio')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TotalCallDuration') is not None:
            self.total_call_duration = m.get('TotalCallDuration')

        if m.get('VideoCallDuration') is not None:
            self.video_call_duration = m.get('VideoCallDuration')

        return self

