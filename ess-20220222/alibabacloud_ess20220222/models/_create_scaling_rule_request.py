# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class CreateScalingRuleRequest(DaraModel):
    def __init__(
        self,
        adjustment_type: str = None,
        adjustment_value: int = None,
        alarm_dimensions: List[main_models.CreateScalingRuleRequestAlarmDimensions] = None,
        alarm_options: main_models.CreateScalingRuleRequestAlarmOptions = None,
        cooldown: int = None,
        disable_scale_in: bool = None,
        estimated_instance_warmup: int = None,
        hybrid_metrics: List[main_models.CreateScalingRuleRequestHybridMetrics] = None,
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
        region_id: str = None,
        resource_owner_account: str = None,
        scale_in_evaluation_count: int = None,
        scale_out_evaluation_count: int = None,
        scaling_group_id: str = None,
        scaling_rule_name: str = None,
        scaling_rule_type: str = None,
        step_adjustments: List[main_models.CreateScalingRuleRequestStepAdjustments] = None,
        target_value: float = None,
    ):
        # The scaling method of the scaling rule. This parameter is required only if you set the ScalingRuleType parameter to SimpleScalingRule or StepScalingRule. Valid values:
        # 
        # *   QuantityChangeInCapacity: adds the specified number of ECS instances to or removes the specified number of ECS instances from the scaling group.
        # *   PercentChangeInCapacity: adds the specified percentage of ECS instances to or removes the specified percentage of ECS instances from the scaling group.
        # *   TotalCapacity: adjusts the number of ECS instances in the scaling group to a specified number.
        self.adjustment_type = adjustment_type
        # The number of instances that must be scaled based on the scaling rule. This parameter is required only if you set the ScalingRuleType parameter to SimpleScalingRule or StepScalingRule. The number of ECS instances that are scaled in a single scaling activity cannot exceed 1,000.
        # 
        # *   Valid values if you set the AdjustmentType parameter to QuantityChangeInCapacity: -1000 to 1000.
        # *   Valid values if you set the AdjustmentType parameter to PercentChangeInCapacity: -100 to 10000.
        # *   Valid values if you set the AdjustmentType parameter to TotalCapacity: 0 to 2000.
        self.adjustment_value = adjustment_value
        # The metric dimensions. This parameter is applicable to target tracking scaling rules. If your predefined metric requires extra dimensions, you must specify this parameter. For example, if you use LoadBalancerRealServerAverageQps as your predefined metric, you must use this parameter to specify the rulePool dimension.
        self.alarm_dimensions = alarm_dimensions
        self.alarm_options = alarm_options
        # The cooldown time of the scaling rule. This parameter is available only if you set the ScalingRuleType parameter to SimpleScalingRule. Valid values: 0 to 86400. Unit: seconds.
        # 
        # By default, this parameter is left empty.
        self.cooldown = cooldown
        # Specifies whether to disable scale-in. This parameter is available only if you set ScalingRuleType to TargetTrackingScalingRule.
        # 
        # Default value: false.
        self.disable_scale_in = disable_scale_in
        # The warmup period of an instance. This parameter is available only if you set the ScalingRuleType parameter to TargetTrackingScalingRule or PredictiveScalingRule. Auto Scaling adds ECS instances that are in the warmup state to a scaling group but does not report monitoring data to CloudMonitor during the warmup period.
        # 
        # > Auto Scaling calculates the number of ECS instances that must be scaled. ECS instances in the warmup state are not counted towards the current capacity of the scaling group.
        # 
        # Valid values: 0 to 86400. Unit: seconds.
        # 
        # Default value: 300.
        self.estimated_instance_warmup = estimated_instance_warmup
        # The Hybrid Cloud Monitoring metrics. For more information, see [Create a custom target tracking scaling rule](https://help.aliyun.com/document_detail/2852162.html).
        self.hybrid_metrics = hybrid_metrics
        # The ID of the Hybrid Cloud Monitoring namespace.
        # 
        # For information about how to manage Hybrid Cloud Monitoring namespaces, see [Manage namespaces](https://help.aliyun.com/document_detail/217606.html).
        self.hybrid_monitor_namespace = hybrid_monitor_namespace
        # The maximum number of ECS instances that can be contained in the scaling group. If you specify InitialMaxSize, you must specify `PredictiveValueBehavior`.
        # 
        # The default value of this parameter is the value of MaxSize.
        self.initial_max_size = initial_max_size
        # The predefined metric that you want to monitor. If you set ScalingRuleType to TargetTrackingScalingRule or PredictiveScalingRule, you must specify this parameter.
        # 
        # Valid values if you set ScalingRuleType to TargetTrackingScalingRule:
        # 
        # *   CpuUtilizationAgent (recommended): the CPU utilization.
        # *   MemoryUtilization (recommended): the memory usage.
        # *   CpuUtilization: the average CPU utilization.
        # *   IntranetTx: the outbound traffic over an internal network.
        # *   IntranetRx: the average inbound traffic over an internal network.
        # *   VpcInternetTx: the outbound traffic from a virtual private cloud (VPC) to the Internet.
        # *   VpcInternetRx: the inbound traffic from the Internet to a VPC.
        # *   LoadBalancerRealServerAverageQps:the queries per second (QPS) per Application Load Balancer (ALB) server group.
        # 
        # Valid values if you set ScalingRuleType to PredictiveScalingRule:
        # 
        # *   CpuUtilization: the average CPU utilization.
        # *   IntranetRx: the average inbound traffic over an internal network.
        # *   IntranetTx: the average outbound traffic over an internal network.
        # 
        # For more information, see [Event-triggered tasks of the system monitoring type](https://help.aliyun.com/document_detail/74854.html).
        self.metric_name = metric_name
        # The metric type. Valid values:
        # 
        # *   system: system metrics of CloudMonitor.
        # *   custom: custom metrics that are reported to CloudMonitor.
        # *   hybrid: metrics of Hybrid Cloud Monitoring.
        self.metric_type = metric_type
        # The minimum number of instances that must be scaled when the AdjustmentType parameter is set to PercentChangeInCapacity. This parameter takes effect only if you set the ScalingRuleType parameter to SimpleScalingRule or StepScalingRule.
        self.min_adjustment_magnitude = min_adjustment_magnitude
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The mode of the predictive scaling rule. Valid values:
        # 
        # *   PredictAndScale: produces predictions and creates prediction tasks.
        # *   PredictOnly: produces predictions but does not create prediction tasks.
        # 
        # Default value: PredictAndScale.
        self.predictive_scaling_mode = predictive_scaling_mode
        # The amount of buffer time before the prediction task is executed. By default, all prediction tasks that are automatically created for a predictive scaling rule are executed on the hour. You can specify an amount of buffer time for resource preparation before the prediction tasks are executed. Valid values: 0 to 60. Unit: minutes.
        # 
        # Default value: 0.
        self.predictive_task_buffer_time = predictive_task_buffer_time
        # The maximum value for predication tasks. Valid values:
        # 
        # *   MaxOverridePredictiveValue: uses the initial maximum capacity as the maximum value for prediction tasks if the predicted value is greater than the initial maximum capacity.
        # *   PredictiveValueOverrideMax: uses the predicted value as the maximum value for prediction tasks if the predicted value is greater than the initial maximum capacity.
        # *   PredictiveValueOverrideMaxWithBuffer: increases the predicted value by a percentage that is specified by the PredictiveValueBuffer parameter. If the predicted value that is increased by the percentage is greater than the initial maximum capacity, the increased value is used as the maximum value for prediction tasks.
        # 
        # Default value: MaxOverridePredictiveValue.
        self.predictive_value_behavior = predictive_value_behavior
        # The ratio based on which the predicted value is increased when you set `PredictiveValueBehavior` to `PredictiveValueOverrideMaxWithBuffer`. If the predicted value increased by this ratio is greater than the initial maximum capacity, the increased value is used as the maximum value for prediction tasks. Valid values: 0 to 100.
        # 
        # Default value: 0.
        self.predictive_value_buffer = predictive_value_buffer
        # The region ID of the scaling group.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The number of consecutive times that the event-triggered task created for scale-in activities must meet the threshold conditions before an alert is triggered. After a target tracking scaling rule is created, an event-triggered task is automatically created and then associated with the target tracking scaling rule.
        # 
        # Default value: 15.
        self.scale_in_evaluation_count = scale_in_evaluation_count
        # The number of consecutive times that the event-triggered task created for scale-out activities must meet the threshold conditions before an alert is triggered. After a target tracking scaling rule is created, an event-triggered task is automatically created and then associated with the target tracking scaling rule.
        # 
        # Default value: 3.
        self.scale_out_evaluation_count = scale_out_evaluation_count
        # The ID of the scaling group to which the scaling rule belongs.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The name of the scaling rule. The name must be 2 to 64 characters in length, and can contain letters, digits, underscores (_), hyphens (-), and periods (.). The name must start with a letter or a digit.
        # 
        # The name of each scaling rule must be unique under the same account within a region.
        # 
        # If you leave this parameter empty, the scaling rule ID is used.
        self.scaling_rule_name = scaling_rule_name
        # The type of the scaling rule. Valid values:
        # 
        # *   SimpleScalingRule: a simple scaling rule. After you execute a simple scaling rule, Auto Scaling adjusts the number of ECS instances or elastic container instances in the scaling group based on the values of AdjustmentType and AdjustmentValue.
        # *   TargetTrackingScalingRule: a target tracking scaling rule. After you execute a target tracking scaling rule, Auto Scaling dynamically calculates the number of ECS instances or elastic container instances to scale based on the predefined metric (MetricName) and attempts to maintain the metric value close to the expected value (TargetValue).
        # *   StepScalingRule: a step scaling rule. After you execute a step scaling rule, Auto Scaling scales instances step by step based on the predefined thresholds and metric values.
        # *   PredictiveScalingRule: a predictive scaling rule. After you execute a predictive scaling rule, Auto Scaling uses machine learning to analyze historical monitoring data of the scaling group and predicts the future values of metrics. In addition, Auto Scaling automatically creates scheduled tasks to adjust the boundary values for the scaling group.
        # 
        # Default value: SimpleScalingRule.
        self.scaling_rule_type = scaling_rule_type
        # Details of the step adjustments.
        self.step_adjustments = step_adjustments
        # The target value. This parameter is required only if you set the ScalingRuleType parameter to TargetTrackingScalingRule or PredictiveScalingRule. The value must be greater than 0 and can have up to three decimal places.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scale_in_evaluation_count is not None:
            result['ScaleInEvaluationCount'] = self.scale_in_evaluation_count

        if self.scale_out_evaluation_count is not None:
            result['ScaleOutEvaluationCount'] = self.scale_out_evaluation_count

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

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
                temp_model = main_models.CreateScalingRuleRequestAlarmDimensions()
                self.alarm_dimensions.append(temp_model.from_map(k1))

        if m.get('AlarmOptions') is not None:
            temp_model = main_models.CreateScalingRuleRequestAlarmOptions()
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
                temp_model = main_models.CreateScalingRuleRequestHybridMetrics()
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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScaleInEvaluationCount') is not None:
            self.scale_in_evaluation_count = m.get('ScaleInEvaluationCount')

        if m.get('ScaleOutEvaluationCount') is not None:
            self.scale_out_evaluation_count = m.get('ScaleOutEvaluationCount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')

        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')

        self.step_adjustments = []
        if m.get('StepAdjustments') is not None:
            for k1 in m.get('StepAdjustments'):
                temp_model = main_models.CreateScalingRuleRequestStepAdjustments()
                self.step_adjustments.append(temp_model.from_map(k1))

        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')

        return self

