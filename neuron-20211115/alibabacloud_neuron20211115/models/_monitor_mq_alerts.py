# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MonitorMqAlerts(DaraModel):
    def __init__(
        self,
        monitor_mq_alerts: List[main_models.MonitorMqAlert] = None,
    ):
        self.monitor_mq_alerts = monitor_mq_alerts

    def validate(self):
        if self.monitor_mq_alerts:
            for v1 in self.monitor_mq_alerts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['monitorMqAlerts'] = []
        if self.monitor_mq_alerts is not None:
            for k1 in self.monitor_mq_alerts:
                result['monitorMqAlerts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_mq_alerts = []
        if m.get('monitorMqAlerts') is not None:
            for k1 in m.get('monitorMqAlerts'):
                temp_model = main_models.MonitorMqAlert()
                self.monitor_mq_alerts.append(temp_model.from_map(k1))

        return self

