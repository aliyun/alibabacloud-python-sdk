# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DescribeServiceAutoScalerResponseBody(DaraModel):
    def __init__(
        self,
        behavior: Dict[str, Any] = None,
        current_metrics: List[main_models.DescribeServiceAutoScalerResponseBodyCurrentMetrics] = None,
        max_replica: int = None,
        min_replica: int = None,
        request_id: str = None,
        scale_strategies: List[main_models.DescribeServiceAutoScalerResponseBodyScaleStrategies] = None,
        service_name: str = None,
    ):
        # The additional information about the Autoscaler policy, such as the interval of triggering Autoscaler.
        self.behavior = behavior
        # The metrics.
        self.current_metrics = current_metrics
        # The maximum number of instances in the service.
        self.max_replica = max_replica
        # The minimum number of instances in the service.
        self.min_replica = min_replica
        # The request ID.
        self.request_id = request_id
        # The auto scaling policies.
        self.scale_strategies = scale_strategies
        # The service name.
        self.service_name = service_name

    def validate(self):
        if self.current_metrics:
            for v1 in self.current_metrics:
                 if v1:
                    v1.validate()
        if self.scale_strategies:
            for v1 in self.scale_strategies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.behavior is not None:
            result['Behavior'] = self.behavior

        result['CurrentMetrics'] = []
        if self.current_metrics is not None:
            for k1 in self.current_metrics:
                result['CurrentMetrics'].append(k1.to_map() if k1 else None)

        if self.max_replica is not None:
            result['MaxReplica'] = self.max_replica

        if self.min_replica is not None:
            result['MinReplica'] = self.min_replica

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ScaleStrategies'] = []
        if self.scale_strategies is not None:
            for k1 in self.scale_strategies:
                result['ScaleStrategies'].append(k1.to_map() if k1 else None)

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Behavior') is not None:
            self.behavior = m.get('Behavior')

        self.current_metrics = []
        if m.get('CurrentMetrics') is not None:
            for k1 in m.get('CurrentMetrics'):
                temp_model = main_models.DescribeServiceAutoScalerResponseBodyCurrentMetrics()
                self.current_metrics.append(temp_model.from_map(k1))

        if m.get('MaxReplica') is not None:
            self.max_replica = m.get('MaxReplica')

        if m.get('MinReplica') is not None:
            self.min_replica = m.get('MinReplica')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scale_strategies = []
        if m.get('ScaleStrategies') is not None:
            for k1 in m.get('ScaleStrategies'):
                temp_model = main_models.DescribeServiceAutoScalerResponseBodyScaleStrategies()
                self.scale_strategies.append(temp_model.from_map(k1))

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

class DescribeServiceAutoScalerResponseBodyScaleStrategies(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        service: str = None,
        threshold: float = None,
    ):
        # The metric name. Valid values:
        # 
        # *   QPS: the queries per second (QPS) for an individual instance.
        # *   CPU: the CPU utilization.
        self.metric_name = metric_name
        # The service for which the metric is specified. If you do not set this parameter, the current service is specified by default.
        self.service = service
        # The threshold of the metric that triggers auto scaling.
        # 
        # *   If you set metricName to QPS, scale-out is triggered when the average QPS for a single instance is greater than this threshold.
        # *   If you set metricName to CPU, scale-out is triggered when the average CPU utilization for a single instance is greater than this threshold.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.service is not None:
            result['service'] = self.service

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('service') is not None:
            self.service = m.get('service')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

class DescribeServiceAutoScalerResponseBodyCurrentMetrics(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        service: str = None,
        value: float = None,
    ):
        # The metric name. Valid values:
        # 
        # *   QPS
        # *   CPU
        self.metric_name = metric_name
        # The service for which the metric is specified.
        self.service = service
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.service is not None:
            result['service'] = self.service

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('service') is not None:
            self.service = m.get('service')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

