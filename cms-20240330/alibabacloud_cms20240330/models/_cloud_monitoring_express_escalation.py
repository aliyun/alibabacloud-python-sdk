# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudMonitoringExpressEscalation(DaraModel):
    def __init__(
        self,
        raw_expression: str = None,
        severity: str = None,
        times: int = None,
    ):
        # The expression that defines the alert condition.
        self.raw_expression = raw_expression
        # The alert severity that triggers the escalation.
        self.severity = severity
        # The number of alert occurrences required to trigger the escalation.
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.raw_expression is not None:
            result['rawExpression'] = self.raw_expression

        if self.severity is not None:
            result['severity'] = self.severity

        if self.times is not None:
            result['times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rawExpression') is not None:
            self.raw_expression = m.get('rawExpression')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('times') is not None:
            self.times = m.get('times')

        return self

