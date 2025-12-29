# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListMetricsOutput(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        metrics: Dict[str, List[main_models.MetricInfo]] = None,
    ):
        self.request_id = request_id
        self.metrics = metrics

    def validate(self):
        if self.metrics:
            for v1 in self.metrics.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['metrics'] = {}
        if self.metrics is not None:
            for k1, v1 in self.metrics.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['metrics'][k1] = l1

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.metrics = {}
        if m.get('metrics') is not None:
            for k1, v1 in m.get('metrics').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.MetricInfo()
                    l1.append(temp_model.from_map(k2))
                self.metrics[k1] = l1

        return self

