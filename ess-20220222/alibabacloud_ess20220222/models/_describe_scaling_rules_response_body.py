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
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The scaling rules.
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
        # The adjustment method of the scaling rule. Valid values:
        # 
        # *   QuantityChangeInCapacity: adds or removes the specified number of Elastic Compute Service (ECS) instances to or from the scaling group.
        # *   PercentChangeInCapacity: adds or removes the specified percentage of ECS instances to or from the scaling group.
        # *   TotalCapacity: adjusts the number of ECS instances in the scaling group to the specified number.
        self.adjustment_type = adjustment_type
        # The number of instances that must be scaled based on the scaling rule.
        self.adjustment_value = adjustment_value
        # The dimensions. This parameter is applicable to target tracking scaling rules. You can specify this parameter if your predefined metric requires extra dimensions. For example, if you predefine the LoadBalancerRealServerAverageQps metric, you must use this parameter to specify the rulePool dimension.
        self.alarm_dimensions = alarm_dimensions
        # The event-triggered tasks that are associated with the scaling rule. The value of this parameter is returned only if you set ShowAlarmRules to true. Otherwise, null is returned.
        self.alarms = alarms
        # The cooldown period of the scaling rule. This parameter is available only if you set ScalingRuleType to SimpleScalingRule. Valid values: 0 to 86400. Unit: seconds.
        self.cooldown = cooldown
        # Indicates whether scale-in is disabled. This parameter takes effect only if you set ScalingRuleType to TargetTrackingScalingRule. Valid values:
        # 
        # *   true
        # *   false
        self.disable_scale_in = disable_scale_in
        # The warm-up period of instances. During the warm-up period, a series of preparation measures are taken for the new instances. Performance metrics of instances being warmed up are not counted towards the monitoring range.
        self.estimated_instance_warmup = estimated_instance_warmup
        # The Hybrid Cloud Monitoring metrics. For more information, see [Create a custom target tracking scaling rule](https://help.aliyun.com/document_detail/2852162.html).
        self.hybrid_metrics = hybrid_metrics
        # The ID of the Hybrid Cloud Monitoring namespace.
        # 
        # For information about how to manage Hybrid Cloud Monitoring namespaces, see [Manage namespaces](https://help.aliyun.com/document_detail/217606.html).
        self.hybrid_monitor_namespace = hybrid_monitor_namespace
        # The maximum number of ECS instances that can be contained in the scaling group. If you specify this parameter, you must also specify PredictiveValueBehavior.
        self.initial_max_size = initial_max_size
        # The maximum number of ECS instances that can be contained in the scaling group.
        self.max_size = max_size
        # The name of the metric of the event-triggered task that is associated with the scaling rule.
        self.metric_name = metric_name
        # The metric type. Valid values:
        # 
        # *   system: system metrics of CloudMonitor.
        # *   custom: custom metrics that are reported to CloudMonitor.
        # *   hybrid: metrics of Hybrid Cloud Monitoring.
        self.metric_type = metric_type
        # The minimum number of instances that must be scaled. This parameter takes effect only if you set ScalingRuleType to SimpleScalingRule or StepScalingRule and set AdjustmentType to PercentChangeInCapacity.
        self.min_adjustment_magnitude = min_adjustment_magnitude
        # The minimum number of ECS instances that must be contained in the scaling group.
        self.min_size = min_size
        # The mode of the predictive scaling rule. Valid values:
        # 
        # *   PredictAndScale: provides predictions and creates prediction tasks.
        # *   PredictOnly: provides predictions but does not create prediction tasks.
        self.predictive_scaling_mode = predictive_scaling_mode
        # The amount of buffer time before prediction tasks are executed. By default, all prediction tasks that are automatically created based on a predictive scaling rule are executed on the hour. You can specify a buffer time for resource preparation before prediction tasks are executed. Valid values: 0 to 60. Unit: minutes.
        self.predictive_task_buffer_time = predictive_task_buffer_time
        # The action on the predicted maximum value. Valid values:
        # 
        # *   MaxOverridePredictiveValue: uses the initial maximum capacity as the maximum value for prediction tasks if the predicted value is greater than the initial maximum capacity.
        # *   PredictiveValueOverrideMax: uses the predicted value as the maximum value for prediction tasks when the predicted value is greater than the initial maximum capacity.
        # *   PredictiveValueOverrideMaxWithBuffer: increases the predicted value by a ratio that is specified by PredictiveValueBuffer, and uses the increased value as the maximum value for prediction tasks if the predicted value increased by this ratio is greater than the initial maximum capacity.
        self.predictive_value_behavior = predictive_value_behavior
        # The ratio based on which the predicted value is increased when PredictiveValueBehavior is set to PredictiveValueOverrideMaxWithBuffer. If the predicted value increased by this ratio is greater than the initial maximum capacity, the increased value is used as the maximum value for prediction tasks. Valid values: 0 to 100.
        self.predictive_value_buffer = predictive_value_buffer
        # The number of consecutive times that the event-triggered task for scale-in purposes must meet the threshold conditions before an alert is triggered. After a target tracking scaling rule is created, an event-triggered task is automatically created and associated with the target tracking scaling rule.
        self.scale_in_evaluation_count = scale_in_evaluation_count
        # The number of consecutive times that the event-triggered task created for scale-out purposes must meet the threshold conditions before an alert is triggered. After a target tracking scaling rule is created, an event-triggered task is automatically created and associated with the target tracking scaling rule.
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
        # *   SimpleScalingRule: a simple scaling rule. Once a simple scaling rule is executed, Auto Scaling adjusts the number of ECS instances in the scaling group based on the values of AdjustmentType and AdjustmentValue.
        # *   TargetTrackingScalingRule: a target tracking scaling rule. Once a target tracking scaling rule is executed, Auto Scaling dynamically calculates the number of ECS instances or elastic container instances to scale based on the predefined metric (MetricName) and attempts to maintain the metric value close to the specified target value (TargetValue).
        # *   StepScalingRule: a step scaling rule. Once a step scaling rule is executed, Auto Scaling scales instances step by step based on the predefined thresholds and metric values.
        # *   PredictiveScalingRule: a predictive scaling rule. Once a predictive scaling rule is executed, Auto Scaling analyzes the historical monitoring data based on the machine learning technology and predicts the trends of metric data. Auto Scaling also creates scheduled tasks to enable dynamic adjustment of the boundary values for the scaling group.
        self.scaling_rule_type = scaling_rule_type
        # The step adjustments of the step scaling rule.
        self.step_adjustments = step_adjustments
        # The target value of the metric. If you set ScalingRuleType to TargetTrackingScalingRule or PredictiveScalingRule, Auto Scaling keeps the metric value close to the target value by adding instances to or removing instances from the scaling group.
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
        # The lower limit of a step adjustment. Valid values: -9.999999E18 to 9.999999E18.
        self.metric_interval_lower_bound = metric_interval_lower_bound
        # The upper limit of a step adjustment. Valid values: -9.999999E18 to 9.999999E18.
        self.metric_interval_upper_bound = metric_interval_upper_bound
        # The number of ECS instances that are scaled in a step adjustment.
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
        # The metric dimensions. This parameter is used to specify the monitored resources.
        self.dimensions = dimensions
        # The metric expression that consists of multiple Hybrid Cloud Monitoring metrics. It calculates a result used to trigger scaling events.
        # 
        # The expression is written in Reverse Polish Notation (RPN) format and supports only the following operators: `+, -, *, /`.
        self.expression = expression
        # The reference ID of the metric in the metric expression.
        self.id = id
        # The name of the Hybrid Cloud Monitoring metric.
        self.metric_name = metric_name
        # The statistical method of the metric value. Valid values:
        # 
        # *   Average: The average value of all metric values within a specified interval is calculated.
        # *   Minimum: The minimum value of all metric values within a specified interval is calculated.
        # *   Maximum: The maximum value of all metric values within a specified interval is calculated.
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
        # The key of the metric dimension.
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
        # The ID of the event-triggered task that is associated with the scaling rule.
        self.alarm_task_id = alarm_task_id
        # The name of the event-triggered task that is associated with the scaling rule.
        self.alarm_task_name = alarm_task_name
        # The comparison operator between the statistical value and the threshold of the metric of the event-triggered task that is associated with the scaling rule. The comparison operator indicates the relationship in which the metric value and the metric threshold can meet the alert condition.
        # 
        # *   Valid value if the metric value is greater than or equal to the threshold: >=
        # *   Valid value if the metric value is less than or equal to the threshold: <=
        # *   Valid value if the metric value is greater than the threshold: >
        # *   Valid value if the metric value is less than the threshold: <
        self.comparison_operator = comparison_operator
        # The dimensions of the event-triggered task that is associated with the scaling rule.
        self.dimensions = dimensions
        # The number of consecutive times when the event-triggered task that is associated with the scaling rule must meet the alert condition before an alert is triggered.
        self.evaluation_count = evaluation_count
        # The name of the metric of the event-triggered task that is associated with the scaling rule.
        self.metric_name = metric_name
        # The type of the metric of the event-triggered task that is associated with the scaling rule. Valid values:
        # 
        # *   system: system metrics
        # *   custom: custom metrics
        self.metric_type = metric_type
        # The statistical period of the metric data in the target tracking scaling rule.
        self.period = period
        # The statistical method of the event-triggered task that is associated with the scaling rule. Valid values:
        # 
        # *   Average
        # *   Maximum
        # *   Minimum
        self.statistics = statistics
        # The alert threshold of the event-triggered task that is associated with the scaling rule.
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
        # The key of the dimension that is associated with the metric. Valid values:
        # 
        # *   ScalingGroupId: the ID of the scaling group.
        # *   userId: the ID of the user account.
        self.dimension_key = dimension_key
        # The value of the dimension that is associated with the metric.
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
        # The dimension key of the metric.
        self.dimension_key = dimension_key
        # The dimension value of the metric.
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

