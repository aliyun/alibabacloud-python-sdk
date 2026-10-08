# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationScalingRulesResponseBody(DaraModel):
    def __init__(
        self,
        app_scaling_rules: main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRules = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The Auto Scaling rules for the application.
        self.app_scaling_rules = app_scaling_rules
        # The HTTP status code.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.app_scaling_rules:
            self.app_scaling_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_scaling_rules is not None:
            result['AppScalingRules'] = self.app_scaling_rules.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppScalingRules') is not None:
            temp_model = main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRules()
            self.app_scaling_rules = temp_model.from_map(m.get('AppScalingRules'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeApplicationScalingRulesResponseBodyAppScalingRules(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        result: List[main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResult] = None,
        total_size: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The number of scaling rules returned on each page.
        self.page_size = page_size
        # The details of the Auto Scaling rules.
        self.result = result
        # The total number of scaling rules.
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class DescribeApplicationScalingRulesResponseBodyAppScalingRulesResult(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        behaviour: main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviour = None,
        create_time: int = None,
        last_disable_time: int = None,
        max_replicas: int = None,
        metric: main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultMetric = None,
        min_replicas: int = None,
        scale_rule_enabled: bool = None,
        scale_rule_name: str = None,
        scale_rule_type: str = None,
        trigger: main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultTrigger = None,
        update_time: int = None,
    ):
        # The ID of the application to which the scaling rule belongs.
        self.app_id = app_id
        # The scaling behavior.
        self.behaviour = behaviour
        # The UNIX timestamp when the scaling rule was created.
        self.create_time = create_time
        # The UNIX timestamp when the scaling rule was last disabled.
        self.last_disable_time = last_disable_time
        # This parameter is deprecated.
        self.max_replicas = max_replicas
        # This parameter is deprecated.
        self.metric = metric
        # This parameter is deprecated.
        self.min_replicas = min_replicas
        # Indicates whether the scaling rule is enabled.
        # 
        # - **true**: The scaling rule is enabled.
        # 
        # - **false**: The scaling rule is disabled.
        self.scale_rule_enabled = scale_rule_enabled
        # The name of the scaling rule.
        self.scale_rule_name = scale_rule_name
        # The type of the scaling rule. Only \\`trigger\\` is supported.
        self.scale_rule_type = scale_rule_type
        # The trigger configuration.
        self.trigger = trigger
        # The UNIX timestamp when the scaling rule was last updated.
        self.update_time = update_time

    def validate(self):
        if self.behaviour:
            self.behaviour.validate()
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

        if self.behaviour is not None:
            result['Behaviour'] = self.behaviour.to_map()

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

        if m.get('Behaviour') is not None:
            temp_model = main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviour()
            self.behaviour = temp_model.from_map(m.get('Behaviour'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastDisableTime') is not None:
            self.last_disable_time = m.get('LastDisableTime')

        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')

        if m.get('Metric') is not None:
            temp_model = main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultMetric()
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
            temp_model = main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultTrigger(DaraModel):
    def __init__(
        self,
        max_replicas: int = None,
        min_replicas: int = None,
        triggers: List[main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultTriggerTriggers] = None,
    ):
        # The maximum number of replicas. The value cannot exceed 1000.
        self.max_replicas = max_replicas
        # The minimum number of replicas. The value cannot be less than 0.
        self.min_replicas = min_replicas
        # A list of trigger configurations.
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
                temp_model = main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultTriggerTriggers()
                self.triggers.append(temp_model.from_map(k1))

        return self

class DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultTriggerTriggers(DaraModel):
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
        # The type of the trigger. Valid values: \\`cron\\` and \\`app_metric\\`.
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

class DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultMetric(DaraModel):
    def __init__(
        self,
        max_replicas: int = None,
        metrics: List[main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultMetricMetrics] = None,
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
                temp_model = main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultMetricMetrics()
                self.metrics.append(temp_model.from_map(k1))

        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')

        return self

class DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultMetricMetrics(DaraModel):
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

class DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviour(DaraModel):
    def __init__(
        self,
        scale_down: main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviourScaleDown = None,
        scale_up: main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviourScaleUp = None,
    ):
        # The configuration of the scale-in behavior.
        self.scale_down = scale_down
        # The configuration of the scale-out behavior.
        self.scale_up = scale_up

    def validate(self):
        if self.scale_down:
            self.scale_down.validate()
        if self.scale_up:
            self.scale_up.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scale_down is not None:
            result['ScaleDown'] = self.scale_down.to_map()

        if self.scale_up is not None:
            result['ScaleUp'] = self.scale_up.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScaleDown') is not None:
            temp_model = main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviourScaleDown()
            self.scale_down = temp_model.from_map(m.get('ScaleDown'))

        if m.get('ScaleUp') is not None:
            temp_model = main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviourScaleUp()
            self.scale_up = temp_model.from_map(m.get('ScaleUp'))

        return self

class DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviourScaleUp(DaraModel):
    def __init__(
        self,
        policies: List[main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviourScaleUpPolicies] = None,
        select_policy: str = None,
        stabilization_window_seconds: int = None,
    ):
        # The policy configuration.
        self.policies = policies
        # The policy for the scaling step size for scale-out events. Valid values: \\`Max\\`, \\`Min\\`, and \\`Disable\\`.
        self.select_policy = select_policy
        # The cooldown period for a scale-out event. Unit: seconds. Valid values: 0 to 3600. Default value: 0.
        self.stabilization_window_seconds = stabilization_window_seconds

    def validate(self):
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.select_policy is not None:
            result['SelectPolicy'] = self.select_policy

        if self.stabilization_window_seconds is not None:
            result['StabilizationWindowSeconds'] = self.stabilization_window_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviourScaleUpPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('SelectPolicy') is not None:
            self.select_policy = m.get('SelectPolicy')

        if m.get('StabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('StabilizationWindowSeconds')

        return self

class DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviourScaleUpPolicies(DaraModel):
    def __init__(
        self,
        period_seconds: int = None,
        type: str = None,
        value: str = None,
    ):
        # The execution interval. Unit: seconds. Valid values: 0 to 1800.
        self.period_seconds = period_seconds
        # The type of the policy. Valid values: \\`Pods\\` and \\`Percent\\`.
        self.type = type
        # The value for the policy. The value must be an integer greater than 0. If \\`Type\\` is \\`Pods\\`, this parameter specifies the number of pods. If \\`Type\\` is \\`Percent\\`, this parameter specifies a percentage. The value can be greater than 100%.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviourScaleDown(DaraModel):
    def __init__(
        self,
        policies: List[main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviourScaleDownPolicies] = None,
        select_policy: str = None,
        stabilization_window_seconds: int = None,
    ):
        # The policy configuration.
        self.policies = policies
        # The policy for the scaling step size for scale-in events. Valid values: \\`Max\\`, \\`Min\\`, and \\`Disable\\`.
        self.select_policy = select_policy
        # The cooldown period for a scale-in event. Unit: seconds. Valid values: 0 to 3600. Default value: 300.
        self.stabilization_window_seconds = stabilization_window_seconds

    def validate(self):
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.select_policy is not None:
            result['SelectPolicy'] = self.select_policy

        if self.stabilization_window_seconds is not None:
            result['StabilizationWindowSeconds'] = self.stabilization_window_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviourScaleDownPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('SelectPolicy') is not None:
            self.select_policy = m.get('SelectPolicy')

        if m.get('StabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('StabilizationWindowSeconds')

        return self

class DescribeApplicationScalingRulesResponseBodyAppScalingRulesResultBehaviourScaleDownPolicies(DaraModel):
    def __init__(
        self,
        period_seconds: int = None,
        type: str = None,
        value: str = None,
    ):
        # The execution interval. Unit: seconds. Valid values: 0 to 1800.
        self.period_seconds = period_seconds
        # The type of the policy. Valid values: \\`Pods\\` and \\`Percent\\`.
        self.type = type
        # The value for the policy. The value must be an integer greater than 0. If \\`Type\\` is \\`Pods\\`, this parameter specifies the number of pods. If \\`Type\\` is \\`Percent\\`, this parameter specifies a percentage. The value can be greater than 100%.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

