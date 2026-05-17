# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class NotifyRouteForSubscription(DaraModel):
    def __init__(
        self,
        channels: List[main_models.NotifyRouteForSubscriptionChannels] = None,
        effect_time_range: main_models.NotifyRouteForSubscriptionEffectTimeRange = None,
    ):
        self.channels = channels
        self.effect_time_range = effect_time_range

    def validate(self):
        if self.channels:
            for v1 in self.channels:
                 if v1:
                    v1.validate()
        if self.effect_time_range:
            self.effect_time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['channels'] = []
        if self.channels is not None:
            for k1 in self.channels:
                result['channels'].append(k1.to_map() if k1 else None)

        if self.effect_time_range is not None:
            result['effectTimeRange'] = self.effect_time_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channels = []
        if m.get('channels') is not None:
            for k1 in m.get('channels'):
                temp_model = main_models.NotifyRouteForSubscriptionChannels()
                self.channels.append(temp_model.from_map(k1))

        if m.get('effectTimeRange') is not None:
            temp_model = main_models.NotifyRouteForSubscriptionEffectTimeRange()
            self.effect_time_range = temp_model.from_map(m.get('effectTimeRange'))

        return self

class NotifyRouteForSubscriptionEffectTimeRange(DaraModel):
    def __init__(
        self,
        day_in_week: List[int] = None,
        end_time_in_minute: int = None,
        start_time_in_minute: int = None,
        time_zone: str = None,
    ):
        self.day_in_week = day_in_week
        self.end_time_in_minute = end_time_in_minute
        self.start_time_in_minute = start_time_in_minute
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day_in_week is not None:
            result['dayInWeek'] = self.day_in_week

        if self.end_time_in_minute is not None:
            result['endTimeInMinute'] = self.end_time_in_minute

        if self.start_time_in_minute is not None:
            result['startTimeInMinute'] = self.start_time_in_minute

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayInWeek') is not None:
            self.day_in_week = m.get('dayInWeek')

        if m.get('endTimeInMinute') is not None:
            self.end_time_in_minute = m.get('endTimeInMinute')

        if m.get('startTimeInMinute') is not None:
            self.start_time_in_minute = m.get('startTimeInMinute')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

class NotifyRouteForSubscriptionChannels(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        enabled_sub_channels: List[str] = None,
        receivers: List[str] = None,
    ):
        self.channel_type = channel_type
        self.enabled_sub_channels = enabled_sub_channels
        self.receivers = receivers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['channelType'] = self.channel_type

        if self.enabled_sub_channels is not None:
            result['enabledSubChannels'] = self.enabled_sub_channels

        if self.receivers is not None:
            result['receivers'] = self.receivers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')

        if m.get('enabledSubChannels') is not None:
            self.enabled_sub_channels = m.get('enabledSubChannels')

        if m.get('receivers') is not None:
            self.receivers = m.get('receivers')

        return self

