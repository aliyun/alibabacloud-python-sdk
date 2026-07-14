# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class NotifyConfigUnified(DaraModel):
    def __init__(
        self,
        active_days: List[int] = None,
        active_end_time: str = None,
        active_start_time: str = None,
        channels: List[main_models.DirectNotifyChannel] = None,
        notify_strategies: List[str] = None,
        send_recover_notification: bool = None,
        severity_channels: Dict[str, main_models.SeverityNotifyConfig] = None,
        silence_time_secs: int = None,
        type: str = None,
        utc_offset: str = None,
    ):
        self.active_days = active_days
        self.active_end_time = active_end_time
        self.active_start_time = active_start_time
        self.channels = channels
        self.notify_strategies = notify_strategies
        self.send_recover_notification = send_recover_notification
        self.severity_channels = severity_channels
        self.silence_time_secs = silence_time_secs
        # This parameter is required.
        self.type = type
        self.utc_offset = utc_offset

    def validate(self):
        if self.channels:
            for v1 in self.channels:
                 if v1:
                    v1.validate()
        if self.severity_channels:
            for v1 in self.severity_channels.values():
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

        if self.notify_strategies is not None:
            result['notifyStrategies'] = self.notify_strategies

        if self.send_recover_notification is not None:
            result['sendRecoverNotification'] = self.send_recover_notification

        result['severityChannels'] = {}
        if self.severity_channels is not None:
            for k1, v1 in self.severity_channels.items():
                result['severityChannels'][k1] = v1.to_map() if v1 else None

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

        if m.get('notifyStrategies') is not None:
            self.notify_strategies = m.get('notifyStrategies')

        if m.get('sendRecoverNotification') is not None:
            self.send_recover_notification = m.get('sendRecoverNotification')

        self.severity_channels = {}
        if m.get('severityChannels') is not None:
            for k1, v1 in m.get('severityChannels').items():
                temp_model = main_models.SeverityNotifyConfig()
                self.severity_channels[k1] = temp_model.from_map(v1)

        if m.get('silenceTimeSecs') is not None:
            self.silence_time_secs = m.get('silenceTimeSecs')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('utcOffset') is not None:
            self.utc_offset = m.get('utcOffset')

        return self

