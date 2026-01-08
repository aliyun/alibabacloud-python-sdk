# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dsw20220101 import models as main_models
from darabonba.model import DaraModel

class GetInstanceMetricsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        pod_metrics: List[main_models.GetInstanceMetricsResponseBodyPodMetrics] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. Valid values:
        # 
        # *   InternalError: an internal error. All errors, except for parameter validation errors, are classified as internal errors.
        # *   ValidationError: a parameter validation error.
        self.code = code
        # The HTTP status code. Valid values:
        # 
        # *   400
        # *   404
        self.http_status_code = http_status_code
        # The instance ID.
        self.instance_id = instance_id
        # The response message.
        self.message = message
        # The information about the metrics of the pod that corresponds to the instance.
        self.pod_metrics = pod_metrics
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.pod_metrics:
            for v1 in self.pod_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message is not None:
            result['Message'] = self.message

        result['PodMetrics'] = []
        if self.pod_metrics is not None:
            for k1 in self.pod_metrics:
                result['PodMetrics'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.pod_metrics = []
        if m.get('PodMetrics') is not None:
            for k1 in m.get('PodMetrics'):
                temp_model = main_models.GetInstanceMetricsResponseBodyPodMetrics()
                self.pod_metrics.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInstanceMetricsResponseBodyPodMetrics(DaraModel):
    def __init__(
        self,
        metrics: List[main_models.GetInstanceMetricsResponseBodyPodMetricsMetrics] = None,
        pod_id: str = None,
    ):
        # The metrics of the pod that corresponds to the instance.
        self.metrics = metrics
        # The ID of the pod that corresponds to the instance.
        self.pod_id = pod_id

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
        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.pod_id is not None:
            result['PodId'] = self.pod_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.GetInstanceMetricsResponseBodyPodMetricsMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')

        return self

class GetInstanceMetricsResponseBodyPodMetricsMetrics(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: float = None,
    ):
        # The timestamp corresponding to the metric.
        self.time = time
        # The metric value.
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

