# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class ModifyScalingRuleRequest(DaraModel):
    def __init__(
        self,
        adjustment_type: str = None,
        adjustment_value: int = None,
        alarm_dimensions: List[main_models.ModifyScalingRuleRequestAlarmDimensions] = None,
        alarm_options: main_models.ModifyScalingRuleRequestAlarmOptions = None,
        cooldown: int = None,
        disable_scale_in: bool = None,
        estimated_instance_warmup: int = None,
        hybrid_metrics: List[main_models.ModifyScalingRuleRequestHybridMetrics] = None,
        hybrid_monitor_namespace: str = None,
        initial_max_size: int = None,
        metric_name: str = None,
        metric_type: str = None,
        min_adjustment_magnitude: int = None,
        owner_account: str = None,
        owner_id: int = None,
        predictive_scaling_mode: str = None,
        predictive_task_buffer_time: int = None,
        predictive_value_behavior: str = None,
        predictive_value_buffer: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scale_in_evaluation_count: int = None,
        scale_out_evaluation_count: int = None,
        scaling_rule_id: str = None,
        scaling_rule_name: str = None,
        step_adjustments: List[main_models.ModifyScalingRuleRequestStepAdjustments] = None,
        target_value: float = None,
    ):
        # The adjustment method of the scaling rule. This parameter is required and applicable only to simple scaling rules and step scaling rules. Valid values: 
        # 
        # - QuantityChangeInCapacity: adds or removes a specified number of ECS instances. 
        # - PercentChangeInCapacity: adds or removes a specified percentage of ECS instances. 
        # - TotalCapacity: adjusts the number of ECS instances in the scaling group to a specified number.
        self.adjustment_type = adjustment_type
        # The adjustment value of the scaling rule. This parameter is required and applicable only to simple scaling rules and step scaling rules. The number of ECS instances adjusted in a single operation cannot exceed 1,000. Valid values vary based on the adjustment method:
        # 
        # - QuantityChangeInCapacity: -1000 to 1000.
        # - PercentChangeInCapacity: -100 to 10000.
        # - TotalCapacity: 0 to 2000.
        self.adjustment_value = adjustment_value
        # The dimension values of the monitoring metric. This parameter is applicable to target tracking scaling rules and is configured when the monitoring metric requires additional dimension information. For example, the LoadBalancerRealServerAverageQps metric requires the rulePool dimension.
        self.alarm_dimensions = alarm_dimensions
        # The alert attributes.
        self.alarm_options = alarm_options
        # The cooldown time of the scaling rule. This parameter is applicable only to simple scaling rules.
        # 
        # Valid values: 0 to 86400. Unit: seconds.
        self.cooldown = cooldown
        # Specifies whether to disable scale-in. This parameter is applicable only to target tracking scaling rules.
        self.disable_scale_in = disable_scale_in
        # The warmup period of instances. This parameter is applicable to target tracking scaling rules and step scaling rules. ECS instances in the warmup state are added to the scaling group as usual, but they do not report monitoring data to CloudMonitor during the warmup period.
        # 
        # > When the system dynamically calculates the number of ECS instances to scale out or scale in, instances in the warmup state are not counted as existing instances.
        # 
        # Valid values: 0 to 86400. Unit: seconds.
        self.estimated_instance_warmup = estimated_instance_warmup
        # The Hybrid Cloud Monitoring monitoring metrics settings. For more information about how to configure the settings, see [Use formula operations to customize target tracking scaling rules](https://help.aliyun.com/document_detail/2852162.html).
        self.hybrid_metrics = hybrid_metrics
        # The ID of the Hybrid Cloud Monitoring monitoring metrics repository.
        # 
        # For more information about how to manage monitoring metrics repositories, see [Manage monitoring metrics repositories](https://help.aliyun.com/document_detail/217606.html).
        self.hybrid_monitor_namespace = hybrid_monitor_namespace
        # The maximum number of instances in the scaling group. This parameter is used together with `PredictiveValueBehavior`.
        self.initial_max_size = initial_max_size
        # The predefined monitoring metric. This parameter is required and applicable to target tracking scaling rules and predictive scaling rules.
        # 
        # Valid values for target tracking scaling rules:
        # 
        # - CpuUtilizationAgent: the CPU utilization collected by the CloudMonitor agent (recommended).
        # - MemoryUtilization: the memory usage collected by the CloudMonitor agent (recommended).
        # - CpuUtilization: the average CPU utilization of ECS instances.
        # - IntranetTx: the average outbound internal traffic of ECS instances.
        # - IntranetRx: the average inbound internal traffic of ECS instances.
        # - VpcInternetTx: the average outbound Internet traffic of ECS instances.
        # - VpcInternetRx: the average inbound Internet traffic of ECS instances.
        # - LoadBalancerRealServerAverageQps: the average queries per second (QPS) per backend server in an Application Load Balancer (ALB) server group.
        # 
        # Valid values for predictive scaling rules:
        # 
        # - CpuUtilization: the average CPU utilization of ECS instances.
        # - IntranetRx: the average inbound internal traffic of ECS instances.
        # - IntranetTx: the average outbound internal traffic of ECS instances.
        # 
        # For more information, see [System monitoring event-triggered tasks](https://help.aliyun.com/document_detail/74854.html).
        self.metric_name = metric_name
        # The type of the monitoring metric. Valid values:
        # 
        # - system: uses system metrics of CloudMonitor.
        # - custom: uses custom metrics reported to CloudMonitor.
        # - hybrid: uses metrics of Hybrid Cloud Monitoring.
        self.metric_type = metric_type
        # The minimum number of instances to adjust. This parameter takes effect only when the scaling rule type is SimpleScalingRule or StepScalingRule and `AdjustmentType` is set to `PercentChangeInCapacity`.
        self.min_adjustment_magnitude = min_adjustment_magnitude
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The mode of the predictive scaling rule. Valid values:
        # 
        # - PredictAndScale: generates prediction results and creates predictive tasks.
        # - PredictOnly: generates prediction results but does not create predictive tasks.
        self.predictive_scaling_mode = predictive_scaling_mode
        # By default, predictive tasks automatically created by predictive scaling rules are executed on the hour. You can set a pre-start time to execute the predictive tasks in advance and prepare resources. Valid values: 0 to 60. Unit: minutes.
        self.predictive_task_buffer_time = predictive_task_buffer_time
        # The method to handle the maximum value for the predictive scaling rule. Valid values:
        # 
        # - MaxOverridePredictiveValue: the initial maximum value overrides the predicted value. If the predicted value is greater than the initial maximum value, the initial maximum value is used as the maximum value for the predictive task.
        # - PredictiveValueOverrideMax: the predicted value overrides the initial maximum value. If the predicted value is greater than the initial maximum value, the predicted value is used as the maximum value for the predictive task.
        # - PredictiveValueOverrideMaxWithBuffer: a buffer ratio is added to the predicted value. The predicted value is increased by the ratio specified by PredictiveValueBuffer. If the increased value is greater than the initial maximum value, the increased value is used.
        self.predictive_value_behavior = predictive_value_behavior
        # The buffer ratio added to the predicted value. This parameter takes effect only when `PredictiveValueBehavior` is set to `PredictiveValueOverrideMaxWithBuffer`. The predicted value is increased by this ratio. If the increased value is greater than the initial maximum value, the increased value is used. Valid values: 0 to 100.
        self.predictive_value_buffer = predictive_value_buffer
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # After a target tracking scaling rule is created, an event-triggered task is automatically created. This parameter specifies the number of consecutive times that the threshold condition must be met before the scale-in event-triggered task triggers an alert.
        self.scale_in_evaluation_count = scale_in_evaluation_count
        # After a target tracking scaling rule is created, an event-triggered task is automatically created. This parameter specifies the number of consecutive times that the threshold condition must be met before the scale-out event-triggered task triggers an alert.
        self.scale_out_evaluation_count = scale_out_evaluation_count
        # The ID of the scaling rule that you want to modify.
        # 
        # This parameter is required.
        self.scaling_rule_id = scaling_rule_id
        # The name of the scaling rule. The name must be 2 to 64 characters in length and can contain letters, digits, underscores (_), hyphens (-), and periods (.). It must start with a letter or digit. The scaling rule name must be unique within a scaling group in a region for an Alibaba Cloud account.
        self.scaling_rule_name = scaling_rule_name
        # The set of instance scaling configurations for step adjustments.
        self.step_adjustments = step_adjustments
        # The target value. This parameter is applicable to target tracking scaling rules and predictive scaling rules. The value can have up to three decimal places and must be greater than 0.
        self.target_value = target_value

    def validate(self):
        if self.alarm_dimensions:
            for v1 in self.alarm_dimensions:
                 if v1:
                    v1.validate()
        if self.alarm_options:
            self.alarm_options.validate()
        if self.hybrid_metrics:
            for v1 in self.hybrid_metrics:
                 if v1:
                    v1.validate()
        if self.step_adjustments:
            for v1 in self.step_adjustments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type

        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value

        result['AlarmDimensions'] = []
        if self.alarm_dimensions is not None:
            for k1 in self.alarm_dimensions:
                result['AlarmDimensions'].append(k1.to_map() if k1 else None)

        if self.alarm_options is not None:
            result['AlarmOptions'] = self.alarm_options.to_map()

        if self.cooldown is not None:
            result['Cooldown'] = self.cooldown

        if self.disable_scale_in is not None:
            result['DisableScaleIn'] = self.disable_scale_in

        if self.estimated_instance_warmup is not None:
            result['EstimatedInstanceWarmup'] = self.estimated_instance_warmup

        result['HybridMetrics'] = []
        if self.hybrid_metrics is not None:
            for k1 in self.hybrid_metrics:
                result['HybridMetrics'].append(k1.to_map() if k1 else None)

        if self.hybrid_monitor_namespace is not None:
            result['HybridMonitorNamespace'] = self.hybrid_monitor_namespace

        if self.initial_max_size is not None:
            result['InitialMaxSize'] = self.initial_max_size

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.min_adjustment_magnitude is not None:
            result['MinAdjustmentMagnitude'] = self.min_adjustment_magnitude

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.predictive_scaling_mode is not None:
            result['PredictiveScalingMode'] = self.predictive_scaling_mode

        if self.predictive_task_buffer_time is not None:
            result['PredictiveTaskBufferTime'] = self.predictive_task_buffer_time

        if self.predictive_value_behavior is not None:
            result['PredictiveValueBehavior'] = self.predictive_value_behavior

        if self.predictive_value_buffer is not None:
            result['PredictiveValueBuffer'] = self.predictive_value_buffer

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scale_in_evaluation_count is not None:
            result['ScaleInEvaluationCount'] = self.scale_in_evaluation_count

        if self.scale_out_evaluation_count is not None:
            result['ScaleOutEvaluationCount'] = self.scale_out_evaluation_count

        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id

        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name

        result['StepAdjustments'] = []
        if self.step_adjustments is not None:
            for k1 in self.step_adjustments:
                result['StepAdjustments'].append(k1.to_map() if k1 else None)

        if self.target_value is not None:
            result['TargetValue'] = self.target_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')

        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')

        self.alarm_dimensions = []
        if m.get('AlarmDimensions') is not None:
            for k1 in m.get('AlarmDimensions'):
                temp_model = main_models.ModifyScalingRuleRequestAlarmDimensions()
                self.alarm_dimensions.append(temp_model.from_map(k1))

        if m.get('AlarmOptions') is not None:
            temp_model = main_models.ModifyScalingRuleRequestAlarmOptions()
            self.alarm_options = temp_model.from_map(m.get('AlarmOptions'))

        if m.get('Cooldown') is not None:
            self.cooldown = m.get('Cooldown')

        if m.get('DisableScaleIn') is not None:
            self.disable_scale_in = m.get('DisableScaleIn')

        if m.get('EstimatedInstanceWarmup') is not None:
            self.estimated_instance_warmup = m.get('EstimatedInstanceWarmup')

        self.hybrid_metrics = []
        if m.get('HybridMetrics') is not None:
            for k1 in m.get('HybridMetrics'):
                temp_model = main_models.ModifyScalingRuleRequestHybridMetrics()
                self.hybrid_metrics.append(temp_model.from_map(k1))

        if m.get('HybridMonitorNamespace') is not None:
            self.hybrid_monitor_namespace = m.get('HybridMonitorNamespace')

        if m.get('InitialMaxSize') is not None:
            self.initial_max_size = m.get('InitialMaxSize')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('MinAdjustmentMagnitude') is not None:
            self.min_adjustment_magnitude = m.get('MinAdjustmentMagnitude')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PredictiveScalingMode') is not None:
            self.predictive_scaling_mode = m.get('PredictiveScalingMode')

        if m.get('PredictiveTaskBufferTime') is not None:
            self.predictive_task_buffer_time = m.get('PredictiveTaskBufferTime')

        if m.get('PredictiveValueBehavior') is not None:
            self.predictive_value_behavior = m.get('PredictiveValueBehavior')

        if m.get('PredictiveValueBuffer') is not None:
            self.predictive_value_buffer = m.get('PredictiveValueBuffer')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScaleInEvaluationCount') is not None:
            self.scale_in_evaluation_count = m.get('ScaleInEvaluationCount')

        if m.get('ScaleOutEvaluationCount') is not None:
            self.scale_out_evaluation_count = m.get('ScaleOutEvaluationCount')

        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')

        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')

        self.step_adjustments = []
        if m.get('StepAdjustments') is not None:
            for k1 in m.get('StepAdjustments'):
                temp_model = main_models.ModifyScalingRuleRequestStepAdjustments()
                self.step_adjustments.append(temp_model.from_map(k1))

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        return self

