# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class AdviseSummary(DaraModel):
    def __init__(
        self,
        memory_utilization_rate: main_models.DoubleMetric = None,
        vcore_utilization_rate: main_models.DoubleMetric = None,
    ):
        self.memory_utilization_rate = memory_utilization_rate
        self.vcore_utilization_rate = vcore_utilization_rate

    def validate(self):
        if self.memory_utilization_rate:
            self.memory_utilization_rate.validate()
        if self.vcore_utilization_rate:
            self.vcore_utilization_rate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.memory_utilization_rate is not None:
            result['MemoryUtilizationRate'] = self.memory_utilization_rate.to_map()

        if self.vcore_utilization_rate is not None:
            result['VcoreUtilizationRate'] = self.vcore_utilization_rate.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemoryUtilizationRate') is not None:
            temp_model = main_models.DoubleMetric()
            self.memory_utilization_rate = temp_model.from_map(m.get('MemoryUtilizationRate'))

        if m.get('VcoreUtilizationRate') is not None:
            temp_model = main_models.DoubleMetric()
            self.vcore_utilization_rate = temp_model.from_map(m.get('VcoreUtilizationRate'))

        return self

