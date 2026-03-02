# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MonitorArmsAlertUpdateCmd(DaraModel):
    def __init__(
        self,
        condition: str = None,
        id: int = None,
        monitor_arms_alert_rules: List[main_models.MonitorArmsAlertRule] = None,
        monitor_notify_strategy: main_models.MonitorNotifyStrategy = None,
    ):
        self.condition = condition
        # This parameter is required.
        self.id = id
        self.monitor_arms_alert_rules = monitor_arms_alert_rules
        self.monitor_notify_strategy = monitor_notify_strategy

    def validate(self):
        if self.monitor_arms_alert_rules:
            for v1 in self.monitor_arms_alert_rules:
                 if v1:
                    v1.validate()
        if self.monitor_notify_strategy:
            self.monitor_notify_strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['condition'] = self.condition

        if self.id is not None:
            result['id'] = self.id

        result['monitorArmsAlertRules'] = []
        if self.monitor_arms_alert_rules is not None:
            for k1 in self.monitor_arms_alert_rules:
                result['monitorArmsAlertRules'].append(k1.to_map() if k1 else None)

        if self.monitor_notify_strategy is not None:
            result['monitorNotifyStrategy'] = self.monitor_notify_strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('id') is not None:
            self.id = m.get('id')

        self.monitor_arms_alert_rules = []
        if m.get('monitorArmsAlertRules') is not None:
            for k1 in m.get('monitorArmsAlertRules'):
                temp_model = main_models.MonitorArmsAlertRule()
                self.monitor_arms_alert_rules.append(temp_model.from_map(k1))

        if m.get('monitorNotifyStrategy') is not None:
            temp_model = main_models.MonitorNotifyStrategy()
            self.monitor_notify_strategy = temp_model.from_map(m.get('monitorNotifyStrategy'))

        return self

