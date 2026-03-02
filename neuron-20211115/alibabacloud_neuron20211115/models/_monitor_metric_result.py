# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MonitorMetricResult(DaraModel):
    def __init__(
        self,
        measure_data: List[main_models.MonitorMetricMeasureData] = None,
        request_id: str = None,
    ):
        self.measure_data = measure_data
        self.request_id = request_id

    def validate(self):
        if self.measure_data:
            for v1 in self.measure_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['measureData'] = []
        if self.measure_data is not None:
            for k1 in self.measure_data:
                result['measureData'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.measure_data = []
        if m.get('measureData') is not None:
            for k1 in m.get('measureData'):
                temp_model = main_models.MonitorMetricMeasureData()
                self.measure_data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

