# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ExperimentReportValue(DaraModel):
    def __init__(
        self,
        baseline: bool = None,
        metric_results: Dict[str, dict] = None,
    ):
        self.baseline = baseline
        self.metric_results = metric_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline is not None:
            result['Baseline'] = self.baseline

        if self.metric_results is not None:
            result['MetricResults'] = self.metric_results

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Baseline') is not None:
            self.baseline = m.get('Baseline')

        if m.get('MetricResults') is not None:
            self.metric_results = m.get('MetricResults')

        return self

