# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ListTrainingJobInstanceMetricsResponseBody(DaraModel):
    def __init__(
        self,
        instance_metrics: List[main_models.ListTrainingJobInstanceMetricsResponseBodyInstanceMetrics] = None,
        request_id: str = None,
    ):
        self.instance_metrics = instance_metrics
        self.request_id = request_id

    def validate(self):
        if self.instance_metrics:
            for v1 in self.instance_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceMetrics'] = []
        if self.instance_metrics is not None:
            for k1 in self.instance_metrics:
                result['InstanceMetrics'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_metrics = []
        if m.get('InstanceMetrics') is not None:
            for k1 in m.get('InstanceMetrics'):
                temp_model = main_models.ListTrainingJobInstanceMetricsResponseBodyInstanceMetrics()
                self.instance_metrics.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTrainingJobInstanceMetricsResponseBodyInstanceMetrics(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        metrics: List[main_models.ListTrainingJobInstanceMetricsResponseBodyInstanceMetricsMetrics] = None,
        node_name: str = None,
    ):
        self.instance_id = instance_id
        self.metrics = metrics
        self.node_name = node_name

    def validate(self):
        if self.metrics:
            for v1 in self.metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.ListTrainingJobInstanceMetricsResponseBodyInstanceMetricsMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        return self

class ListTrainingJobInstanceMetricsResponseBodyInstanceMetricsMetrics(DaraModel):
    def __init__(
        self,
        time: str = None,
        value: float = None,
    ):
        self.time = time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

