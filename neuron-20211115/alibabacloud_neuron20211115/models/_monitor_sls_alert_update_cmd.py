# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MonitorSlsAlertUpdateCmd(DaraModel):
    def __init__(
        self,
        condition: str = None,
        id: int = None,
        monitor_notify_strategy: main_models.MonitorNotifyStrategy = None,
        monitor_sls_alert_rules: List[main_models.MonitorSlsAlertRule] = None,
    ):
        self.condition = condition
        # This parameter is required.
        self.id = id
        self.monitor_notify_strategy = monitor_notify_strategy
        self.monitor_sls_alert_rules = monitor_sls_alert_rules

    def validate(self):
        if self.monitor_notify_strategy:
            self.monitor_notify_strategy.validate()
        if self.monitor_sls_alert_rules:
            for v1 in self.monitor_sls_alert_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['condition'] = self.condition

        if self.id is not None:
            result['id'] = self.id

        if self.monitor_notify_strategy is not None:
            result['monitorNotifyStrategy'] = self.monitor_notify_strategy.to_map()

        result['monitorSlsAlertRules'] = []
        if self.monitor_sls_alert_rules is not None:
            for k1 in self.monitor_sls_alert_rules:
                result['monitorSlsAlertRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('monitorNotifyStrategy') is not None:
            temp_model = main_models.MonitorNotifyStrategy()
            self.monitor_notify_strategy = temp_model.from_map(m.get('monitorNotifyStrategy'))

        self.monitor_sls_alert_rules = []
        if m.get('monitorSlsAlertRules') is not None:
            for k1 in m.get('monitorSlsAlertRules'):
                temp_model = main_models.MonitorSlsAlertRule()
                self.monitor_sls_alert_rules.append(temp_model.from_map(k1))

        return self

