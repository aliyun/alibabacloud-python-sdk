# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MonitorNotifyAlertPageResult(DaraModel):
    def __init__(
        self,
        int_total: int = None,
        notify_alerts: List[main_models.MonitorNotifyAlert] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.int_total = int_total
        self.notify_alerts = notify_alerts
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.notify_alerts:
            for v1 in self.notify_alerts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.int_total is not None:
            result['intTotal'] = self.int_total

        result['notifyAlerts'] = []
        if self.notify_alerts is not None:
            for k1 in self.notify_alerts:
                result['notifyAlerts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('intTotal') is not None:
            self.int_total = m.get('intTotal')

        self.notify_alerts = []
        if m.get('notifyAlerts') is not None:
            for k1 in m.get('notifyAlerts'):
                temp_model = main_models.MonitorNotifyAlert()
                self.notify_alerts.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