class ModifyScalingRuleRequestStepAdjustments(DaraModel):
    def __init__(
        self,
        metric_interval_lower_bound: float = None,
        metric_interval_upper_bound: float = None,
        scaling_adjustment: int = None,
    ):
        # The lower boundary of the step adjustment. This parameter is applicable only to step scaling rules. Valid values: -9.999999E18 to 9.999999E18.
        self.metric_interval_lower_bound = metric_interval_lower_bound
        # The upper boundary of the step adjustment. This parameter is applicable only to step scaling rules. Valid values: -9.999999E18 to 9.999999E18.
        self.metric_interval_upper_bound = metric_interval_upper_bound
        # The number of instances to adjust for the step adjustment. This parameter is applicable only to step scaling rules.
        self.scaling_adjustment = scaling_adjustment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_interval_lower_bound is not None:
            result['MetricIntervalLowerBound'] = self.metric_interval_lower_bound

        if self.metric_interval_upper_bound is not None:
            result['MetricIntervalUpperBound'] = self.metric_interval_upper_bound

        if self.scaling_adjustment is not None:
            result['ScalingAdjustment'] = self.scaling_adjustment

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricIntervalLowerBound') is not None:
            self.metric_interval_lower_bound = m.get('MetricIntervalLowerBound')

        if m.get('MetricIntervalUpperBound') is not None:
            self.metric_interval_upper_bound = m.get('MetricIntervalUpperBound')

        if m.get('ScalingAdjustment') is not None:
            self.scaling_adjustment = m.get('ScalingAdjustment')

        return self

