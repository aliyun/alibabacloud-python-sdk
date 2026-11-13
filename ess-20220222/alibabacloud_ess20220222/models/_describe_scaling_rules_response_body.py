# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeScalingRulesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_rules: List[main_models.DescribeScalingRulesResponseBodyScalingRules] = None,
        total_count: int = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The information about the scaling rules.
        self.scaling_rules = scaling_rules
        # The total number of scaling rules.
        self.total_count = total_count

    def validate(self):
        if self.scaling_rules:
            for v1 in self.scaling_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ScalingRules'] = []
        if self.scaling_rules is not None:
            for k1 in self.scaling_rules:
                result['ScalingRules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scaling_rules = []
        if m.get('ScalingRules') is not None:
            for k1 in m.get('ScalingRules'):
                temp_model = main_models.DescribeScalingRulesResponseBodyScalingRules()
                self.scaling_rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeScalingRulesResponseBodyScalingRules(DaraModel):
    def __init__(
        self,
        adjustment_type: str = None,
        adjustment_value: int = None,
        alarm_dimensions: List[main_models.DescribeScalingRulesResponseBodyScalingRulesAlarmDimensions] = None,
        alarms: List[main_models.DescribeScalingRulesResponseBodyScalingRulesAlarms] = None,
        cooldown: int = None,
        disable_scale_in: bool = None,
        estimated_instance_warmup: int = None,
        hybrid_metrics: List[main_models.DescribeScalingRulesResponseBodyScalingRulesHybridMetrics] = None,
        hybrid_monitor_namespace: str = None,
        initial_max_size: int = None,
        max_size: int = None,
        metric_name: str = None,
        metric_type: str = None,
        min_adjustment_magnitude: int = None,
        min_size: int = None,
        predictive_scaling_mode: str = None,
        predictive_task_buffer_time: int = None,
        predictive_value_behavior: str = None,
        predictive_value_buffer: int = None,
        scale_in_evaluation_count: int = None,
        scale_out_evaluation_count: int = None,
        scaling_group_id: str = None,
        scaling_rule_ari: str = None,
        scaling_rule_id: str = None,
        scaling_rule_name: str = None,
        scaling_rule_type: str = None,
        step_adjustments: List[main_models.DescribeScalingRulesResponseBodyScalingRulesStepAdjustments] = None,
        target_value: float = None,
    ):
        # The adjustment type of the scaling rule. Valid values:
        # 
        # - QuantityChangeInCapacity: increases or decreases a specified number of ECS instances.
        # - PercentChangeInCapacity: increases or decreases a specified percentage of ECS instances.
        # - TotalCapacity: adjusts the number of ECS instances in the scaling group to a specified number.
        self.adjustment_type = adjustment_type
        # The adjustment value of the scaling rule.
        self.adjustment_value = adjustment_value
        # The dimension value of the metric. This parameter applies to target tracking scaling rules and is configured when the metric requires additional dimension information. For example, the LoadBalancerRealServerAverageQps metric requires the rulePool dimension information.
        self.alarm_dimensions = alarm_dimensions
        # The CloudMonitor event-triggered tasks associated with the scaling rule. The associated CloudMonitor event-triggered tasks are returned only when the ShowAlarmRules parameter is set to true. Otherwise, an empty list is returned.
        self.alarms = alarms
        # The cooldown time of the scaling rule. This parameter applies only to simple scaling rules. Valid values: 0 to 86400. Unit: seconds.
        self.cooldown = cooldown
        # Specifies whether to disable scale-in. This parameter applies only to target tracking scaling rules. Valid values:
        # 
        # - true: disables scale-in.
        # - false: allows scale-in.
        self.disable_scale_in = disable_scale_in
        # The warmup time required for newly created instances to complete a series of preparations. During the warmup period, the started instances do not affect the monitoring metrics of the scaling group.
        self.estimated_instance_warmup = estimated_instance_warmup
        # The monitoring metrics settings for Hybrid Cloud Monitoring. For more information about how to configure the settings, see [Use formula operations to customize target tracking scaling rules](https://help.aliyun.com/document_detail/2852162.html).
        self.hybrid_metrics = hybrid_metrics
        # The ID of the monitoring metrics repository for Hybrid Cloud Monitoring.
        # 
        # To manage monitoring metrics repositories, see [Manage monitoring metrics repositories](https://help.aliyun.com/document_detail/217606.html).
        self.hybrid_monitor_namespace = hybrid_monitor_namespace
        # The maximum number of instances in the scaling group. This parameter is used in combination with PredictiveValueBehavior.
        self.initial_max_size = initial_max_size
        # The maximum number of instances in the scaling group.
        self.max_size = max_size
        # The name of the metric for the event-triggered task associated with the scaling rule.
        self.metric_name = metric_name
        # The type of the metric. Valid values:
        # 
        # - system: uses system metrics of CloudMonitor.
        # - custom: uses custom metrics reported to CloudMonitor.
        # - hybrid: uses metrics of Hybrid Cloud Monitoring.
        self.metric_type = metric_type
        # The minimum number of instances to be adjusted by the scaling rule. This parameter takes effect only when the scaling rule type is SimpleScalingRule or StepScalingRule and the AdjustmentType is PercentChangeInCapacity.
        self.min_adjustment_magnitude = min_adjustment_magnitude
        # The minimum number of instances in the scaling group.
        self.min_size = min_size
        # The mode of the predictive scaling rule. Valid values:
        # 
        # - PredictAndScale: generates prediction results and creates predictive tasks.
        # - PredictOnly: generates prediction results but does not create predictive tasks.
        self.predictive_scaling_mode = predictive_scaling_mode
        # The predictive tasks automatically created by the predictive scaling rule are executed on the hour by default. You can set the pre-start time to execute the predictive tasks in advance and prepare resources. Valid values: 0 to 60. Unit: minutes.
        self.predictive_task_buffer_time = predictive_task_buffer_time
        # The processing method for the maximum value of the predictive scaling rule. Valid values:
        # 
        # - MaxOverridePredictiveValue: the initial maximum value overrides the predicted value. If the predicted value is greater than the initial maximum value, the maximum value of the predictive task uses the initial maximum value.
        # - PredictiveValueOverrideMax: the predicted value overrides the initial maximum value. If the predicted value is greater than the initial maximum value, the maximum value of the predictive task uses the predicted value.
        # - PredictiveValueOverrideMaxWithBuffer: a certain percentage is added to the predicted value. The predicted value is increased by the percentage specified by PredictiveValueBuffer. If the increased value is greater than the initial maximum value, the increased value is used.
        self.predictive_value_behavior = predictive_value_behavior
        # This parameter takes effect when PredictiveValueBehavior is set to PredictiveValueOverrideMaxWithBuffer. The predicted value is increased by this percentage. If the increased value is greater than the initial maximum value, the increased value is used. Valid values: 0 to 100.
        self.predictive_value_buffer = predictive_value_buffer
        # After a target tracking scaling rule is created, an event-triggered task is automatically created. This parameter specifies the number of consecutive times the threshold condition must be met to trigger the scale-in event-triggered task.
        self.scale_in_evaluation_count = scale_in_evaluation_count
        # After a target tracking scaling rule is created, an event-triggered task is automatically created. This parameter specifies the number of consecutive times the threshold condition must be met to trigger the scale-out event-triggered task.
        self.scale_out_evaluation_count = scale_out_evaluation_count
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The unique identifier of the scaling rule.
        self.scaling_rule_ari = scaling_rule_ari
        # The ID of the scaling rule.
        self.scaling_rule_id = scaling_rule_id
        # The name of the scaling rule.
        self.scaling_rule_name = scaling_rule_name
        # The type of the scaling rule. Valid values:
        # 
        # - SimpleScalingRule: simple scaling rule. Adjusts the number of ECS instances based on the adjustment type (AdjustmentType) and adjustment value (AdjustmentValue).
        # - TargetTrackingScalingRule: target tracking scaling rule. Dynamically calculates the number of ECS instances to scale out or scale-in based on a predefined metric (MetricName) and attempts to maintain the metric value near the target value (TargetValue).
        # - StepScalingRule: step scaling rule. Provides a step-by-step extension method based on thresholds and metric values.
        # - PredictiveScalingRule: predictive scaling rule. Analyzes the historical monitoring data of the scaling group based on machine learning capabilities to predict future monitoring metrics, and supports the automatic creation of scheduled tasks to set the boundaries of the scaling group.
        self.scaling_rule_type = scaling_rule_type
        # The step adjustments of the step scaling rule.
        self.step_adjustments = step_adjustments
        # The target value. When the scaling rule is a target tracking scaling rule or a predictive scaling rule, the scaling rule maintains the metric near the target value by adding or removing instances.
        self.target_value = target_value

    def validate(self):
        if self.alarm_dimensions:
            for v1 in self.alarm_dimensions:
                 if v1:
                    v1.validate()
        if self.alarms:
            for v1 in self.alarms:
                 if v1:
                    v1.validate()
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

        result['Alarms'] = []
        if self.alarms is not None:
            for k1 in self.alarms:
                result['Alarms'].append(k1.to_map() if k1 else None)

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

        if self.max_size is not None:
            result['MaxSize'] = self.max_size

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.min_adjustment_magnitude is not None:
            result['MinAdjustmentMagnitude'] = self.min_adjustment_magnitude

        if self.min_size is not None:
            result['MinSize'] = self.min_size

        if self.predictive_scaling_mode is not None:
            result['PredictiveScalingMode'] = self.predictive_scaling_mode

        if self.predictive_task_buffer_time is not None:
            result['PredictiveTaskBufferTime'] = self.predictive_task_buffer_time

        if self.predictive_value_behavior is not None:
            result['PredictiveValueBehavior'] = self.predictive_value_behavior

        if self.predictive_value_buffer is not None:
            result['PredictiveValueBuffer'] = self.predictive_value_buffer

        if self.scale_in_evaluation_count is not None:
            result['ScaleInEvaluationCount'] = self.scale_in_evaluation_count

        if self.scale_out_evaluation_count is not None:
            result['ScaleOutEvaluationCount'] = self.scale_out_evaluation_count

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.scaling_rule_ari is not None:
            result['ScalingRuleAri'] = self.scaling_rule_ari

        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id

        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name

        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type

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
                temp_model = main_models.DescribeScalingRulesResponseBodyScalingRulesAlarmDimensions()
                self.alarm_dimensions.append(temp_model.from_map(k1))

        self.alarms = []
        if m.get('Alarms') is not None:
            for k1 in m.get('Alarms'):
                temp_model = main_models.DescribeScalingRulesResponseBodyScalingRulesAlarms()
                self.alarms.append(temp_model.from_map(k1))

        if m.get('Cooldown') is not None:
            self.cooldown = m.get('Cooldown')

        if m.get('DisableScaleIn') is not None:
            self.disable_scale_in = m.get('DisableScaleIn')

        if m.get('EstimatedInstanceWarmup') is not None:
            self.estimated_instance_warmup = m.get('EstimatedInstanceWarmup')

        self.hybrid_metrics = []
        if m.get('HybridMetrics') is not None:
            for k1 in m.get('HybridMetrics'):
                temp_model = main_models.DescribeScalingRulesResponseBodyScalingRulesHybridMetrics()
                self.hybrid_metrics.append(temp_model.from_map(k1))

        if m.get('HybridMonitorNamespace') is not None:
            self.hybrid_monitor_namespace = m.get('HybridMonitorNamespace')

        if m.get('InitialMaxSize') is not None:
            self.initial_max_size = m.get('InitialMaxSize')

        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('MinAdjustmentMagnitude') is not None:
            self.min_adjustment_magnitude = m.get('MinAdjustmentMagnitude')

        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')

        if m.get('PredictiveScalingMode') is not None:
            self.predictive_scaling_mode = m.get('PredictiveScalingMode')

        if m.get('PredictiveTaskBufferTime') is not None:
            self.predictive_task_buffer_time = m.get('PredictiveTaskBufferTime')

        if m.get('PredictiveValueBehavior') is not None:
            self.predictive_value_behavior = m.get('PredictiveValueBehavior')

        if m.get('PredictiveValueBuffer') is not None:
            self.predictive_value_buffer = m.get('PredictiveValueBuffer')

        if m.get('ScaleInEvaluationCount') is not None:
            self.scale_in_evaluation_count = m.get('ScaleInEvaluationCount')

        if m.get('ScaleOutEvaluationCount') is not None:
            self.scale_out_evaluation_count = m.get('ScaleOutEvaluationCount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('ScalingRuleAri') is not None:
            self.scaling_rule_ari = m.get('ScalingRuleAri')

        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')

        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')

        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')

        self.step_adjustments = []
        if m.get('StepAdjustments') is not None:
            for k1 in m.get('StepAdjustments'):
                temp_model = main_models.DescribeScalingRulesResponseBodyScalingRulesStepAdjustments()
                self.step_adjustments.append(temp_model.from_map(k1))

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        return self

class DescribeScalingRulesResponseBodyScalingRulesStepAdjustments(DaraModel):
    def __init__(
        self,
        metric_interval_lower_bound: float = None,
        metric_interval_upper_bound: float = None,
        scaling_adjustment: int = None,
    ):
        # The lower boundary of the step adjustment. Valid values: -9.999999E18 to 9.999999E18.
        self.metric_interval_lower_bound = metric_interval_lower_bound
        # The upper boundary of the step adjustment. Valid values: -9.999999E18 to 9.999999E18.
        self.metric_interval_upper_bound = metric_interval_upper_bound
        # The number of instances to be scaled for the step adjustment.
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

class DescribeScalingRulesResponseBodyScalingRulesHybridMetrics(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.DescribeScalingRulesResponseBodyScalingRulesHybridMetricsDimensions] = None,
        expression: str = None,
        id: str = None,
        metric_name: str = None,
        statistic: str = None,
    ):
        # The dimensions of the metric. Used to specify the resources monitored by the metric.
        self.dimensions = dimensions
        # The metric operation expression for multiple Hybrid Cloud Monitoring metrics. The calculation result of the expression is used to trigger scaling.
        # 
        # The operation expression must meet the Reverse Polish Notation (RPN) specification, and only the `+ - * /` operators are supported.
        self.expression = expression
        # The reference ID of the metric in the metric operation expression.
        self.id = id
        # The name of the monitoring metrics in the monitoring metrics repository for Hybrid Cloud Monitoring.
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
                temp_model = main_models.DescribeScalingRulesResponseBodyScalingRulesHybridMetricsDimensions()
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

class DescribeScalingRulesResponseBodyScalingRulesHybridMetricsDimensions(DaraModel):
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

class DescribeScalingRulesResponseBodyScalingRulesAlarms(DaraModel):
    def __init__(
        self,
        alarm_task_id: str = None,
        alarm_task_name: str = None,
        comparison_operator: str = None,
        dimensions: List[main_models.DescribeScalingRulesResponseBodyScalingRulesAlarmsDimensions] = None,
        evaluation_count: int = None,
        metric_name: str = None,
        metric_type: str = None,
        period: int = None,
        statistics: str = None,
        threshold: float = None,
    ):
        # The ID of the event-triggered task associated with the scaling rule.
        self.alarm_task_id = alarm_task_id
        # The name of the event-triggered task associated with the scaling rule.
        self.alarm_task_name = alarm_task_name
        # The comparison operator used to compare the statistical value of the metric with the threshold for the event-triggered task associated with the scaling rule. This operator specifies the relationship between the statistical value and the threshold that meets the condition. Valid values:
        # 
        # - >=: the statistical value of the metric is greater than or equal to the threshold.
        # - <=: the statistical value of the metric is less than or equal to the threshold.
        # - >: the statistical value of the metric is greater than the threshold.
        # - <: the statistical value of the metric is less than the threshold.
        self.comparison_operator = comparison_operator
        # The dimension information of the event-triggered task associated with the scaling rule.
        self.dimensions = dimensions
        # The number of consecutive times the threshold expression must be met for the event-triggered task associated with the scaling rule to reach the alert state.
        self.evaluation_count = evaluation_count
        # The name of the metric for the event-triggered task associated with the scaling rule.
        self.metric_name = metric_name
        # The type of the event-triggered task associated with the scaling rule. Valid values:
        # 
        # - system: system monitoring event-triggered task.
        # - custom: custom monitoring event-triggered task.
        self.metric_type = metric_type
        # The period for collecting metric data in the target tracking scaling rule.
        self.period = period
        # The statistical method of the event-triggered task associated with the scaling rule. Valid values:
        # 
        # - Average: the average value.
        # - Maximum: the maximum value.
        # - Minimum: the minimum value.
        self.statistics = statistics
        # The alert threshold of the event-triggered task associated with the scaling rule.
        self.threshold = threshold

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
        if self.alarm_task_id is not None:
            result['AlarmTaskId'] = self.alarm_task_id

        if self.alarm_task_name is not None:
            result['AlarmTaskName'] = self.alarm_task_name

        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.period is not None:
            result['Period'] = self.period

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTaskId') is not None:
            self.alarm_task_id = m.get('AlarmTaskId')

        if m.get('AlarmTaskName') is not None:
            self.alarm_task_name = m.get('AlarmTaskName')

        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.DescribeScalingRulesResponseBodyScalingRulesAlarmsDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

class DescribeScalingRulesResponseBodyScalingRulesAlarmsDimensions(DaraModel):
    def __init__(
        self,
        dimension_key: str = None,
        dimension_value: str = None,
    ):
        # The key of the dimension associated with the metric. Valid values:
        # 
        # - scaling_group: the ID of the scaling group.
        # - userId: the ID of the user account.
        self.dimension_key = dimension_key
        # The value of the dimension associated with the metric.
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

class DescribeScalingRulesResponseBodyScalingRulesAlarmDimensions(DaraModel):
    def __init__(
        self,
        dimension_key: str = None,
        dimension_value: str = None,
    ):
        # The key of the dimension associated with the metric.
        self.dimension_key = dimension_key
        # The value of the dimension associated with the metric.
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

