# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class EnableApplicationScalingRuleResponseBody(DaraModel):
    def __init__(
        self,
        app_scaling_rule: main_models.EnableApplicationScalingRuleResponseBodyAppScalingRule = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The information about the auto scaling policy.
        self.app_scaling_rule = app_scaling_rule
        # The HTTP status code.
        self.code = code
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.app_scaling_rule:
            self.app_scaling_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_scaling_rule is not None:
            result['AppScalingRule'] = self.app_scaling_rule.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppScalingRule') is not None:
            temp_model = main_models.EnableApplicationScalingRuleResponseBodyAppScalingRule()
            self.app_scaling_rule = temp_model.from_map(m.get('AppScalingRule'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class EnableApplicationScalingRuleResponseBodyAppScalingRule(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: int = None,
        last_disable_time: int = None,
        max_replicas: int = None,
        metric: main_models.EnableApplicationScalingRuleResponseBodyAppScalingRuleMetric = None,
        min_replicas: int = None,
        scale_rule_enabled: bool = None,
        scale_rule_name: str = None,
        scale_rule_type: str = None,
        trigger: main_models.EnableApplicationScalingRuleResponseBodyAppScalingRuleTrigger = None,
        update_time: int = None,
    ):
        # The ID of the application to which the auto scaling policy belongs.
        self.app_id = app_id
        # The time when the auto scaling policy was created.
        self.create_time = create_time
        # The time when the auto scaling policy was last disabled.
        self.last_disable_time = last_disable_time
        # This parameter is deprecated.
        self.max_replicas = max_replicas
        # This parameter is deprecated.
        self.metric = metric
        # This parameter is deprecated.
        self.min_replicas = min_replicas
        # Indicates whether the auto scaling policy is enabled. Valid values:
        # 
        # - **true**: The auto scaling policy is enabled.
        # 
        # - **false**: The auto scaling policy is disabled.
        self.scale_rule_enabled = scale_rule_enabled
        # The name of the auto scaling policy.
        self.scale_rule_name = scale_rule_name
        # The type of the auto scaling policy. The value is fixed to trigger.
        self.scale_rule_type = scale_rule_type
        # The configurations of the trigger.
        self.trigger = trigger
        # The time when the auto scaling policy was last modified.
        self.update_time = update_time

    def validate(self):
        if self.metric:
            self.metric.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.last_disable_time is not None:
            result['LastDisableTime'] = self.last_disable_time

        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas

        if self.metric is not None:
            result['Metric'] = self.metric.to_map()

        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas

        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled

        if self.scale_rule_name is not None:
            result['ScaleRuleName'] = self.scale_rule_name

        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type

        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastDisableTime') is not None:
            self.last_disable_time = m.get('LastDisableTime')

        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')

        if m.get('Metric') is not None:
            temp_model = main_models.EnableApplicationScalingRuleResponseBodyAppScalingRuleMetric()
            self.metric = temp_model.from_map(m.get('Metric'))

        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')

        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')

        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')

        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')

        if m.get('Trigger') is not None:
            temp_model = main_models.EnableApplicationScalingRuleResponseBodyAppScalingRuleTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class EnableApplicationScalingRuleResponseBodyAppScalingRuleTrigger(DaraModel):
    def __init__(
        self,
        max_replicas: int = None,
        min_replicas: int = None,
        triggers: List[main_models.EnableApplicationScalingRuleResponseBodyAppScalingRuleTriggerTriggers] = None,
    ):
        # The maximum number of replicas. The upper limit is 1000.
        self.max_replicas = max_replicas
        # The minimum number of replicas. The lower limit is 0.
        self.min_replicas = min_replicas
        # The list of triggers.
        self.triggers = triggers

    def validate(self):
        if self.triggers:
            for v1 in self.triggers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas

        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas

        result['Triggers'] = []
        if self.triggers is not None:
            for k1 in self.triggers:
                result['Triggers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')

        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')

        self.triggers = []
        if m.get('Triggers') is not None:
            for k1 in m.get('Triggers'):
                temp_model = main_models.EnableApplicationScalingRuleResponseBodyAppScalingRuleTriggerTriggers()
                self.triggers.append(temp_model.from_map(k1))

        return self

class EnableApplicationScalingRuleResponseBodyAppScalingRuleTriggerTriggers(DaraModel):
    def __init__(
        self,
        meta_data: str = None,
        name: str = None,
        type: str = None,
    ):
        # The metadata of the trigger.
        self.meta_data = meta_data
        # The name of the trigger.
        self.name = name
        # The type of the trigger. Valid values: cron and app_metric.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta_data is not None:
            result['MetaData'] = self.meta_data

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class EnableApplicationScalingRuleResponseBodyAppScalingRuleMetric(DaraModel):
    def __init__(
        self,
        max_replicas: int = None,
        metrics: List[main_models.EnableApplicationScalingRuleResponseBodyAppScalingRuleMetricMetrics] = None,
        min_replicas: int = None,
    ):
        # This parameter is deprecated.
        self.max_replicas = max_replicas
        # This parameter is deprecated.
        self.metrics = metrics
        # This parameter is deprecated.
        self.min_replicas = min_replicas

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
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas

        result['Metrics'] = []
        if self.metrics is not None:
            for k1 in self.metrics:
                result['Metrics'].append(k1.to_map() if k1 else None)

        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')

        self.metrics = []
        if m.get('Metrics') is not None:
            for k1 in m.get('Metrics'):
                temp_model = main_models.EnableApplicationScalingRuleResponseBodyAppScalingRuleMetricMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')

        return self

class EnableApplicationScalingRuleResponseBodyAppScalingRuleMetricMetrics(DaraModel):
    def __init__(
        self,
        metric_target_average_utilization: int = None,
        metric_type: str = None,
    ):
        # This parameter is deprecated.
        self.metric_target_average_utilization = metric_target_average_utilization
        # This parameter is deprecated.
        self.metric_type = metric_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_target_average_utilization is not None:
            result['MetricTargetAverageUtilization'] = self.metric_target_average_utilization

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricTargetAverageUtilization') is not None:
            self.metric_target_average_utilization = m.get('MetricTargetAverageUtilization')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        return self