class CreateScalingRuleRequestStepAdjustments(DaraModel):
    def __init__(
        self,
        metric_interval_lower_bound: float = None,
        metric_interval_upper_bound: float = None,
        scaling_adjustment: int = None,
    ):
        # The lower limit specified in a step adjustment. This parameter is available only if you set the ScalingRuleType parameter to StepScalingRule. Valid values: -9.999999E18 to 9.999999E18.
        self.metric_interval_lower_bound = metric_interval_lower_bound
        # The upper limit that is specified in a step adjustment. Valid values: -9.999999E18 to 9.999999E18.
        self.metric_interval_upper_bound = metric_interval_upper_bound
        # The number of ECS instances that you want to scale in a step adjustment. This parameter is available only if you set the ScalingRuleType parameter to StepScalingRule.
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

class CreateScalingRuleRequestHybridMetrics(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.CreateScalingRuleRequestHybridMetricsDimensions] = None,
        expression: str = None,
        id: str = None,
        metric_name: str = None,
        statistic: str = None,
    ):
        # The metric dimensions. You can use this parameter to specify the monitored resources.
        self.dimensions = dimensions
        # The metric expression that consists of multiple Hybrid Cloud Monitoring metrics. It calculates a result used to trigger scaling events.
        # 
        # The expression must be written in Reverse Polish Notation (RPN) format and supports only the following operators: `+, -, *, /`.
        self.expression = expression
        # The reference ID of the metric in the metric expression.
        self.id = id
        # The name of the Hybrid Cloud Monitoring metric.
        self.metric_name = metric_name
        # The statistical method of the metric value. Valid values:
        # 
        # *   Average: calculates the average value of all metric values within a specified interval.
        # *   Minimum: calculates the minimum value of all metric values within a specified interval.
        # *   Maximum: calculates the maximum value of all metric values within a specified interval.
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
                temp_model = main_models.CreateScalingRuleRequestHybridMetricsDimensions()
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

class CreateScalingRuleRequestHybridMetricsDimensions(DaraModel):
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

class CreateScalingRuleRequestAlarmOptions(DaraModel):
    def __init__(
        self,
        period: int = None,
    ):
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

class CreateScalingRuleRequestAlarmDimensions(DaraModel):
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

