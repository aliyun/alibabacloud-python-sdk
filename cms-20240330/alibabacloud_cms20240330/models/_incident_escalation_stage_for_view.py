# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentEscalationStageForView(DaraModel):
    def __init__(
        self,
        cycle_notify_count: int = None,
        cycle_notify_interval: int = None,
        effect_time_range: main_models.EffectTimeRange = None,
        index: int = None,
        notify_channels: List[main_models.NotifyChannel] = None,
        target_incident_state: str = None,
        trigger_delay: int = None,
    ):
        self.cycle_notify_count = cycle_notify_count
        self.cycle_notify_interval = cycle_notify_interval
        self.effect_time_range = effect_time_range
        # This parameter is required.
        self.index = index
        self.notify_channels = notify_channels
        self.target_incident_state = target_incident_state
        self.trigger_delay = trigger_delay

    def validate(self):
        if self.effect_time_range:
            self.effect_time_range.validate()
        if self.notify_channels:
            for v1 in self.notify_channels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_notify_count is not None:
            result['cycleNotifyCount'] = self.cycle_notify_count

        if self.cycle_notify_interval is not None:
            result['cycleNotifyInterval'] = self.cycle_notify_interval

        if self.effect_time_range is not None:
            result['effectTimeRange'] = self.effect_time_range.to_map()

        if self.index is not None:
            result['index'] = self.index

        result['notifyChannels'] = []
        if self.notify_channels is not None:
            for k1 in self.notify_channels:
                result['notifyChannels'].append(k1.to_map() if k1 else None)

        if self.target_incident_state is not None:
            result['targetIncidentState'] = self.target_incident_state

        if self.trigger_delay is not None:
            result['triggerDelay'] = self.trigger_delay

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cycleNotifyCount') is not None:
            self.cycle_notify_count = m.get('cycleNotifyCount')

        if m.get('cycleNotifyInterval') is not None:
            self.cycle_notify_interval = m.get('cycleNotifyInterval')

        if m.get('effectTimeRange') is not None:
            temp_model = main_models.EffectTimeRange()
            self.effect_time_range = temp_model.from_map(m.get('effectTimeRange'))

        if m.get('index') is not None:
            self.index = m.get('index')

        self.notify_channels = []
        if m.get('notifyChannels') is not None:
            for k1 in m.get('notifyChannels'):
                temp_model = main_models.NotifyChannel()
                self.notify_channels.append(temp_model.from_map(k1))

        if m.get('targetIncidentState') is not None:
            self.target_incident_state = m.get('targetIncidentState')

        if m.get('triggerDelay') is not None:
            self.trigger_delay = m.get('triggerDelay')

        return self

