# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class NotifyConfigUnified(DaraModel):
    def __init__(
        self,
        active_days: List[int] = None,
        active_end_time: str = None,
        active_start_time: str = None,
        channels: List[main_models.DirectNotifyChannel] = None,
        silence_time_secs: int = None,
        type: str = None,
        utc_offset: str = None,
    ):
        # The active days of the week.
        self.active_days = active_days
        # The end of the daily active time window. On active days, the system sends notifications only before this time. Format: `HH:mm`.
        self.active_end_time = active_end_time
        # The start of the daily active time window. On active days, the system sends notifications only after this time. Format: `HH:mm`.
        self.active_start_time = active_start_time
        # The notification channels that receive alerts.
        # 
        # This parameter is required.
        self.channels = channels
        # The silence time in seconds. After sending a notification, the system suppresses new notifications for the same alert for this duration.
        self.silence_time_secs = silence_time_secs
        # The type of the notification configuration.
        # 
        # This parameter is required.
        self.type = type
        # The UTC offset for `activeStartTime` and `activeEndTime`. The format is `[+/-]HH:mm`. For example, `+08:00` represents the UTC+8 time zone.
        self.utc_offset = utc_offset

    def validate(self):
        if self.channels:
            for v1 in self.channels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_days is not None:
            result['activeDays'] = self.active_days

        if self.active_end_time is not None:
            result['activeEndTime'] = self.active_end_time

        if self.active_start_time is not None:
            result['activeStartTime'] = self.active_start_time

        result['channels'] = []
        if self.channels is not None:
            for k1 in self.channels:
                result['channels'].append(k1.to_map() if k1 else None)

        if self.silence_time_secs is not None:
            result['silenceTimeSecs'] = self.silence_time_secs

        if self.type is not None:
            result['type'] = self.type

        if self.utc_offset is not None:
            result['utcOffset'] = self.utc_offset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeDays') is not None:
            self.active_days = m.get('activeDays')

        if m.get('activeEndTime') is not None:
            self.active_end_time = m.get('activeEndTime')

        if m.get('activeStartTime') is not None:
            self.active_start_time = m.get('activeStartTime')

        self.channels = []
        if m.get('channels') is not None:
            for k1 in m.get('channels'):
                temp_model = main_models.DirectNotifyChannel()
                self.channels.append(temp_model.from_map(k1))

        if m.get('silenceTimeSecs') is not None:
            self.silence_time_secs = m.get('silenceTimeSecs')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('utcOffset') is not None:
            self.utc_offset = m.get('utcOffset')

        return self

