# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CloudMonitoringSimpleEscalation(DaraModel):
    def __init__(
        self,
        escalations: List[main_models.CloudMonitoringSimpleEscalationEntry] = None,
        metric_name: str = None,
        period: int = None,
    ):
        # An object that defines a single escalation rule.
        self.escalations = escalations
        # The name of the metric.
        self.metric_name = metric_name
        # The evaluation period for the metric, in seconds.
        self.period = period

    def validate(self):
        if self.escalations:
            for v1 in self.escalations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['escalations'] = []
        if self.escalations is not None:
            for k1 in self.escalations:
                result['escalations'].append(k1.to_map() if k1 else None)

        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.period is not None:
            result['period'] = self.period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.escalations = []
        if m.get('escalations') is not None:
            for k1 in m.get('escalations'):
                temp_model = main_models.CloudMonitoringSimpleEscalationEntry()
                self.escalations.append(temp_model.from_map(k1))

        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('period') is not None:
            self.period = m.get('period')

        return self

