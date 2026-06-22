# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ResourceSummary(DaraModel):
    def __init__(
        self,
        inefficient_task_rate: main_models.DoubleMetric = None,
        memory_utilization_rate: main_models.DoubleMetric = None,
        original_total_vcore: main_models.IntegerMetric = None,
        vcore_utilization_rate: main_models.DoubleMetric = None,
    ):
        self.inefficient_task_rate = inefficient_task_rate
        self.memory_utilization_rate = memory_utilization_rate
        self.original_total_vcore = original_total_vcore
        self.vcore_utilization_rate = vcore_utilization_rate

    def validate(self):
        if self.inefficient_task_rate:
            self.inefficient_task_rate.validate()
        if self.memory_utilization_rate:
            self.memory_utilization_rate.validate()
        if self.original_total_vcore:
            self.original_total_vcore.validate()
        if self.vcore_utilization_rate:
            self.vcore_utilization_rate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inefficient_task_rate is not None:
            result['InefficientTaskRate'] = self.inefficient_task_rate.to_map()

        if self.memory_utilization_rate is not None:
            result['MemoryUtilizationRate'] = self.memory_utilization_rate.to_map()

        if self.original_total_vcore is not None:
            result['OriginalTotalVcore'] = self.original_total_vcore.to_map()

        if self.vcore_utilization_rate is not None:
            result['VcoreUtilizationRate'] = self.vcore_utilization_rate.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InefficientTaskRate') is not None:
            temp_model = main_models.DoubleMetric()
            self.inefficient_task_rate = temp_model.from_map(m.get('InefficientTaskRate'))

        if m.get('MemoryUtilizationRate') is not None:
            temp_model = main_models.DoubleMetric()
            self.memory_utilization_rate = temp_model.from_map(m.get('MemoryUtilizationRate'))

        if m.get('OriginalTotalVcore') is not None:
            temp_model = main_models.IntegerMetric()
            self.original_total_vcore = temp_model.from_map(m.get('OriginalTotalVcore'))

        if m.get('VcoreUtilizationRate') is not None:
            temp_model = main_models.DoubleMetric()
            self.vcore_utilization_rate = temp_model.from_map(m.get('VcoreUtilizationRate'))

        return self

