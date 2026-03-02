# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MonitorArmsAlerts(DaraModel):
    def __init__(
        self,
        monitor_arms_alerts: List[main_models.MonitorArmsAlert] = None,
    ):
        self.monitor_arms_alerts = monitor_arms_alerts

    def validate(self):
        if self.monitor_arms_alerts:
            for v1 in self.monitor_arms_alerts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['monitorArmsAlerts'] = []
        if self.monitor_arms_alerts is not None:
            for k1 in self.monitor_arms_alerts:
                result['monitorArmsAlerts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_arms_alerts = []
        if m.get('monitorArmsAlerts') is not None:
            for k1 in m.get('monitorArmsAlerts'):
                temp_model = main_models.MonitorArmsAlert()
                self.monitor_arms_alerts.append(temp_model.from_map(k1))

        return self