class ModifyScalingRuleRequestHybridMetrics(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.ModifyScalingRuleRequestHybridMetricsDimensions] = None,
        expression: str = None,
        id: str = None,
        metric_name: str = None,
        statistic: str = None,
    ):
        # The dimensions of the metric. This parameter is used to specify the resources monitored by the metric.
        self.dimensions = dimensions
        # The metric operation expression for multiple Hybrid Cloud Monitoring metrics. The calculation result of the expression is used to trigger scaling activities.
        # 
        # The operation expression must comply with the Reverse Polish Notation (RPN) specification, and only the `+`, `-`, `*`, and `/` operators are supported.
        self.expression = expression
        # The reference ID of the metric in the metric operation expression.
        self.id = id
        # The name of the metric in the Hybrid Cloud Monitoring monitoring metrics repository.
        self.metric_name = metric_name
        # The statistical method of the metric. Valid values:
        # 
        # - Average: the average value of all data points in the specified period.
        # - Minimum: the minimum value of all data points in the specified period.
        # - Maximum: the maximum value of all data points in the specified period.
        self.statistic = statistic

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.id is not None:
            result['Id'] = self.id

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.statistic is not None:
            result['Statistic'] = self.statistic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.ModifyScalingRuleRequestHybridMetricsDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Statistic') is not None:
            self.statistic = m.get('Statistic')

        return self

class ModifyScalingRuleRequestHybridMetricsDimensions(DaraModel):
    def __init__(
        self,
        dimension_key: str = None,
        dimension_value: str = None,
    ):
        # The key of the metric dimension.
        self.dimension_key = dimension_key
        # The value of the metric dimension.
        self.dimension_value = dimension_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key

        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')

        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')

        return self

class ModifyScalingRuleRequestAlarmOptions(DaraModel):
    def __init__(
        self,
        period: int = None,
    ):
        # The period for collecting monitoring metric data in the target tracking scaling rule. Unit: seconds. Valid values:
        # 
        # - 15
        # - 60
        # - 120
        # - 300
        # - 900
        # 
        # > Default value: 60.
        self.period = period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period is not None:
            result['Period'] = self.period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')

        return self

class ModifyScalingRuleRequestAlarmDimensions(DaraModel):
    def __init__(
        self,
        dimension_key: str = None,
        dimension_value: str = None,
    ):
        # The key of the dimension associated with the monitoring metric.
        self.dimension_key = dimension_key
        # The value of the dimension associated with the monitoring metric.
        self.dimension_value = dimension_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key

        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')

        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')

        return self

