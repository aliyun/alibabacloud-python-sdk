# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudMonitoringPrometheusEscalation(DaraModel):
    def __init__(
        self,
        prom_ql: str = None,
        severity: str = None,
        times: int = None,
    ):
        # The PromQL query statement.
        self.prom_ql = prom_ql
        # The severity level.
        self.severity = severity
        # The number of consecutive times the alert is triggered.
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prom_ql is not None:
            result['promQl'] = self.prom_ql

        if self.severity is not None:
            result['severity'] = self.severity

        if self.times is not None:
            result['times'] = self.times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('promQl') is not None:
            self.prom_ql = m.get('promQl')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('times') is not None:
            self.times = m.get('times')

        return self

