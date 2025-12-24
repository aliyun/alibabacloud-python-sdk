# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class UpdateServiceAutoScalerRequest(DaraModel):
    def __init__(
        self,
        behavior: main_models.UpdateServiceAutoScalerRequestBehavior = None,
        max: int = None,
        min: int = None,
        scale_strategies: List[main_models.UpdateServiceAutoScalerRequestScaleStrategies] = None,
    ):
        # The Autoscaler operation.
        self.behavior = behavior
        # The maximum number of instances. The value must be greater than that of the min parameter.
        # 
        # This parameter is required.
        self.max = max
        # The minimum number of instances. The value must be greater than 0.
        # 
        # This parameter is required.
        self.min = min
        # The auto scaling policies.
        # 
        # This parameter is required.
        self.scale_strategies = scale_strategies

    def validate(self):
        if self.behavior:
            self.behavior.validate()
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
            result['behavior'] = self.behavior.to_map()

        if self.max is not None:
            result['max'] = self.max

        if self.min is not None:
            result['min'] = self.min

        result['scaleStrategies'] = []
        if self.scale_strategies is not None:
            for k1 in self.scale_strategies:
                result['scaleStrategies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('behavior') is not None:
            temp_model = main_models.UpdateServiceAutoScalerRequestBehavior()
            self.behavior = temp_model.from_map(m.get('behavior'))

        if m.get('max') is not None:
            self.max = m.get('max')

        if m.get('min') is not None:
            self.min = m.get('min')

        self.scale_strategies = []
        if m.get('scaleStrategies') is not None:
            for k1 in m.get('scaleStrategies'):
                temp_model = main_models.UpdateServiceAutoScalerRequestScaleStrategies()
                self.scale_strategies.append(temp_model.from_map(k1))

        return self

class UpdateServiceAutoScalerRequestScaleStrategies(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        service: str = None,
        threshold: float = None,
    ):
        # The name of the metric for triggering auto scaling. Valid values:
        # 
        # *   qps: the queries per second (QPS) for an individual instance.
        # *   cpu: the CPU utilization.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The service for which the metric is specified. If you do not set this parameter, the current service is specified by default.
        self.service = service
        # The threshold of the metric that triggers auto scaling.
        # 
        # *   If you set metricName to QPS, scale-out is triggered when the average QPS for a single instance is greater than this threshold.
        # *   If you set metricName to CPU, scale-out is triggered when the average CPU utilization for a single instance is greater than this threshold.
        # 
        # This parameter is required.
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

class UpdateServiceAutoScalerRequestBehavior(DaraModel):
    def __init__(
        self,
        on_zero: main_models.UpdateServiceAutoScalerRequestBehaviorOnZero = None,
        scale_down: main_models.UpdateServiceAutoScalerRequestBehaviorScaleDown = None,
        scale_up: main_models.UpdateServiceAutoScalerRequestBehaviorScaleUp = None,
    ):
        # The operation that reduces the number of instances to 0.
        self.on_zero = on_zero
        # The scale-in operation.
        self.scale_down = scale_down
        # The scale-out operation.
        self.scale_up = scale_up

    def validate(self):
        if self.on_zero:
            self.on_zero.validate()
        if self.scale_down:
            self.scale_down.validate()
        if self.scale_up:
            self.scale_up.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.on_zero is not None:
            result['onZero'] = self.on_zero.to_map()

        if self.scale_down is not None:
            result['scaleDown'] = self.scale_down.to_map()

        if self.scale_up is not None:
            result['scaleUp'] = self.scale_up.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('onZero') is not None:
            temp_model = main_models.UpdateServiceAutoScalerRequestBehaviorOnZero()
            self.on_zero = temp_model.from_map(m.get('onZero'))

        if m.get('scaleDown') is not None:
            temp_model = main_models.UpdateServiceAutoScalerRequestBehaviorScaleDown()
            self.scale_down = temp_model.from_map(m.get('scaleDown'))

        if m.get('scaleUp') is not None:
            temp_model = main_models.UpdateServiceAutoScalerRequestBehaviorScaleUp()
            self.scale_up = temp_model.from_map(m.get('scaleUp'))

        return self

class UpdateServiceAutoScalerRequestBehaviorScaleUp(DaraModel):
    def __init__(
        self,
        stabilization_window_seconds: int = None,
    ):
        # The time window that is required before the scale-out operation is performed. Default value: 0. The scale-out operation can be performed only if the specified metric exceeds the specified threshold in the specified time window.
        self.stabilization_window_seconds = stabilization_window_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stabilization_window_seconds is not None:
            result['stabilizationWindowSeconds'] = self.stabilization_window_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('stabilizationWindowSeconds')

        return self

class UpdateServiceAutoScalerRequestBehaviorScaleDown(DaraModel):
    def __init__(
        self,
        stabilization_window_seconds: int = None,
    ):
        # The time window that is required before the scale-in operation is performed. Default value: 300. The scale-in operation can be performed only if the specified metric drops below the threshold in the specified time window.
        self.stabilization_window_seconds = stabilization_window_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stabilization_window_seconds is not None:
            result['stabilizationWindowSeconds'] = self.stabilization_window_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('stabilizationWindowSeconds')

        return self

class UpdateServiceAutoScalerRequestBehaviorOnZero(DaraModel):
    def __init__(
        self,
        scale_down_grace_period_seconds: int = None,
        scale_up_activation_replicas: int = None,
    ):
        # The time window that is required before the number of instances is reduced to 0. Default value: 600. The number of instances can be reduced to 0 only if no request is available or no traffic exists in the specified time window.
        self.scale_down_grace_period_seconds = scale_down_grace_period_seconds
        # The number of instances that you want to create at a time if the number of instances is scaled out from 0. Default value: 1.
        self.scale_up_activation_replicas = scale_up_activation_replicas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scale_down_grace_period_seconds is not None:
            result['scaleDownGracePeriodSeconds'] = self.scale_down_grace_period_seconds

        if self.scale_up_activation_replicas is not None:
            result['scaleUpActivationReplicas'] = self.scale_up_activation_replicas

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scaleDownGracePeriodSeconds') is not None:
            self.scale_down_grace_period_seconds = m.get('scaleDownGracePeriodSeconds')

        if m.get('scaleUpActivationReplicas') is not None:
            self.scale_up_activation_replicas = m.get('scaleUpActivationReplicas')

        return self

