# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MonitorMetricMeasureData(DaraModel):
    def __init__(
        self,
        measure: str = None,
        measure_point_data: List[main_models.MonitorMetricMeasurePointData] = None,
    ):
        self.measure = measure
        self.measure_point_data = measure_point_data

    def validate(self):
        if self.measure_point_data:
            for v1 in self.measure_point_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.measure is not None:
            result['measure'] = self.measure

        result['measurePointData'] = []
        if self.measure_point_data is not None:
            for k1 in self.measure_point_data:
                result['measurePointData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('measure') is not None:
            self.measure = m.get('measure')

        self.measure_point_data = []
        if m.get('measurePointData') is not None:
            for k1 in m.get('measurePointData'):
                temp_model = main_models.MonitorMetricMeasurePointData()
                self.measure_point_data.append(temp_model.from_map(k1))

        return self

