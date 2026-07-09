# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CloudMonitoringCompositeEscalation(DaraModel):
    def __init__(
        self,
        escalations: List[main_models.CloudMonitoringCompositeEscalationEntry] = None,
        relation: str = None,
        severity: str = None,
        times: int = None,
    ):
        # A single entry in the escalation policy. See the `CloudMonitoringCompositeEscalationEntry` object for details.
        self.escalations = escalations
        # Specifies the logical relationship for evaluating the conditions of the composite alert rule. Valid values: `and` and `or`.
        self.relation = relation
        # Specifies the severity level of the alert. For example: `Critical`, `Warning`, and `Info`.
        self.severity = severity
        # Specifies the number of times the alert conditions must be met to trigger this escalation policy.
        self.times = times

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

        if self.relation is not None:
            result['relation'] = self.relation

        if self.severity is not None:
            result['severity'] = self.severity

        if self.times is not None:
            result['times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.escalations = []
        if m.get('escalations') is not None:
            for k1 in m.get('escalations'):
                temp_model = main_models.CloudMonitoringCompositeEscalationEntry()
                self.escalations.append(temp_model.from_map(k1))

        if m.get('relation') is not None:
            self.relation = m.get('relation')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('times') is not None:
            self.times = m.get('times')

        return self

