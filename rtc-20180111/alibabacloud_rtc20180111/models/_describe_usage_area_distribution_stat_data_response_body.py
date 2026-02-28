# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeUsageAreaDistributionStatDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        usage_area_stat_list: List[main_models.DescribeUsageAreaDistributionStatDataResponseBodyUsageAreaStatList] = None,
    ):
        self.request_id = request_id
        self.usage_area_stat_list = usage_area_stat_list

    def validate(self):
        if self.usage_area_stat_list:
            for v1 in self.usage_area_stat_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UsageAreaStatList'] = []
        if self.usage_area_stat_list is not None:
            for k1 in self.usage_area_stat_list:
                result['UsageAreaStatList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.usage_area_stat_list = []
        if m.get('UsageAreaStatList') is not None:
            for k1 in m.get('UsageAreaStatList'):
                temp_model = main_models.DescribeUsageAreaDistributionStatDataResponseBodyUsageAreaStatList()
                self.usage_area_stat_list.append(temp_model.from_map(k1))

        return self

class DescribeUsageAreaDistributionStatDataResponseBodyUsageAreaStatList(DaraModel):
    def __init__(
        self,
        audio_call_duration: int = None,
        name: str = None,
        total_call_duration: int = None,
        video_call_duration: int = None,
    ):
        self.audio_call_duration = audio_call_duration
        self.name = name
        self.total_call_duration = total_call_duration
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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TotalCallDuration') is not None:
            self.total_call_duration = m.get('TotalCallDuration')

        if m.get('VideoCallDuration') is not None:
            self.video_call_duration = m.get('VideoCallDuration')

        return self

